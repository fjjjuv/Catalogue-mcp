# Devin

Copier le contenu de `<nom>.json` sous la clé `mcpServers` de :
- `%APPDATA%\devin\mcp_config.json` (Windows, global)
- `.devin/mcp_config.json` (projet)

Ou via CLI :

```bash
devin mcp add trello https://mcp.trello.com/v1
```

## OAuth — Trello

```bash
devin mcp login trello --scopes "offline_access,read:me,read:account,read:board:trello,write:board:trello,read:organization:trello,write:organization:trello,read:member:trello,read:member.inbox:trello,write:member.inbox:trello,read:member.planner:trello,write:member.planner:trello"
```

Note : le login **sans** `--scopes` provoque une erreur Atlassian
("no supported Atlassian permissions") — les scopes sont obligatoires.

## OAuth — Asana

Nécessite un client OAuth pré-enregistré : renseigner
`ASANA_MCP_CLIENT_ID` / `ASANA_MCP_CLIENT_SECRET` en variables
d'environnement, puis `devin mcp login asana`.
