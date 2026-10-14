# Semgrep — DIY local MCP

**[🇫🇷 Français](README_FR.md)**
📄 **Full guide, examples & rating:** [https://fjjjuv.github.io/Catalogue-mcp/serveurs/semgrep.html](https://fjjjuv.github.io/Catalogue-mcp/serveurs/semgrep.html)


> ⚠️ **This is not a regular MCP server.** Semgrep is first a
> **static security analysis CLI** installed on the machine. Its
> `semgrep mcp` command turns the CLI into an MCP server — we wired it
> up ourselves in the config.

| | |
|---|---|
| **Type** | local stdio |
| **Auth** | none (`semgrep login` optional for rules/cloud) |
| **Config key** | `semgrep` |
| **Tested version** | Semgrep 1.180.0 (installed via `pip install semgrep`) |

## How it works

`semgrep mcp` launches the MCP server **built into the CLI**:

```
semgrep mcp                      # stdio transport (default, what we use)
semgrep mcp -t streamable-http   # HTTP server mode on port 8000
```

Tools exposed to the agent: `security_check`/`semgrep_scan` (scan code
or a folder), `semgrep_rule_schema` (write custom rules),
`get_supported_languages`, etc.

### Useful hooks (`semgrep mcp --hook`)

| Hook | Effect |
|---|---|
| `post-tool-cli-scan` | auto-scan after each agent action |
| `stop-cli-scan` + `record-file-edit` | scan at the end of an editing session |
| `inject-secure-defaults` | injects security rules into the context |
| `supply-chain-scan` | scans deps when an install command is detected |

## Requirements

```bash
# Check
semgrep --version

# Install
pip install semgrep          # or: brew install semgrep
```

⚠️ **Windows / Devin**: the `semgrep` name is not always found in the
GUI application's PATH → the server may mark itself
`"disabled": true` at load time. Fix: point to the full executable
path (see `devin.json`).

Typical path after `pip install`:
`C:\Users\<user>\AppData\Local\Programs\Python\Python312\Scripts\semgrep.exe`

## Manual scan (no MCP)

For a one-off audit, the CLI is enough — no MCP needed:

```bash
semgrep scan --config auto --json -o semgrep-results.json
python -c "import json;d=json.load(open('semgrep-results.json'));print('findings:',len(d['results']))"
```

- `--config auto`: ~248 rules from the public Semgrep registry
- Result: vulnerabilities, secret leaks, bad practices
- Parsing errors (e.g. Playwright `.yml` snapshots) are non-blocking

## MCP vs CLI vs dashboard

| Need | Solution |
|---|---|
| One-off scan | CLI `semgrep scan --config auto` |
| Security checked continuously while the agent codes | **this MCP** |
| Results in a GUI | `semgrep login` + `semgrep ci` → semgrep.dev dashboard (free, sends results to the cloud) |

## Config files per platform

| File | Platform | Location |
|---|---|---|
| `devin.json` | Devin | merge into `%APPDATA%\devin\mcp_config.json` under `mcpServers` — **absolute path recommended** |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (`servers` key) |
| `codex.toml` | Codex | `~/.codex/config.toml` |

## Setup history

1. `semgrep --version` → not found → `pip install semgrep` (1.180.0)
2. Initial project scan: 30 files, 248 rules, 0 vulnerabilities
3. `semgrep mcp` added to the global Devin config
4. First load → auto-disabled (`disabled: true`) because `semgrep`
   wasn't in the GUI PATH → fixed with the absolute `semgrep.exe` path
