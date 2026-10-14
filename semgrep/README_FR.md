# Semgrep — MCP "bricolé" local

**[🇬🇧 English](README.md)**
📄 **Guide complet, exemples & note :** [https://fjjjuv.github.io/Catalogue-mcp/serveurs/semgrep.html](https://fjjjuv.github.io/Catalogue-mcp/serveurs/semgrep.html)


> ⚠️ **Ce n'est pas un serveur MCP classique.** Semgrep est d'abord une
> **CLI d'analyse statique de sécurité** installée sur la machine. Sa
> commande `semgrep mcp` transforme la CLI en serveur MCP — c'est nous qui
> l'avons branché comme serveur dans la config.

| | |
|---|---|
| **Type** | local stdio |
| **Auth** | aucune (`semgrep login` optionnel pour règles/cloud) |
| **Clé de config** | `semgrep` |
| **Version testée** | Semgrep 1.180.0 (installé via `pip install semgrep`) |

## Comment ça marche

`semgrep mcp` lance le serveur MCP **embarqué dans la CLI** :

```
semgrep mcp                      # transport stdio (défaut, ce qu'on utilise)
semgrep mcp -t streamable-http   # mode serveur HTTP sur port 8000
```

Outils exposés à l'agent : `security_check`/`semgrep_scan` (scanner du
code ou un dossier), `semgrep_rule_schema` (écrire des règles custom),
`get_supported_languages`, etc.

### Hooks utiles (`semgrep mcp --hook`)

| Hook | Effet |
|---|---|
| `post-tool-cli-scan` | scan auto après chaque action de l'agent |
| `stop-cli-scan` + `record-file-edit` | scan à la fin d'une session d'édition |
| `inject-secure-defaults` | injecte des règles de sécurité dans le contexte |
| `supply-chain-scan` | scanne les deps quand une commande d'install est détectée |

## Prérequis

```bash
# Vérifier
semgrep --version

# Installer
pip install semgrep          # ou: brew install semgrep
```

⚠️ **Windows / Devin** : le nom `semgrep` n'est pas toujours trouvé dans
le PATH de l'application graphique → le serveur peut se marquer
`"disabled": true` tout seul au chargement. Solution : pointer le chemin
complet de l'exécutable (voir `devin.json`).

Chemin typique après `pip install` :
`C:\Users\<user>\AppData\Local\Programs\Python\Python312\Scripts\semgrep.exe`

## Scan manuel (sans MCP)

Pour un audit ponctuel, la CLI suffit — pas besoin du MCP :

```bash
semgrep scan --config auto --json -o semgrep-results.json
python -c "import json;d=json.load(open('semgrep-results.json'));print('findings:',len(d['results']))"
```

- `--config auto` : ~248 règles du registre public Semgrep
- Résultat : vulnérabilités, fuites de secrets, mauvaises pratiques
- Les erreurs de parsing (ex. snapshots `.yml` de Playwright) sont non bloquantes

## MCP vs CLI vs dashboard

| Besoin | Solution |
|---|---|
| Scan ponctuel | CLI `semgrep scan --config auto` |
| Sécurité vérifiée en continu pendant que l'agent code | **ce MCP** |
| Résultats en interface graphique | `semgrep login` + `semgrep ci` → dashboard semgrep.dev (gratuit, envoie les résultats au cloud) |

## Fichiers de config par plateforme

| Fichier | Plateforme | Emplacement |
|---|---|---|
| `devin.json` | Devin | fusionner dans `%APPDATA%\devin\mcp_config.json` sous `mcpServers` — **chemin absolu recommandé** |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (clé `servers`) |
| `codex.toml` | Codex | `~/.codex/config.toml` |

## Historique de mise en place

1. `semgrep --version` → non trouvé → `pip install semgrep` (1.180.0)
2. Scan initial du projet : 30 fichiers, 248 règles, 0 vulnérabilité
3. `semgrep mcp` ajouté dans la config globale Devin
4. Premier chargement → auto-désactivé (`disabled: true`) car `semgrep`
   pas dans le PATH graphique → corrigé avec le chemin absolu de `semgrep.exe`
