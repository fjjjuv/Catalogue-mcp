# XERJ — moteur de recherche local + mémoire d'agent, exposé en MCP

**[🇬🇧 English](README.md)**
📄 **Guide complet, exemples & note :** [https://fjjjuv.github.io/Catalogue-mcp/serveurs/xerj.html](https://fjjjuv.github.io/Catalogue-mcp/serveurs/xerj.html)

## C'est quoi ?

XERJ est un **moteur de recherche qui tourne sur ta machine** (un seul
binaire Rust, sans JVM ni dépendances). Tu lui donnes un dossier, il indexe
les fichiers, et ton agent IA peut alors **chercher dans tes vraies
données** au lieu de deviner — code, docs, logs, PDFs.

Il parle l'API Elasticsearch, et il embarque un **serveur MCP dans le même
binaire** : les agents peuvent l'utiliser directement.

## Pourquoi c'est utile

| Sans XERJ | Avec XERJ |
|---|---|
| L'agent `grep` des fichiers entiers → il brûle des tokens | Une requête renvoie le passage exact `fichier:ligne` |
| L'agent oublie tout entre les sessions | `xerj_memory_*` = mémoire durable et cherchable |
| Les API de recherche coûtent à chaque appel | Tout tourne **en local, gratuitement** |

## Prérequis

⚠️ **Important :** le serveur MCP a besoin d'un **nœud** XERJ qui tourne —
il ne le démarre pas tout seul. Deux processus :

```bash
# 1. Installer le binaire
curl -fsSL https://xerj.org/get | sh        # Linux / macOS / Git Bash
powershell -ExecutionPolicy Bypass -c "irm https://xerj.org/get.ps1 | iex"  # Windows

# 2. Démarrer le nœud (le laisser tourner)
xerj --insecure --data-dir ~/.xerj/data
# → écoute sur http://localhost:9200, console : http://localhost:9200/_xerj-console/
```

Les configs MCP de ce dossier lancent ensuite `xerj mcp`, qui fait simple‐
ment proxy vers ce nœud.

## Test rapide

```bash
# Indexer un dossier (quelques secondes pour un petit projet)
xerj autoindex ./mon-projet

# Côté agent : xerj_map liste les champs indexés
```

## Ce que l'agent reçoit (13 outils)

- **`xerj_search`** — recherche plein texte/code, la définition classée en premier
- **`xerj_semantic_search` / `xerj_vector_search` / `xerj_hybrid_search`** — recherche par le sens
- **`xerj_memory_store` / `xerj_memory_recall`** — mémoire long terme (marche même sans dossier indexé)
- **`xerj_map`** — « qu'est-ce qui est indexé, avec quels champs »
- **`xerj_brain_*`** — index de liens/relations
- **`xerj_plan`**, **`xerj_code_search`** — planificateur de requêtes, recherche de code de référence

## Fichiers de config par plateforme

| Fichier | Plateforme | Emplacement |
|---|---|---|
| `devin.json` | Devin | à fusionner dans `%APPDATA%\devin\mcp_config.json` sous `mcpServers` |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (clé `servers`) |
| `codex.toml` | Codex | `~/.codex/config.toml` |

## Pièges

- **Les applis GUI peuvent ne pas voir `xerj` dans le PATH** → mettre le
  chemin absolu dans `command`, ex. `C:\Users\<toi>\.local\bin\xerj.exe`.
- **Non indexé = introuvable.** XERJ ne cherche que dans ce qu'`autoindex`
  a couvert ; pour le reste, l'agent repasse sur ses outils classiques.
- **`--insecure` est pour localhost uniquement.** Un vrai déploiement
  utilise la clé API de `<data-dir>/admin.key` via `XERJ_AUTH`.

| | |
|---|---|
| **Type** | local stdio |
| **Auth** | aucune sur un nœud local (`--insecure`), sinon `XERJ_AUTH: ApiKey <clé>` |
| **Clé de config** | `xerj` |
| **Version testée** | xerj v1.0.0-rc.95 |
