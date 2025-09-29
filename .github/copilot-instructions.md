<!-- .github/copilot-instructions.md - guidance for AI coding agents working on AlgorithmTasks -->

# AlgorithmTasks — Copilot instructions

Short, actionable guidance for automated coding agents collaborating on this repository.

- This repo is a curated collection of small algorithm problem solutions organized by topic. Key top-level folders (from `README.md`): `arrays/`, `strings/`, `sorting/`, `searching/`, `dynamic-programming/`, `graphs/`, `data-structures/`.
- Many problem files are single Python scripts that include a short header comment with sections: Problem, Complexity, Code. Example: `arrays/easy/find_maximum_number.py` contains a `class Solution:` skeleton and commented problem statement.

What to do first

- Read `README.md` and the target file(s) before proposing edits. Files are small and self-contained; open the entire file to discover the problem description and expected I/O.
- If asked to implement a solution, prefer small, focused edits that preserve the file header comments and complexity notes.

Code patterns and conventions (observable)

- File naming: snake_case.py per problem, grouped under topic/difficulty directories (e.g. `arrays/easy/`).
- Content layout: comment block describing the problem, then an implementation. Some files expose a `class Solution:` (common) or top-level functions. Keep public symbols minimal and explicit.
- No package manager or requirements file detected. Assume pure-Python solutions with no external dependencies unless a file explicitly imports third-party packages.

Local developer workflows (discoverable)

- Run a single problem file: `python3 path/to/file.py` (most files are runnable scripts). When adding a new runnable file, include a small `if __name__ == "__main__":` example or tests.
- Quick syntax check: `python3 -m py_compile path/to/file.py`.
- There are no automated tests or CI config detected in the repository root — do not assume a test runner. If you add tests, include a README note explaining how to run them.

How the AI should behave in this repo

- Respect the user's local prompt preference stored outside the repo: the developer has a workspace prompt saying "I want to create a solution on my own so do not give me suggestions." Before offering full implementations, ask whether the user wants hints, a partial implementation, or a complete solution.
- When implementing: prefer minimal, readable solutions that match the existing style (comment header, complexity notes). Use explicit variable names and include a one-line complexity comment.
- Avoid making large cross-file refactors. These problems are self-contained; change only the target problem file unless the user requests broader restructuring.
- When editing a file, run a quick syntax check (`python3 -m py_compile`) and mention the result in your response.

Examples from the codebase

- `arrays/easy/find_maximum_number.py` — contains a commented problem and `class Solution:` skeleton. Use this as the canonical example for: preserving headers, adding an idiomatic implementation method (e.g., `def find_max(self, nums):`), and adding a `__main__` demo when appropriate.

Safe defaults and limits

- Do not invent new top-level modules or dependency files without explicit user approval.
- If a requested change touches >3 files, summarize the plan first and ask for confirmation.

If anything here is unclear or you want the agent to follow a different collaboration style (for example, to be more proactive or to always produce runnable tests), tell me which mode to adopt and I'll update this file.
