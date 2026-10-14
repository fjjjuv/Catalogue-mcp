# GitHub MCP Server (officiel)

**[🇬🇧 English](README.md)**
📄 **Guide complet, exemples & note :** [https://fjjjuv.github.io/Catalogue-mcp/serveurs/github.html](https://fjjjuv.github.io/Catalogue-mcp/serveurs/github.html)


Accès à l'API GitHub : repos, fichiers, issues, PR, releases, commits, recherche de code.

| | |
|---|---|
| **Type** | remote |
| **Auth** | OAuth / token GitHub |
| **Clé de config** | `github` |

Read-only + Write selon les scopes accordés.

## Fichiers de config par plateforme

| Fichier | Plateforme | Emplacement |
|---|---|---|
| `devin.json` | Devin | fusionner dans `%APPDATA%\devin\mcp_config.json` sous `mcpServers` |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (clé `servers`) |
| `codex.toml` | Codex | `~/.codex/config.toml` |
