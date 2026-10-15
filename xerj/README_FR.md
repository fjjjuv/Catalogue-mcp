# XERJ — moteur de recherche + mémoire d'agent en MCP

**[🇬🇧 English](README.md)**
📄 **Guide complet, exemples & note :** [https://fjjjuv.github.io/Catalogue-mcp/serveurs/xerj.html](https://fjjjuv.github.io/Catalogue-mcp/serveurs/xerj.html)

> XERJ est un moteur de recherche écrit en Rust (compatible protocole
> Elasticsearch) avec un serveur MCP **dans le même binaire** : `xerj mcp`.
> Il indexe code, docs, logs et PDFs pour la recherche d'agent, le RAG et la
> mémoire long terme — et offre aussi un store durable `/_memory/{ns}`.

| | |
|---|---|
| **Type** | local stdio |
| **Auth** | aucune sur un nœud local (`--insecure`), sinon `XERJ_AUTH: ApiKey <clé>` |
| **Clé de config** | `xerj` |
| **Version testée** | xerj v1.0.0-rc.95 |
| **Prérequis** | un nœud qui tourne : `xerj --insecure --data-dir ~/.xerj/data` |

## Comment ça marche

Deux parties, un seul binaire :

```
# 1. Le moteur (nœud) — parle ES 8.x sur :9200
xerj --insecure --data-dir ~/.xerj/data

# 2. Le serveur MCP — proxifie vers ce nœud en stdio
xerj mcp
```

Le serveur MCP ne démarre **pas** le nœud. Si rien ne répond sur
`XERJ_URL`, les outils renvoient une erreur de connexion.

13 outils exposés : `xerj_search` (BM25 / DSL, définition d'abord sur le
code), `xerj_semantic_search`, `xerj_vector_search`, `xerj_hybrid_search`,
`xerj_memory_store`, `xerj_memory_recall`, `xerj_brain_*` (index de liens),
`xerj_plan`, `xerj_map`, `xerj_code_search`.

## Installation

```bash
curl -fsSL https://xerj.org/get | sh        # Linux / macOS / Git Bash
# Windows PowerShell :
powershell -ExecutionPolicy Bypass -c "irm https://xerj.org/get.ps1 | iex"
```

Le binaire arrive dans `~/.local/bin/xerj` (Windows :
`%USERPROFILE%\.local\bin\xerj.exe`).

## Indexer un dossier

```bash
xerj autoindex <dossier>            # écrit les index ax-* + autoindex-catalog
xerj autoindex <dossier> --dry-run  # estimation d'abord, rien indexé
```

Ensuite `xerj_map` (MCP) retourne la carte des champs de chaque index, et
`xerj_search` cherche dans `ax-*` par défaut — pas besoin du nom d'index.

## Mémoire d'agent sans indexation

```json
xerj_memory_store {"namespace": "projet", "text": "la prod utilise PostgreSQL"}
xerj_memory_recall {"namespace": "projet", "query": "base de données"}
```

Fonctionne même avec zéro dossier indexé — la mémoire vit dans ses propres index.

## Fichiers de config par plateforme

| Fichier | Plateforme | Emplacement |
|---|---|---|
| `devin.json` | Devin | à fusionner dans `%APPDATA%\devin\mcp_config.json` sous `mcpServers` |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (clé `servers`) |
| `codex.toml` | Codex | `~/.codex/config.toml` |

## Pièges

- **PATH des applis GUI** : les applis bureau peuvent ne pas voir `xerj` dans
  le PATH → mettre le chemin absolu du binaire dans `command`
  (ex. `C:\Users\<toi>\.local\bin\xerj.exe`).
- **Non indexé = introuvable** : xerj ne cherche que dans ce qu'`autoindex` a
  parcouru. Pour le reste, l'agent repasse sur ses outils classiques.
- **`--insecure`** = pas de clé API — OK pour localhost uniquement. Un vrai
  déploiement utilise `<data-dir>/admin.key` via `XERJ_AUTH`.
