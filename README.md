# 🧥 CORSET: Unified Agent & Token Optimizer

**CORSET** (Code Optimization & Reduced Symbolic Execution of Tokens) is an all-in-one skill and ruleset for AI coding agents (Claude.ai, Cursor, Antigravity, Claude Code, Codex). 

It combines the token-slashing power of **Caveman** (terse communications) and **Ponytail** (minimal code generation via the elimination ladder) into one unified instruction layer.

---

## 🚀 Highlights
- **Talk Less (Caveman Protocol):** Cuts conversational fluff, introductions, and postambles (~60% prose output token savings).
- **Write Less (Ponytail Ladder):** Forces agents to delete dead code, reuse utilities, and rely on stdlib/native platform features.
- **Zero Loss:** Retains 100% of security checks, error boundaries, UI conventions, and business logic.

---

## 📥 Setup Instructions

### For Claude.ai (Web App)
1. Open **Projects** in Claude.ai.
2. Create a Project named `CORSET Coding` and paste the contents of `AGENTS.md` into **Project Instructions**.
3. *Alternative:* Paste the contents of `AGENTS.md` into **Settings -> Instructions for Claude** for account-wide enforcement.

### For Cursor / Windsurf / Codex / VSCode
Copy `AGENTS.md` directly into the root directory of your project repository.

### For Antigravity
Copy `.agents/rules/optimizer.md` into your repository.

---

## 📊 Benchmarking

Measure token and code line reductions locally using [Promptfoo](https://promptfoo.dev):

```bash
npm install -g promptfoo
npx promptfoo eval -c benchmarks/eval_config.yaml -o benchmarks/results.json
python benchmarks/log_parser.py