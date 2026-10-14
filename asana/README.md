# Asana

**[🇫🇷 Français](README_FR.md)**
📄 **Full guide, examples & rating:** [https://fjjjuv.github.io/Catalogue-mcp/serveurs/asana.html](https://fjjjuv.github.io/Catalogue-mcp/serveurs/asana.html)


Asana's official MCP server.

| | |
|---|---|
| Endpoint | `https://mcp.asana.com/v2/mcp` |
| Auth | OAuth 2.0 |
| Note | Devin requires a pre-registered OAuth client (client ID + secret) |

## Files per platform

| File | Platform | Destination |
|---|---|---|
| `devin.json` | Devin | `mcpServers` in `%APPDATA%\devin\mcp_config.json` — uses `${env:ASANA_MCP_CLIENT_ID}` / `${env:ASANA_MCP_CLIENT_SECRET}` |
| `cursor.json` | Cursor | `mcpServers` in `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `mcpServers` in `claude_desktop_config.json` |
| `vscode.json` | VS Code | `servers` in `.vscode/mcp.json` |
| `codex.toml` | Codex | `~/.codex/config.toml` |

## Claude Code (CLI)

```bash
claude mcp add --transport http asana https://mcp.asana.com/v2/mcp
# then /mcp → asana → Authenticate
```

## Devin — OAuth

```bash
devin mcp login asana
```

Requires the `ASANA_MCP_CLIENT_ID` and `ASANA_MCP_CLIENT_SECRET`
environment variables (OAuth client registered with Asana).
