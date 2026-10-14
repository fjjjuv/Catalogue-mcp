# Trello (official MCP server)

**[🇫🇷 Français](README_FR.md)**
📄 **Full guide, examples & rating:** [https://fjjjuv.github.io/Catalogue-mcp/serveurs/trello.html](https://fjjjuv.github.io/Catalogue-mcp/serveurs/trello.html)


Official MCP server hosted by Atlassian.

| | |
|---|---|
| Endpoint | `https://mcp.trello.com/v1` |
| Repo | https://github.com/atlassian/trello-mcp-server |
| Auth | OAuth 2.0, workspace-scoped access |
| Pricing | Free, all Trello plans |
| Features | Boards, lists, cards, checklists, comments, labels, custom fields, inbox, planner, search |

## Files per platform

| File | Platform | Destination |
|---|---|---|
| `devin.json` | Devin | `mcpServers` in `%APPDATA%\devin\mcp_config.json` or `.devin/mcp_config.json` |
| `cursor.json` | Cursor | `mcpServers` in `.cursor/mcp.json` or `~/.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `mcpServers` in `claude_desktop_config.json` |
| `vscode.json` | VS Code | `servers` in `.vscode/mcp.json` (`"servers"` key, `"type": "http"`) |
| `codex.toml` | Codex | `~/.codex/config.toml` |

## Claude Code (CLI only)

```bash
claude mcp add --transport http trello https://mcp.trello.com/v1
# then /mcp → trello → Authenticate
```

## Devin — OAuth (required scopes)

Login without scopes fails ("no supported Atlassian permissions").
Use:

```bash
devin mcp add trello https://mcp.trello.com/v1
devin mcp login trello --scopes "offline_access,read:me,read:account,read:board:trello,write:board:trello,read:organization:trello,write:organization:trello,read:member:trello,read:member.inbox:trello,write:member.inbox:trello,read:member.planner:trello,write:member.planner:trello"
```

## Codex — CLI

```bash
codex mcp add trello --url https://mcp.trello.com/v1
codex mcp login trello
```
