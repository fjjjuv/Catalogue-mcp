# Semgrep

Analyse statique de code : détection de vulnérabilités et patterns.

| | |
|---|---|
| **Type** | local stdio |
| **Auth** | aucune (login optionnel) |
| **Clé de config** | `semgrep` |

Nécessite `semgrep` installé et dans le PATH (ou chemin absolu vers semgrep.exe).

## Fichiers de config par plateforme

| Fichier | Plateforme | Emplacement |
|---|---|---|
| `devin.json` | Devin | fusionner dans `%APPDATA%\devin\mcp_config.json` sous `mcpServers` |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (clé `servers`) |
| `codex.toml` | Codex | `~/.codex/config.toml` |
