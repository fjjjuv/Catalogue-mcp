# DeepWiki

Documentation IA des dépôts GitHub (structure wiki, Q&A sur un codebase).

| | |
|---|---|
| **Type** | remote |
| **Auth** | aucune |
| **Clé de config** | `deepwiki` |

Outils : read_wiki_structure, read_wiki_contents, ask_wiki_question.

## Fichiers de config par plateforme

| Fichier | Plateforme | Emplacement |
|---|---|---|
| `devin.json` | Devin | fusionner dans `%APPDATA%\devin\mcp_config.json` sous `mcpServers` |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (clé `servers`) |
| `codex.toml` | Codex | `~/.codex/config.toml` |
