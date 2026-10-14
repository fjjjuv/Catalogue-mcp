# GitHub MCP Server (official)

**[🇫🇷 Français](README_FR.md)**

Access to the GitHub API: repos, files, issues, PRs, releases, commits, code search.

| | |
|---|---|
| **Type** | remote |
| **Auth** | OAuth / GitHub token |
| **Config key** | `github` |

Read-only + write depending on granted scopes.

## Config files per platform

| File | Platform | Location |
|---|---|---|
| `devin.json` | Devin | merge into `%APPDATA%\devin\mcp_config.json` under `mcpServers` |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (`servers` key) |
| `codex.toml` | Codex | `~/.codex/config.toml` |
