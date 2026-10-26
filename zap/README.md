# OWASP ZAP MCP Server

**[🇫🇷 Français](README_FR.md)**
📄 **Full guide, examples & rating:** [https://fjjjuv.github.io/Catalogue-mcp/serveurs/zap.html](https://fjjjuv.github.io/Catalogue-mcp/serveurs/zap.html)

Lets an AI assistant drive OWASP ZAP through the official "MCP Integration" add-on (ZAP 2.17+): start spiders, active scans, read alerts, generate reports.

| | |
|---|---|
| **Type** | local HTTP (`localhost:8282`) |
| **Auth** | security key in `Authorization` header |
| **Config key** | `zap` |
| **Requires** | OWASP ZAP running + MCP Integration add-on installed |

## Setup

1. In ZAP: install the **MCP Integration** add-on via Marketplace (Tools → Manage Add-ons)
2. Options → MCP Integration: enable the server (port `8282` by default)
3. Copy the **security key** and replace `VOTRE_CLE_SECURITE_ZAP` in the config files
4. Keep ZAP running — the MCP server only exists while ZAP is open

> ⚠️ **Never expose the server outside localhost** — it gives full control of ZAP, the key travels in plain HTTP, and CORS allows any origin.

## Config files per platform

| File | Platform | Location |
|---|---|---|
| `devin.json` | Devin | merge into `%APPDATA%\devin\mcp_config.json` under `mcpServers` |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (`servers` key) |
| `codex.toml` | Codex | `~/.codex/config.toml` |

## Troubleshooting (real cases)

| Problem | Cause | Solution |
|---|---|---|
| `HTTPS required` (JSON-RPC -32000) | `secureOnly: true` default | Edit `%USERPROFILE%\ZAP\config.xml` → `<secureOnly>false</secureOnly>` **while ZAP is fully closed** (it rewrites the file on exit) |
| Self-signed cert rejected (`https://localhost:8282`) | ZAP uses its own CA | Prefer plain HTTP on localhost (see above) — or accept the cert manually |
| `NullPointerException` when opening Options (ServerCertificatesOptionsPanel / InsightsParam) | Known ZAP bug in some add-on option panels | Update all add-ons via Marketplace; config can also be edited directly in `config.xml` (`<mcp>` section) |
| Port 8282 not listening | ZAP not running or add-on missing | Launch ZAP, verify `javaw` process + `netstat -an | findstr 8282` |
| "No implementor" on API port 8080 | MCP has no ZAP REST API actions | Normal — configure only via config.xml or Options panel |
| Key unknown / lost | Stored in config file | Read `<securityKey>` in `%USERPROFILE%\ZAP\config.xml` |
