# MCP Trello — Configurations par plateforme

Configurations prêtes à l'emploi pour connecter le **serveur MCP Trello officiel**
(hébergé par Atlassian) aux principaux clients MCP.

## À propos du serveur

| | |
|---|---|
| Endpoint | `https://mcp.trello.com/v1` |
| Repo officiel | https://github.com/atlassian/trello-mcp-server |
| Authentification | OAuth 2.0, accès scopé par workspace |
| Tarif | Gratuit, tous plans Trello |
| Fonctionnalités | Boards, lists, cards, checklists, commentaires, labels, custom fields, inbox, planner, recherche |

## Plateformes supportées

| Plateforme | Dossier | Méthode |
|---|---|---|
| Devin | [`devin/`](devin/) | `devin mcp add` + `devin mcp login --scopes` |
| Cursor | [`cursor/`](cursor/) | `.cursor/mcp.json` |
| Claude Desktop | [`claude-desktop/`](claude-desktop/) | `claude_desktop_config.json` |
| VS Code | [`vscode/`](vscode/) | `.vscode/mcp.json` (clé `"servers"`) |
| Codex | [`codex/`](codex/) | `codex mcp add` / `config.toml` |
| Claude Code | [`claude-code/`](claude-code/) | `claude mcp add --transport http` |

## Scopes OAuth Trello

Certains clients (ex. Devin) exigent des scopes explicites — sans eux,
Atlassian renvoie *"This application has not requested any supported
Atlassian permissions"*. Liste complète supportée par le serveur :

```
offline_access read:me read:account
read:board:trello write:board:trello
read:organization:trello write:organization:trello
read:member:trello
read:member.inbox:trello write:member.inbox:trello
read:member.planner:trello write:member.planner:trello
```

## Comment ça marche

1. Copier la config du dossier correspondant à votre client
2. Lancer la connexion → le navigateur s'ouvre sur l'écran de
   consentement Atlassian/Trello
3. Choisir le workspace à autoriser, valider les permissions
4. Vos outils `trello*` sont disponibles dans le client

## Licence

[MIT](LICENSE)
