# Memory (official MCP server)

**[🇫🇷 Français](README_FR.md)**
📄 **Full guide, examples & rating:** [https://fjjjuv.github.io/Catalogue-mcp/serveurs/memory.html](https://fjjjuv.github.io/Catalogue-mcp/serveurs/memory.html)


Persistent knowledge graph: entities, relations, observations.

| | |
|---|---|
| **Type** | local stdio |
| **Auth** | none |
| **Config key** | `memory` |

Long-term memory across sessions.

## Config files per platform

| File | Platform | Location |
|---|---|---|
| `devin.json` | Devin | merge into `%APPDATA%\devin\mcp_config.json` under `mcpServers` |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (`servers` key) |
| `codex.toml` | Codex | `~/.codex/config.toml` |
