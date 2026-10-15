# XERJ — search engine + agent memory as MCP

**[🇫🇷 Français](README_FR.md)**
📄 **Full guide, examples & rating:** [https://fjjjuv.github.io/Catalogue-mcp/serveurs/xerj.html](https://fjjjuv.github.io/Catalogue-mcp/serveurs/xerj.html)

> XERJ is a search engine written in Rust (Elasticsearch-compatible wire
> protocol) with an MCP server **built into the same binary**: `xerj mcp`.
> It indexes code, docs, logs and PDFs for agent search, RAG and long-term
> memory — and also gives the agent a durable `/_memory/{ns}` store.

| | |
|---|---|
| **Type** | local stdio |
| **Auth** | none on a local node (`--insecure`), else `XERJ_AUTH: ApiKey <key>` |
| **Config key** | `xerj` |
| **Tested version** | xerj v1.0.0-rc.95 |
| **Requires** | a running node: `xerj --insecure --data-dir ~/.xerj/data` |

## How it works

Two parts, one binary:

```
# 1. The engine (node) — speaks ES 8.x on :9200
xerj --insecure --data-dir ~/.xerj/data

# 2. The MCP server — proxies to that node over stdio
xerj mcp
```

The MCP server does **not** start the node for you. If nothing answers on
`XERJ_URL`, the tools return a connection error.

13 tools exposed: `xerj_search` (BM25 / DSL, definition-first on code),
`xerj_semantic_search`, `xerj_vector_search`, `xerj_hybrid_search`,
`xerj_memory_store`, `xerj_memory_recall`, `xerj_brain_*` (link index),
`xerj_plan`, `xerj_map`, `xerj_code_search`.

## Install

```bash
curl -fsSL https://xerj.org/get | sh        # Linux / macOS / Git Bash
# Windows PowerShell:
powershell -ExecutionPolicy Bypass -c "irm https://xerj.org/get.ps1 | iex"
```

Binary lands in `~/.local/bin/xerj` (Windows: `%USERPROFILE%\.local\bin\xerj.exe`).

## Index a folder

```bash
xerj autoindex <folder>            # writes ax-* indices + autoindex-catalog
xerj autoindex <folder> --dry-run  # estimate first, indexes nothing
```

Then `xerj_map` (MCP) returns each index's field map, and `xerj_search`
searches `ax-*` by default — no index name needed.

## Agent memory without indexing

```json
xerj_memory_store {"namespace": "proj", "text": "prod runs PostgreSQL"}
xerj_memory_recall {"namespace": "proj", "query": "database"}
```

Works even with zero indexed folders — memory lives in its own indices.

## Config files per platform

| File | Platform | Location |
|---|---|---|
| `devin.json` | Devin | merge into `%APPDATA%\devin\mcp_config.json` under `mcpServers` |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (`servers` key) |
| `codex.toml` | Codex | `~/.codex/config.toml` |

## Gotchas

- **GUI PATH**: desktop apps may not see `xerj` in PATH → use the absolute
  binary path in `command` (e.g. `C:\Users\<you>\.local\bin\xerj.exe`).
- **Not indexed = not searchable**: xerj only searches what `autoindex` ran on.
  For anything else, the agent falls back to its classic search tools.
- **`--insecure`** means no API key — fine for localhost only. A real
  deployment uses `<data-dir>/admin.key` via `XERJ_AUTH`.
