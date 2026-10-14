# Playwright

**[🇬🇧 English](README.md)**

Serveur MCP Playwright (Microsoft) — automatisation navigateur pour les
agents : naviguer, cliquer, remplir des formulaires, capturer des
screenshots et le DOM.

| | |
|---|---|
| Package | `@playwright/mcp` (npm) |
| Type | Serveur **local** (stdio) — différent des serveurs remote OAuth |
| Prérequis | Node.js + npx |

## Fichiers par plateforme

| Fichier | Plateforme | Destination |
|---|---|---|
| `devin.json` | Devin | `mcpServers` de `%APPDATA%\devin\mcp_config.json` — utilise `cmd.exe /c` sous Windows |
| `cursor.json` | Cursor | `mcpServers` de `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `mcpServers` de `claude_desktop_config.json` |
| `vscode.json` | VS Code | `servers` de `.vscode/mcp.json` (`"type": "stdio"`) |
| `codex.toml` | Codex | `~/.codex/config.toml` |

## Claude Code (CLI)

```bash
claude mcp add playwright -- npx -y @playwright/mcp@latest
```

## Codex — CLI

```bash
codex mcp add playwright -- npx -y @playwright/mcp@latest
```

## Devin — CLI

```bash
devin mcp add playwright -- cmd.exe /c npx -y @playwright/mcp@latest
```

Pas d'OAuth : le serveur se lance localement, les outils
`browser_*` apparaissent directement.
