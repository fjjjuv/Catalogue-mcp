# XERJ — local search engine + agent memory, exposed as MCP

**[🇫🇷 Français](README_FR.md)**
📄 **Full guide, examples & rating:** [https://fjjjuv.github.io/Catalogue-mcp/serveurs/xerj.html](https://fjjjuv.github.io/Catalogue-mcp/serveurs/xerj.html)

## What is it?

XERJ is a **search engine you run on your own machine** (one Rust binary,
no JVM, no dependencies). You point it at a folder, it indexes the files,
and your AI agent can then **search your real data** instead of guessing —
code, docs, logs, PDFs.

It speaks the Elasticsearch API, and it ships an **MCP server inside the
same binary**, so agents can use it directly.

## Why it's useful

| Without XERJ | With XERJ |
|---|---|
| The agent `grep`s whole files → burns tokens | One query returns the exact `file:line` passage |
| The agent forgets everything between sessions | `xerj_memory_*` = durable, searchable memory |
| Search APIs cost money per call | Everything runs **locally and free** |

## Requirements

⚠️ **Important:** the MCP server needs a running XERJ **node** — it does
not start one itself. Two processes:

```bash
# 1. Install the binary
curl -fsSL https://xerj.org/get | sh        # Linux / macOS / Git Bash
powershell -ExecutionPolicy Bypass -c "irm https://xerj.org/get.ps1 | iex"  # Windows

# 2. Start the node (leave it running)
xerj --insecure --data-dir ~/.xerj/data
# → listens on http://localhost:9200, console: http://localhost:9200/_xerj-console/
```

The MCP configs in this folder then run `xerj mcp`, which just proxies to
that node.

## Quick test

```bash
# Index a folder (~seconds for a small project)
xerj autoindex ./my-project

# Or check from the agent: xerj_map lists the indexed fields
```

## What the agent gets (13 tools)

- **`xerj_search`** — full-text/code search, definition-first ranking
- **`xerj_semantic_search` / `xerj_vector_search` / `xerj_hybrid_search`** — meaning-based retrieval
- **`xerj_memory_store` / `xerj_memory_recall`** — long-term agent memory (works with zero indexed folders)
- **`xerj_map`** — "what's indexed and what fields exist"
- **`xerj_brain_*`** — link/relationship index
- **`xerj_plan`**, **`xerj_code_search`** — query planner, reference-code search

## Config files per platform

| File | Platform | Location |
|---|---|---|
| `devin.json` | Devin | merge into `%APPDATA%\devin\mcp_config.json` under `mcpServers` |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (`servers` key) |
| `codex.toml` | Codex | `~/.codex/config.toml` |

## Gotchas

- **GUI apps may not see `xerj` in PATH** → use the absolute path in
  `command`, e.g. `C:\Users\<you>\.local\bin\xerj.exe` on Windows.
- **Not indexed = not found.** XERJ only searches what `autoindex` covered;
  the agent falls back to classic tools for the rest.
- **`--insecure` is for localhost only.** A real deployment uses the API
  key in `<data-dir>/admin.key` via `XERJ_AUTH`.

| | |
|---|---|
| **Type** | local stdio |
| **Auth** | none on a local node (`--insecure`), else `XERJ_AUTH: ApiKey <key>` |
| **Config key** | `xerj` |
| **Tested version** | xerj v1.0.0-rc.95 |
