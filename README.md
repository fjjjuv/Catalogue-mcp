# MCP Trello — Configurations par plateforme

Configurations prêtes à l'emploi pour connecter le **serveur MCP Trello officiel**
(hébergé par Atlassian) à différents clients MCP.

## Serveur

- Endpoint : `https://mcp.trello.com/v1`
- Repo officiel : https://github.com/atlassian/trello-mcp-server
- Auth : OAuth 2.0, accès scopé par workspace
- Gratuit : disponible sur tous les plans Trello

## Plateformes

| Plateforme | Dossier | Méthode |
|---|---|---|
| Devin | [`devin/`](devin/) | `devin mcp login trello` |
| Cursor | [`cursor/`](cursor/) | `.cursor/mcp.json` |
| Claude Desktop | [`claude-desktop/`](claude-desktop/) | `claude_desktop_config.json` |
| VS Code | [`vscode/`](vscode/) | `.vscode/mcp.json` |
| Codex | [`codex/`](codex/) | `codex mcp add` |
| Claude Code | [`claude-code/`](claude-code/) | `claude mcp add` |

## Scopes OAuth Trello

Si le client demande des scopes explicites :

```
offline_access read:me read:account read:board:trello write:board:trello
read:organization:trello write:organization:trello read:member:trello
read:member.inbox:trello write:member.inbox:trello
read:member.planner:trello write:member.planner:trello
```
