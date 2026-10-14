# Playwright

**[🇫🇷 Français](README_FR.md)**
📄 **Full guide, examples & rating:** [https://fjjjuv.github.io/Catalogue-mcp/serveurs/playwright.html](https://fjjjuv.github.io/Catalogue-mcp/serveurs/playwright.html)


Playwright MCP server (Microsoft) — browser automation for agents:
navigate, click, fill forms, capture screenshots and the DOM.

| | |
|---|---|
| Package | `@playwright/mcp` (npm) |
| Type | **local** server (stdio) — unlike remote OAuth servers |
| Requirements | Node.js + npx |

## Files per platform

| File | Platform | Destination |
|---|---|---|
| `devin.json` | Devin | `mcpServers` in `%APPDATA%\devin\mcp_config.json` — uses `cmd.exe /c` on Windows |
| `cursor.json` | Cursor | `mcpServers` in `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `mcpServers` in `claude_desktop_config.json` |
| `vscode.json` | VS Code | `servers` in `.vscode/mcp.json` (`"type": "stdio"`) |
| `codex.toml` | Codex | `~/.codex/config.toml` |

## Claude Code (CLI)

```bash
claude mcp add playwright -- npx -y @playwright/mcp@latest
```

## Codex — CLI

```bash
codex mcp add playwright -- npx -y @playwright/mcp@latest
```

## Devin — CLI

```bash
devin mcp add playwright -- cmd.exe /c npx -y @playwright/mcp@latest
```

No OAuth: the server starts locally and the `browser_*` tools appear
directly.
