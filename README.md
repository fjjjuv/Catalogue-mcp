# MCP Configs

Collection de configurations prêtes à l'emploi pour connecter des
**serveurs MCP** aux principaux clients : Devin, Cursor, Claude Desktop,
VS Code, Codex, Claude Code.

## Organisation

Un dossier par serveur MCP à la racine. Chaque dossier contient tout ce
qui appartient au serveur : sa doc (`README.md`) et un fichier de config
par plateforme, nommé d'après la plateforme.

```
<serveur>/
  README.md            # infos du serveur + instructions par client
  devin.json           # → mcp_config.json de Devin
  cursor.json          # → .cursor/mcp.json
  claude-desktop.json  # → claude_desktop_config.json
  vscode.json          # → .vscode/mcp.json (clé "servers")
  codex.toml           # → ~/.codex/config.toml
```

## Serveurs

| Dossier | Serveur | Type | Auth |
|---|---|---|---|
| [`trello/`](trello/) | Trello (officiel Atlassian) | remote `https://mcp.trello.com/v1` | OAuth 2.0 |
| [`asana/`](asana/) | Asana | remote `https://mcp.asana.com/v2/mcp` | OAuth 2.0 |
| [`github/`](github/) | GitHub MCP Server (officiel) | remote `https://api.githubcopilot.com/mcp` | OAuth / token |
| [`exa-code/`](exa-code/) | Exa Code | remote `https://mcp.exa.ai/mcp` | compte Exa |
| [`deepwiki/`](deepwiki/) | DeepWiki | remote `https://mcp.deepwiki.com/mcp` | aucune |
| [`cloudflare-docs/`](cloudflare-docs/) | Cloudflare Docs | remote `https://docs.mcp.cloudflare.com/mcp` | aucune |
| [`playwright/`](playwright/) | Playwright | local stdio (`npx @playwright/mcp`) | aucune |
| [`puppeteer/`](puppeteer/) | Puppeteer | local stdio (`npx @modelcontextprotocol/server-puppeteer`) | aucune |
| [`computer-use/`](computer-use/) | Computer Use | local stdio (`npx computer-use-mcp`) | aucune |
| [`context7/`](context7/) | Context7 (Upstash) | local stdio (`npx @upstash/context7-mcp`) | aucune |
| [`memory/`](memory/) | Memory (officiel MCP) | local stdio (`npx @modelcontextprotocol/server-memory`) | aucune |
| [`semgrep/`](semgrep/) | Semgrep | local stdio (`semgrep mcp`) | aucune |

## Formats par plateforme

| Plateforme | Clé racine | Format |
|---|---|---|
| Devin | `mcpServers` | JSON |
| Cursor | `mcpServers` | JSON |
| Claude Desktop | `mcpServers` | JSON |
| VS Code | `servers` + `type` | JSON |
| Codex | `mcp_servers.*` | TOML |
| Claude Code | via `claude mcp add` | CLI |

## Secrets

Ne jamais commiter de secrets. Utiliser `${env:VAR}` quand le client le
supporte (Devin), sinon des variables d'environnement.

## Licence

[MIT](LICENSE)
