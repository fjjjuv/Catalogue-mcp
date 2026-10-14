# Asana

**[🇬🇧 English](README.md)**
📄 **Guide complet, exemples & note :** [https://fjjjuv.github.io/Catalogue-mcp/serveurs/asana.html](https://fjjjuv.github.io/Catalogue-mcp/serveurs/asana.html)


Serveur MCP officiel d'Asana.

| | |
|---|---|
| Endpoint | `https://mcp.asana.com/v2/mcp` |
| Auth | OAuth 2.0 |
| Note | Devin exige un client OAuth pré-enregistré (client ID + secret) |

## Fichiers par plateforme

| Fichier | Plateforme | Destination |
|---|---|---|
| `devin.json` | Devin | `mcpServers` de `%APPDATA%\devin\mcp_config.json` — utilise `${env:ASANA_MCP_CLIENT_ID}` / `${env:ASANA_MCP_CLIENT_SECRET}` |
| `cursor.json` | Cursor | `mcpServers` de `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `mcpServers` de `claude_desktop_config.json` |
| `vscode.json` | VS Code | `servers` de `.vscode/mcp.json` |
| `codex.toml` | Codex | `~/.codex/config.toml` |

## Claude Code (CLI)

```bash
claude mcp add --transport http asana https://mcp.asana.com/v2/mcp
# puis /mcp → asana → Authenticate
```

## Devin — OAuth

```bash
devin mcp login asana
```

Nécessite les variables d'environnement `ASANA_MCP_CLIENT_ID` et
`ASANA_MCP_CLIENT_SECRET` (client OAuth enregistré auprès d'Asana).
