# Catalogue-mcp

**[🇫🇷 Version française](README_FR.md)** · 🌐 [Catalogue website](https://fjjjuv.github.io/Catalogue-mcp/)

Ready-to-use configurations to connect **MCP servers** to the main
clients: Devin, Cursor, Claude Desktop, VS Code, Codex, Claude Code.

## Layout

One folder per MCP server at the root. Each folder contains everything
belonging to that server: its docs (`README.md` in English,
`README_FR.md` in French) and one config file per platform, named after
the platform.

```
<server>/
  README.md            # server info + per-client instructions (EN)
  README_FR.md         # same doc in French
  devin.json           # → Devin's mcp_config.json
  cursor.json          # → .cursor/mcp.json
  claude-desktop.json  # → claude_desktop_config.json
  vscode.json          # → .vscode/mcp.json ("servers" key)
  codex.toml           # → ~/.codex/config.toml
```

## Servers

| Folder | Server | Type | Auth |
|---|---|---|---|
| [`trello/`](trello/) | Trello (official Atlassian) | remote `https://mcp.trello.com/v1` | OAuth 2.0 |
| [`asana/`](asana/) | Asana | remote `https://mcp.asana.com/v2/mcp` | OAuth 2.0 |
| [`github/`](github/) | GitHub MCP Server (official) | remote `https://api.githubcopilot.com/mcp` | OAuth / token |
| [`exa-code/`](exa-code/) | Exa Code | remote `https://mcp.exa.ai/mcp` | Exa account |
| [`deepwiki/`](deepwiki/) | DeepWiki | remote `https://mcp.deepwiki.com/mcp` | none |
| [`cloudflare-docs/`](cloudflare-docs/) | Cloudflare Docs | remote `https://docs.mcp.cloudflare.com/mcp` | none |
| [`playwright/`](playwright/) | Playwright | local stdio (`npx @playwright/mcp`) | none |
| [`puppeteer/`](puppeteer/) | Puppeteer | local stdio (`npx @modelcontextprotocol/server-puppeteer`) | none |
| [`computer-use/`](computer-use/) | Computer Use | local stdio (`npx computer-use-mcp`) | none |
| [`context7/`](context7/) | Context7 (Upstash) | local stdio (`npx @upstash/context7-mcp`) | none |
| [`memory/`](memory/) | Memory (official MCP) | local stdio (`npx @modelcontextprotocol/server-memory`) | none |
| [`semgrep/`](semgrep/) | Semgrep | local stdio (`semgrep mcp`) | none |

## Config formats per platform

| Platform | Root key | Format |
|---|---|---|
| Devin | `mcpServers` | JSON |
| Cursor | `mcpServers` | JSON |
| Claude Desktop | `mcpServers` | JSON |
| VS Code | `servers` + `type` | JSON |
| Codex | `mcp_servers.*` | TOML |
| Claude Code | via `claude mcp add` | CLI |

## Secrets

Never commit secrets. Use `${env:VAR}` when the client supports it
(Devin), otherwise environment variables.

## License

[MIT](LICENSE)
