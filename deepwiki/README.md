# DeepWiki

**[🇫🇷 Français](README_FR.md)**

AI-generated documentation for GitHub repositories (wiki structure, Q&A on a codebase).

| | |
|---|---|
| **Type** | remote |
| **Auth** | none |
| **Config key** | `deepwiki` |

Tools: read_wiki_structure, read_wiki_contents, ask_wiki_question.

## Config files per platform

| File | Platform | Location |
|---|---|---|
| `devin.json` | Devin | merge into `%APPDATA%\devin\mcp_config.json` under `mcpServers` |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (`servers` key) |
| `codex.toml` | Codex | `~/.codex/config.toml` |
