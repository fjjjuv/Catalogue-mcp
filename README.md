<p align="center">
  <img src="https://fjjjuv.github.io/Catalogue-mcp/logo.svg" alt="Catalogue-mcp" width="96" height="96">
</p>

<h1 align="center">Catalogue-mcp</h1>

<p align="center">
  <strong>12 MCP servers. 6 platforms. One plug-and-play config each.</strong><br>
  Give your AI agent real superpowers — boards, repos, browsers, memory, security scans.
</p>

<p align="center">
  <a href="https://fjjjuv.github.io/Catalogue-mcp/">🌐 Website</a> •
  <a href="README_FR.md">🇫🇷 Français</a> •
  <a href="LICENSE">📄 MIT License</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/MCP_servers-12-6366f1" alt="12 servers">
  <img src="https://img.shields.io/badge/platforms-6-38bdf8" alt="6 platforms">
  <img src="https://img.shields.io/badge/cost-100%25_free-34d399" alt="free">
  <img src="https://img.shields.io/badge/license-MIT-f59e0b" alt="MIT">
</p>

---

## 🚀 Why this repo

One MCP server = one new skill for your agent. This catalog gives you
the **exact config file** to drop into Devin, Cursor, Claude Desktop,
VS Code or Codex — no docs digging, no format guessing.

- ⚡ **Zero copy-paste** — the agent reads/writes directly in your tools (Trello, GitHub…)
- 📚 **Ground truth** — Context7 & DeepWiki inject real, current docs
- 🔒 **Continuous security** — Semgrep scans while the agent writes code
- 🖥️ **Real actions** — Playwright browses for real, Computer Use clicks your desktop
- 🧠 **Memory** — your preferences survive across sessions

## 📦 The servers

| Folder | Server | Superpower | Type | Auth |
|---|---|---|---|---|
| [`trello/`](trello/) | Trello (official Atlassian) | Manage boards, cards & checklists | remote | OAuth 2.0 |
| [`github/`](github/) | GitHub MCP Server | Repos, issues, PRs, code search | remote | OAuth / token |
| [`asana/`](asana/) | Asana | Tasks & projects | remote | OAuth 2.0 |
| [`deepwiki/`](deepwiki/) | DeepWiki | Q&A on any GitHub codebase | remote | none |
| [`exa-code/`](exa-code/) | Exa Code | Semantic code search | remote | Exa account |
| [`cloudflare-docs/`](cloudflare-docs/) | Cloudflare Docs | Official Cloudflare docs | remote | none |
| [`playwright/`](playwright/) | Playwright | Real browser automation | local stdio | none |
| [`puppeteer/`](puppeteer/) | Puppeteer | Chrome automation via CDP | local stdio | none |
| [`computer-use/`](computer-use/) | Computer Use | Mouse & keyboard on your PC | local stdio | none |
| [`context7/`](context7/) | Context7 (Upstash) | Fresh library docs in context | local stdio | none |
| [`memory/`](memory/) | Memory | Knowledge graph across sessions | local stdio | none |
| [`semgrep/`](semgrep/) | Semgrep | Security scans while coding | local stdio | none |

📊 Full comparison & ratings → **[fjjjuv.github.io/Catalogue-mcp](https://fjjjuv.github.io/Catalogue-mcp/)**

## 🛠️ Layout

One folder per server, one config file per platform — the name says
where it goes:

```
<server>/
  README.md            # server doc (EN)
  README_FR.md         # doc (FR)
  devin.json           # → %APPDATA%\devin\mcp_config.json
  cursor.json          # → .cursor/mcp.json
  claude-desktop.json  # → claude_desktop_config.json
  vscode.json          # → .vscode/mcp.json ("servers" key)
  codex.toml           # → ~/.codex/config.toml
```

| Platform | Root key | Format |
|---|---|---|
| Devin | `mcpServers` | JSON |
| Cursor | `mcpServers` | JSON |
| Claude Desktop | `mcpServers` | JSON |
| VS Code | `servers` + `type` | JSON |
| Codex | `mcp_servers.*` | TOML |
| Claude Code | via `claude mcp add` | CLI |

## 📄 License

[MIT](LICENSE) — free, open source, do whatever you want with it.
