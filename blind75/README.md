# Blind 75

The 75 LeetCode problems, scaffolded for practice. Each problem is a stub with
the statement, examples, constraints, an approach hint and a target complexity —
plus a pytest file with the LeetCode examples and edge cases already written.

You write the solution. The tests tell you whether it's right.

## Running

**Run the problem file itself** — it executes that problem's tests:

```bash
.venv/bin/python blind75/01_arrays/two_sum.py
```

In VS Code, point the interpreter at `.venv` (Cmd+Shift+P → "Python: Select
Interpreter") and the ▶ Run button on any problem file does the same thing.

Or drive pytest directly:

```bash
cd blind75
../.venv/bin/pytest tests/01_arrays/test_two_sum.py   # one problem
../.venv/bin/pytest tests/01_arrays                   # one category
../.venv/bin/pytest                                   # everything
```

Activate the venv (`source .venv/bin/activate`) and it's just `python` / `pytest`.

Every test fails right now — the stubs are empty. That's the starting line.

## Layout

```
blind75/
  01_arrays/
    two_sum.py                    <- you write this
  ...
  tests/
    01_arrays/
      test_two_sum.py             <- already written, don't edit
  common/structures.py            <- ListNode, TreeNode, GraphNode + helpers
  conftest.py                     <- wires up the import paths
```

Problem folders hold only problems; every test lives under `tests/`, mirroring
the same category names.

Method names match LeetCode exactly (`twoSum`, not `two_sum`), so a finished
solution can be pasted straight into the LeetCode editor.

The problems that need a linked list or tree take real `ListNode`/`TreeNode`
objects, same as LeetCode — the tests build them from list literals via
`common.structures`.

## Suggested order

Categories are numbered in a reasonable study order: arrays and strings build
the sliding-window and two-pointer instincts everything else leans on, trees and
graphs share a traversal skeleton, and DP is worth saving until pattern
recognition is cheap.

## Progress

Tick these off as the tests go green.

### 01 — Arrays (10)

- [x] [Two Sum](01_arrays/two_sum.py) — Easy — hash map
- [x] [Best Time to Buy and Sell Stock](01_arrays/best_time_to_buy_and_sell_stock.py) — Easy — one pass
- [x] [Contains Duplicate](01_arrays/contains_duplicate.py) — Easy — set
- [x] [Product of Array Except Self](01_arrays/product_of_array_except_self.py) — Medium — prefix/suffix
- [x] [Maximum Subarray](01_arrays/maximum_subarray.py) — Medium — Kadane
- [x] [Maximum Product Subarray](01_arrays/maximum_product_subarray.py) — Medium — Kadane, min+max
- [x] [Find Minimum in Rotated Sorted Array](01_arrays/find_minimum_in_rotated_sorted_array.py) — Medium — binary search
- [x] [Search in Rotated Sorted Array](01_arrays/search_in_rotated_sorted_array.py) — Medium — binary search
- [x] [3Sum](01_arrays/three_sum.py) — Medium — sort + two pointers
- [x] [Container With Most Water](01_arrays/container_with_most_water.py) — Medium — two pointers

### 02 — Binary (5)

- [ ] [Sum of Two Integers](02_binary/sum_of_two_integers.py) — Medium — XOR + carry
- [ ] [Number of 1 Bits](02_binary/number_of_1_bits.py) — Easy — `n & (n-1)`
- [ ] [Counting Bits](02_binary/counting_bits.py) — Easy — DP on bits
- [ ] [Missing Number](02_binary/missing_number.py) — Easy — XOR or Gauss
- [ ] [Reverse Bits](02_binary/reverse_bits.py) — Easy — shift 32 times

### 03 — Dynamic Programming (11)

- [x] [Climbing Stairs](03_dynamic_programming/climbing_stairs.py) — Easy — Fibonacci
- [x] [Coin Change](03_dynamic_programming/coin_change.py) — Medium — unbounded knapsack
- [x] [Longest Increasing Subsequence](03_dynamic_programming/longest_increasing_subsequence.py) — Medium — patience sorting
- [x] [Longest Common Subsequence](03_dynamic_programming/longest_common_subsequence.py) — Medium — 2D grid DP
- [x] [Word Break](03_dynamic_programming/word_break.py) — Medium — DP over prefixes
- [x] [Combination Sum IV](03_dynamic_programming/combination_sum_iv.py) — Medium — loop order matters
- [x] [House Robber](03_dynamic_programming/house_robber.py) — Medium — take/skip
- [x] [House Robber II](03_dynamic_programming/house_robber_ii.py) — Medium — run it twice
- [x] [Decode Ways](03_dynamic_programming/decode_ways.py) — Medium — Fibonacci with gates
- [x] [Unique Paths](03_dynamic_programming/unique_paths.py) — Medium — grid DP
- [x] [Jump Game](03_dynamic_programming/jump_game.py) — Medium — greedy reach

### 04 — Graphs (8)

- [ ] [Clone Graph](04_graphs/clone_graph.py) — Medium — DFS + memo
- [ ] [Course Schedule](04_graphs/course_schedule.py) — Medium — cycle detection
- [ ] [Pacific Atlantic Water Flow](04_graphs/pacific_atlantic_water_flow.py) — Medium — reverse DFS from edges
- [ ] [Number of Islands](04_graphs/number_of_islands.py) — Medium — flood fill
- [ ] [Longest Consecutive Sequence](04_graphs/longest_consecutive_sequence.py) — Medium — set + run starts
- [ ] [Alien Dictionary](04_graphs/alien_dictionary.py) — Hard — topological sort — *premium*
- [ ] [Graph Valid Tree](04_graphs/graph_valid_tree.py) — Medium — union-find — *premium*
- [ ] [Number of Connected Components](04_graphs/number_of_connected_components.py) — Medium — union-find — *premium*

### 05 — Intervals (5)

- [ ] [Insert Interval](05_intervals/insert_interval.py) — Medium — three-phase pass
- [ ] [Merge Intervals](05_intervals/merge_intervals.py) — Medium — sort by start
- [ ] [Non-overlapping Intervals](05_intervals/non_overlapping_intervals.py) — Medium — greedy, sort by end
- [ ] [Meeting Rooms](05_intervals/meeting_rooms.py) — Easy — sort + adjacent check — *premium*
- [ ] [Meeting Rooms II](05_intervals/meeting_rooms_ii.py) — Medium — min-heap / sweep line — *premium*

### 06 — Linked Lists (6)

- [ ] [Reverse Linked List](06_linked_lists/reverse_linked_list.py) — Easy — three pointers
- [ ] [Linked List Cycle](06_linked_lists/linked_list_cycle.py) — Easy — Floyd's
- [ ] [Merge Two Sorted Lists](06_linked_lists/merge_two_sorted_lists.py) — Easy — dummy head
- [ ] [Merge k Sorted Lists](06_linked_lists/merge_k_sorted_lists.py) — Hard — heap / divide & conquer
- [ ] [Remove Nth Node From End](06_linked_lists/remove_nth_node_from_end.py) — Medium — gap of n
- [ ] [Reorder List](06_linked_lists/reorder_list.py) — Medium — mid + reverse + weave

### 07 — Matrix (4)

- [ ] [Set Matrix Zeroes](07_matrix/set_matrix_zeroes.py) — Medium — mark then write
- [ ] [Spiral Matrix](07_matrix/spiral_matrix.py) — Medium — four boundaries
- [ ] [Rotate Image](07_matrix/rotate_image.py) — Medium — transpose + reverse
- [ ] [Word Search](07_matrix/word_search.py) — Medium — DFS + backtracking

### 08 — Heap (3)

- [ ] [Top K Frequent Elements](08_heap/top_k_frequent_elements.py) — Medium — heap / bucket sort
- [ ] [Find Median from Data Stream](08_heap/find_median_from_data_stream.py) — Hard — two heaps
- [ ] Merge k Sorted Lists — Hard — lives in [06_linked_lists](06_linked_lists/merge_k_sorted_lists.py)

### 09 — Strings (10)

- [ ] [Longest Substring Without Repeating Characters](09_strings/longest_substring_without_repeating.py) — Medium — sliding window
- [ ] [Longest Repeating Character Replacement](09_strings/longest_repeating_character_replacement.py) — Medium — sliding window
- [ ] [Minimum Window Substring](09_strings/minimum_window_substring.py) — Hard — sliding window
- [ ] [Valid Anagram](09_strings/valid_anagram.py) — Easy — counts
- [ ] [Group Anagrams](09_strings/group_anagrams.py) — Medium — canonical key
- [ ] [Valid Parentheses](09_strings/valid_parentheses.py) — Easy — stack
- [ ] [Valid Palindrome](09_strings/valid_palindrome.py) — Easy — two pointers
- [ ] [Longest Palindromic Substring](09_strings/longest_palindromic_substring.py) — Medium — expand around center
- [ ] [Palindromic Substrings](09_strings/palindromic_substrings.py) — Medium — expand around center
- [ ] [Encode and Decode Strings](09_strings/encode_and_decode_strings.py) — Medium — length prefixing — *premium*

### 10 — Trees & Tries (14)

- [ ] [Maximum Depth of Binary Tree](10_trees_and_tries/maximum_depth_of_binary_tree.py) — Easy — recursion
- [ ] [Same Tree](10_trees_and_tries/same_tree.py) — Easy — lockstep recursion
- [ ] [Invert Binary Tree](10_trees_and_tries/invert_binary_tree.py) — Easy — swap children
- [ ] [Binary Tree Maximum Path Sum](10_trees_and_tries/binary_tree_maximum_path_sum.py) — Hard — return vs record
- [ ] [Binary Tree Level Order Traversal](10_trees_and_tries/binary_tree_level_order_traversal.py) — Medium — BFS by level
- [ ] [Serialize and Deserialize Binary Tree](10_trees_and_tries/serialize_and_deserialize_binary_tree.py) — Hard — preorder + null markers
- [ ] [Subtree of Another Tree](10_trees_and_tries/subtree_of_another_tree.py) — Easy — reuse Same Tree
- [ ] [Construct Binary Tree from Preorder and Inorder](10_trees_and_tries/construct_binary_tree_preorder_inorder.py) — Medium — split on root
- [ ] [Validate Binary Search Tree](10_trees_and_tries/validate_binary_search_tree.py) — Medium — carry (low, high)
- [ ] [Kth Smallest Element in a BST](10_trees_and_tries/kth_smallest_element_in_a_bst.py) — Medium — inorder, stop at k
- [ ] [Lowest Common Ancestor of a BST](10_trees_and_tries/lowest_common_ancestor_of_bst.py) — Medium — walk down the split
- [ ] [Implement Trie](10_trees_and_tries/implement_trie.py) — Medium — trie
- [ ] [Design Add and Search Words](10_trees_and_tries/design_add_and_search_words.py) — Medium — trie + wildcard DFS
- [ ] [Word Search II](10_trees_and_tries/word_search_ii.py) — Hard — trie + DFS pruning

## Notes

**Premium problems** (marked above) aren't submittable on free LeetCode. The
stubs and tests here work exactly the same — practise them locally.

**Merge k Sorted Lists** is listed under both Linked List and Heap in the
canonical Blind 75, which is why 76 checkboxes cover 75 distinct files.

**The tests are the spec.** If one looks wrong, check the problem statement
before assuming the test is — every expected value here was verified against a
working solution.
