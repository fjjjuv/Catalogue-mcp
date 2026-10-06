# Codex

## Via CLI

```bash
codex mcp add trello --url https://mcp.trello.com/v1
codex mcp add asana --url https://mcp.asana.com/v2/mcp
codex mcp login <nom>
```

## Via config

Fusionner les blocs de `servers/*.toml` dans `~/.codex/config.toml`,
puis `codex mcp login <nom>` pour le flux OAuth.
