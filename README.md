# MCP Configs — configurations multi-plateformes

Collection de configurations prêtes à l'emploi pour connecter des
**serveurs MCP** aux principaux clients : Devin, Cursor, Claude Desktop,
VS Code, Codex, Claude Code.

## Organisation

```
<plateforme>/
  README.md              # instructions spécifiques au client
  servers/
    <serveur>.json|toml  # bloc de config à copier
```

| Plateforme | Fichier de config | Format |
|---|---|---|
| [Devin](devin/) | `%APPDATA%\devin\mcp_config.json` ou `.devin/mcp_config.json` | `mcpServers` (JSON) |
| [Cursor](cursor/) | `.cursor/mcp.json` | `mcpServers` (JSON) |
| [Claude Desktop](claude-desktop/) | `claude_desktop_config.json` | `mcpServers` (JSON) |
| [VS Code](vscode/) | `.vscode/mcp.json` | `servers` + `type` (JSON) |
| [Codex](codex/) | `~/.codex/config.toml` | `mcp_servers.*` (TOML) |
| [Claude Code](claude-code/) | via `claude mcp add` | CLI |

## Serveurs disponibles

| Serveur | Endpoint | Auth | Notes |
|---|---|---|---|
| **Trello** (officiel Atlassian) | `https://mcp.trello.com/v1` | OAuth 2.0 | Scopes explicites requis par certains clients (voir [devin/README.md](devin/README.md)) |
| **Asana** | `https://mcp.asana.com/v2/mcp` | OAuth 2.0 | Client ID/secret pré-enregistré requis dans Devin |

## Utilisation

1. Choisir le dossier de votre plateforme
2. Copier le fichier `servers/<serveur>.json` dans la config du client
   (fusionner sous la clé `mcpServers` / `servers` selon le format)
3. Lancer la connexion → flux OAuth dans le navigateur
4. Les outils `<serveur>*` deviennent disponibles

## Secrets

Ne jamais commiter de secrets. Utiliser `${env:VAR}` quand le client le
supporte (Devin), ou une variable d'environnement.

## Licence

[MIT](LICENSE)
