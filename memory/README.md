# Memory (serveur officiel MCP)

Graphe de connaissances persistant : entités, relations, observations.

| | |
|---|---|
| **Type** | local stdio |
| **Auth** | aucune |
| **Clé de config** | `memory` |

Mémoire long terme entre sessions.

## Fichiers de config par plateforme

| Fichier | Plateforme | Emplacement |
|---|---|---|
| `devin.json` | Devin | fusionner dans `%APPDATA%\devin\mcp_config.json` sous `mcpServers` |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (clé `servers`) |
| `codex.toml` | Codex | `~/.codex/config.toml` |
