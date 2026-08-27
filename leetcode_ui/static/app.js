const sidebar = document.getElementById("sidebar");
const main = document.getElementById("main");

let current = null; // { category, slug }
let categoriesData = [];
let editor = null; // CodeMirror instance

function humanizeCategory(name) {
  return name.replace(/^\d{2}_/, "").replace(/_/g, " ")
    .replace(/\b\w/g, c => c.toUpperCase());
}

async function loadProblems() {
  const res = await fetch("/api/problems");
  const data = await res.json();
  categoriesData = data.categories;
  renderSidebar();
}

function renderSidebar() {
  sidebar.innerHTML = "";
  for (const cat of categoriesData) {
    const catEl = document.createElement("div");
    catEl.className = "category";

    const header = document.createElement("div");
    header.className = "category-header";
    const solvedCount = cat.problems.filter(p => p.solved).length;
    header.innerHTML = `<span>${humanizeCategory(cat.name)}</span><span>${solvedCount}/${cat.problems.length}</span>`;

    const list = document.createElement("div");
    list.className = "problem-list";

    header.addEventListener("click", () => list.classList.toggle("collapsed"));

    for (const p of cat.problems) {
      const item = document.createElement("div");
      item.className = "problem-item";
      if (current && current.category === p.category && current.slug === p.slug) {
        item.classList.add("active");
      }
      const marker = p.solved
        ? `<span class="check">&#10003;</span>`
        : `<span class="stub-dot" style="background:${p.stub ? '#8a8a8a' : '#e5c07b'}"></span>`;
      item.innerHTML = `${marker}<span>${p.title}</span>`;
      item.addEventListener("click", () => openProblem(p.category, p.slug));
      list.appendChild(item);
    }

    catEl.appendChild(header);
    catEl.appendChild(list);
    sidebar.appendChild(catEl);
  }
}

async function openProblem(category, slug) {
  current = { category, slug };
  const res = await fetch(`/api/problem?category=${encodeURIComponent(category)}&slug=${encodeURIComponent(slug)}`);
  if (!res.ok) return;
  const data = await res.json();
  renderMain(data);
  renderSidebar();
}

function renderMain(data) {
  main.innerHTML = `
    <div id="desc-pane">
      <h1>${escapeHtml(data.title)}</h1>
      <pre>${escapeHtml(data.docstring)}</pre>
    </div>
    <div id="code-pane">
      <div id="code-toolbar">
        <button id="run-btn">Run Tests</button>
        <button id="save-btn" class="secondary">Save</button>
        <span id="save-indicator" style="color:var(--muted); font-size:12px;"></span>
      </div>
      <div id="editor-container"></div>
      <div id="results" class="empty">Run tests to see results here.</div>
    </div>
  `;

  editor = CodeMirror(document.getElementById("editor-container"), {
    value: data.code,
    mode: "python",
    theme: "dracula",
    lineNumbers: true,
    indentUnit: 4,
    tabSize: 4,
    indentWithTabs: false,
    styleActiveLine: true,
    matchBrackets: true,
    autoCloseBrackets: true,
    extraKeys: {
      "Tab": (cm) => cm.replaceSelection("    ", "end"),
    },
  });

  document.getElementById("save-btn").addEventListener("click", () => saveCode(false));
  document.getElementById("run-btn").addEventListener("click", runTests);
}

function escapeHtml(s) {
  const div = document.createElement("div");
  div.textContent = s;
  return div.innerHTML;
}

async function saveCode(silent) {
  const indicator = document.getElementById("save-indicator");
  await fetch("/api/save", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ category: current.category, slug: current.slug, code: editor.getValue() }),
  });
  if (!silent && indicator) {
    indicator.textContent = "Saved";
    setTimeout(() => { indicator.textContent = ""; }, 1500);
  }
}

async function runTests() {
  const results = document.getElementById("results");
  const runBtn = document.getElementById("run-btn");
  runBtn.disabled = true;
  runBtn.textContent = "Running...";
  results.className = "";
  results.innerHTML = "Running tests...";

  try {
    const res = await fetch("/api/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ category: current.category, slug: current.slug, code: editor.getValue() }),
    });
    const data = await res.json();

    if (!data.ok) {
      results.innerHTML = `<div class="result-status fail">Error</div><div>${escapeHtml(data.error || "unknown error")}</div>`;
      return;
    }

    const statusClass = data.passed ? "pass" : "fail";
    const statusText = data.passed ? "All tests passed" : "Some tests failed";
    let html = `<div class="result-status ${statusClass}">${statusText}</div>`;

    if (data.cases.length) {
      for (const c of data.cases) {
        const shortName = c.name.split("::").pop();
        html += `<div class="case-row ${c.status}">${c.status === "PASSED" ? "✓" : "✗"} ${escapeHtml(shortName)}</div>`;
      }
    }
    html += `<div id="raw-output">${escapeHtml(data.output)}</div>`;
    results.innerHTML = html;

    if (data.passed) {
      loadProblems();
    }
  } catch (err) {
    results.innerHTML = `<div class="result-status fail">Request failed</div><div>${escapeHtml(String(err))}</div>`;
  } finally {
    runBtn.disabled = false;
    runBtn.textContent = "Run Tests";
  }
}

loadProblems();
