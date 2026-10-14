# Trello (serveur MCP officiel)

**[🇬🇧 English](README.md)**
📄 **Guide complet, exemples & note :** [https://fjjjuv.github.io/Catalogue-mcp/serveurs/trello.html](https://fjjjuv.github.io/Catalogue-mcp/serveurs/trello.html)


Serveur MCP officiel hébergé par Atlassian.

| | |
|---|---|
| Endpoint | `https://mcp.trello.com/v1` |
| Repo | https://github.com/atlassian/trello-mcp-server |
| Auth | OAuth 2.0, accès scopé par workspace |
| Tarif | Gratuit, tous plans Trello |
| Fonctionnalités | Boards, lists, cards, checklists, commentaires, labels, custom fields, inbox, planner, recherche |

## Fichiers par plateforme

| Fichier | Plateforme | Destination |
|---|---|---|
| `devin.json` | Devin | `mcpServers` de `%APPDATA%\devin\mcp_config.json` ou `.devin/mcp_config.json` |
| `cursor.json` | Cursor | `mcpServers` de `.cursor/mcp.json` ou `~/.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `mcpServers` de `claude_desktop_config.json` |
| `vscode.json` | VS Code | `servers` de `.vscode/mcp.json` (clé `"servers"`, `"type": "http"`) |
| `codex.toml` | Codex | `~/.codex/config.toml` |

## Claude Code (CLI uniquement)

```bash
claude mcp add --transport http trello https://mcp.trello.com/v1
# puis /mcp → trello → Authenticate
```

## Devin — OAuth (scopes obligatoires)

Le login sans scopes échoue ("no supported Atlassian permissions").
Utiliser :

```bash
devin mcp add trello https://mcp.trello.com/v1
devin mcp login trello --scopes "offline_access,read:me,read:account,read:board:trello,write:board:trello,read:organization:trello,write:organization:trello,read:member:trello,read:member.inbox:trello,write:member.inbox:trello,read:member.planner:trello,write:member.planner:trello"
```

## Codex — CLI

```bash
codex mcp add trello --url https://mcp.trello.com/v1
codex mcp login trello
```
