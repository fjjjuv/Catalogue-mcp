# Context7 (Upstash)

**[🇫🇷 Français](README_FR.md)**

Up-to-date library documentation + code examples injected into context.

| | |
|---|---|
| **Type** | local stdio |
| **Auth** | none (optional API key) |
| **Config key** | `context7` |

Supports `use context7` in prompts.

## Config files per platform

| File | Platform | Location |
|---|---|---|
| `devin.json` | Devin | merge into `%APPDATA%\devin\mcp_config.json` under `mcpServers` |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (`servers` key) |
| `codex.toml` | Codex | `~/.codex/config.toml` |
