# Context7 (Upstash)

Documentation à jour des bibliothèques + exemples de code injectés dans le contexte.

| | |
|---|---|
| **Type** | local stdio |
| **Auth** | aucune (clé API optionnelle) |
| **Clé de config** | `context7` |

Compatible `use context7` dans les prompts.

## Fichiers de config par plateforme

| Fichier | Plateforme | Emplacement |
|---|---|---|
| `devin.json` | Devin | fusionner dans `%APPDATA%\devin\mcp_config.json` sous `mcpServers` |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (clé `servers`) |
| `codex.toml` | Codex | `~/.codex/config.toml` |
