#!/usr/bin/env python3
"""
Local LeetCode-style UI for the blind75/ problem set.

Zero third-party dependencies (stdlib only). Run:
    python3 leetcode_ui/server.py
then open http://localhost:8765
"""

import json
import re
import subprocess
import sys
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import urlparse, parse_qs

ROOT = Path(__file__).resolve().parent.parent
BLIND75 = ROOT / "blind75"
STATIC_DIR = Path(__file__).resolve().parent / "static"
PROGRESS_FILE = Path(__file__).resolve().parent / "progress.json"

CATEGORY_RE = re.compile(r"^\d{2}_")


def category_dirs():
    return sorted(
        d for d in BLIND75.iterdir()
        if d.is_dir() and CATEGORY_RE.match(d.name) and d.name != "tests"
    )


def problem_files(category_dir: Path):
    return sorted(
        f for f in category_dir.glob("*.py")
        if f.name != "__init__.py"
    )


def test_file_for(category: str, slug: str):
    return BLIND75 / "tests" / category / f"test_{slug}.py"


def parse_docstring(py_path: Path):
    """Pull the module docstring and split out title/meta/body."""
    try:
        text = py_path.read_text()
    except OSError:
        return {"title": py_path.stem, "meta": "", "body": ""}

    m = re.match(r'\s*"""(.*?)"""', text, re.DOTALL)
    if not m:
        return {"title": py_path.stem, "meta": "", "body": ""}

    doc = m.group(1).strip("\n")
    lines = doc.split("\n")
    title_line = lines[0].strip() if lines else py_path.stem
    rest = "\n".join(lines[1:]).strip("\n")
    return {"title": title_line, "meta": "", "body": rest}


def is_stub(py_path: Path) -> bool:
    """Best-effort: True if the Solution class's primary method body is just `pass`."""
    try:
        import ast
        tree = ast.parse(py_path.read_text())
    except (OSError, SyntaxError):
        return False

    for node in ast.walk(tree):
        if isinstance(node, ast.ClassDef) and node.name == "Solution":
            for m in node.body:
                if isinstance(m, ast.FunctionDef):
                    body = [
                        n for n in m.body
                        if not (isinstance(n, ast.Expr) and isinstance(getattr(n, "value", None), ast.Constant))
                    ]
                    if len(body) == 1 and isinstance(body[0], ast.Pass):
                        return True
    return False


def load_progress():
    if PROGRESS_FILE.exists():
        try:
            return json.loads(PROGRESS_FILE.read_text())
        except (OSError, json.JSONDecodeError):
            return {}
    return {}


def save_progress(data):
    PROGRESS_FILE.write_text(json.dumps(data, indent=2))


def list_problems():
    progress = load_progress()
    categories = []
    for cat_dir in category_dirs():
        problems = []
        for py in problem_files(cat_dir):
            slug = py.stem
            doc = parse_docstring(py)
            key = f"{cat_dir.name}/{slug}"
            problems.append({
                "slug": slug,
                "category": cat_dir.name,
                "title": doc["title"],
                "stub": is_stub(py),
                "solved": progress.get(key, {}).get("solved", False),
            })
        categories.append({"name": cat_dir.name, "problems": problems})
    return categories


def run_tests(category: str, slug: str):
    test_path = test_file_for(category, slug)
    if not test_path.exists():
        return {"ok": False, "error": f"No test file found at {test_path}"}

    proc = subprocess.run(
        [sys.executable, "-m", "pytest", "-v", str(test_path)],
        cwd=str(BLIND75),
        capture_output=True,
        text=True,
        timeout=30,
    )
    passed = proc.returncode == 0
    output = proc.stdout + "\n" + proc.stderr

    cases = []
    for line in proc.stdout.splitlines():
        m = re.match(r"^(\S+::\S+)\s+(PASSED|FAILED|ERROR)", line)
        if m:
            cases.append({"name": m.group(1), "status": m.group(2)})

    if passed:
        key = f"{category}/{slug}"
        progress = load_progress()
        progress.setdefault(key, {})["solved"] = True
        save_progress(progress)

    return {"ok": True, "passed": passed, "output": output, "cases": cases}


class Handler(BaseHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # keep stdout quiet

    def _send_json(self, obj, status=200):
        body = json.dumps(obj).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _send_file(self, path: Path, content_type: str):
        try:
            body = path.read_bytes()
        except OSError:
            self.send_response(404)
            self.end_headers()
            return
        self.send_response(200)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def do_GET(self):
        parsed = urlparse(self.path)
        path = parsed.path
        qs = parse_qs(parsed.query)

        if path == "/" or path == "/index.html":
            self._send_file(STATIC_DIR / "index.html", "text/html")
            return

        if path == "/app.js":
            self._send_file(STATIC_DIR / "app.js", "application/javascript")
            return

        if path.startswith("/vendor/"):
            name = path[len("/vendor/"):]
            if "/" in name or "\\" in name:
                self.send_response(404)
                self.end_headers()
                return
            vendor_path = STATIC_DIR / "vendor" / name
            content_type = "text/css" if name.endswith(".css") else "application/javascript"
            self._send_file(vendor_path, content_type)
            return

        if path == "/api/problems":
            self._send_json({"categories": list_problems()})
            return

        if path == "/api/problem":
            category = qs.get("category", [""])[0]
            slug = qs.get("slug", [""])[0]
            py = BLIND75 / category / f"{slug}.py"
            if not py.exists():
                self._send_json({"error": "not found"}, 404)
                return
            doc = parse_docstring(py)
            test_path = test_file_for(category, slug)
            self._send_json({
                "slug": slug,
                "category": category,
                "title": doc["title"],
                "docstring": doc["body"],
                "code": py.read_text(),
                "has_test": test_path.exists(),
            })
            return

        self.send_response(404)
        self.end_headers()

    def do_POST(self):
        parsed = urlparse(self.path)
        path = parsed.path
        length = int(self.headers.get("Content-Length", 0))
        raw = self.rfile.read(length) if length else b"{}"
        try:
            payload = json.loads(raw)
        except json.JSONDecodeError:
            payload = {}

        if path == "/api/save":
            category = payload.get("category", "")
            slug = payload.get("slug", "")
            code = payload.get("code", "")
            py = BLIND75 / category / f"{slug}.py"
            if not py.exists():
                self._send_json({"ok": False, "error": "problem file not found"}, 404)
                return
            py.write_text(code)
            self._send_json({"ok": True})
            return

        if path == "/api/run":
            category = payload.get("category", "")
            slug = payload.get("slug", "")
            code = payload.get("code")
            py = BLIND75 / category / f"{slug}.py"
            if not py.exists():
                self._send_json({"ok": False, "error": "problem file not found"}, 404)
                return
            if code is not None:
                py.write_text(code)
            result = run_tests(category, slug)
            self._send_json(result)
            return

        self.send_response(404)
        self.end_headers()


def main():
    port = 8765
    server = ThreadingHTTPServer(("localhost", port), Handler)
    print(f"LeetCode UI running at http://localhost:{port}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
