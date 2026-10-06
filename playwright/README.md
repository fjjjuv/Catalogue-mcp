# Playwright

Serveur MCP officiel de Microsoft pour l'automatisation de navigateur
(navigation, clics, screenshots, tests...). Serveur **stdio local**,
pas d'OAuth nécessaire.

| | |
|---|---|
| Package | `@playwright/mcp` (via npx) |
| Repo | https://github.com/microsoft/playwright-mcp |
| Transport | stdio (commande locale) |
| Auth | Aucune |

## Fichiers par plateforme

| Fichier | Plateforme | Destination |
|---|---|---|
| `devin.json` | Devin | `mcpServers` de `%APPDATA%\devin\mcp_config.json` — wrapper `cmd.exe /c` requis sous Windows |
| `cursor.json` | Cursor | `mcpServers` de `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `mcpServers` de `claude_desktop_config.json` |
| `vscode.json` | VS Code | `servers` de `.vscode/mcp.json` (`"type": "stdio"`) |
| `codex.toml` | Codex | `~/.codex/config.toml` |

## Claude Code (CLI)

```bash
claude mcp add playwright -- npx -y @playwright/mcp@latest
```

## Note Windows

Sous Windows, certains clients exigent le wrapper `cmd.exe /c` devant
`npx` (voir `devin.json`). Sous macOS/Linux, `npx` directement suffit.
