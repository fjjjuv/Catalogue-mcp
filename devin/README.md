# Devin

## Via CLI

```bash
devin mcp add trello https://mcp.trello.com/v1
devin mcp login trello --scopes "offline_access,read:me,read:account,read:board:trello,write:board:trello,read:organization:trello,write:organization:trello,read:member:trello,read:member.inbox:trello,write:member.inbox:trello,read:member.planner:trello,write:member.planner:trello"
```

Note : le login **sans** `--scopes` provoque une erreur Atlassian
("no supported Atlassian permissions") — les scopes sont obligatoires.

## Via fichier de config

Copier `mcp_config.json` dans :
- User : `%APPDATA%\devin\mcp_config.json` (Windows) / `~/.config/devin/mcp_config.json`
- Projet : `.devin/mcp_config.json`

Puis lancer `devin mcp login trello` (avec les scopes ci-dessus).
