# Serveur MCP OWASP ZAP

**[🇬🇧 English](README.md)**
📄 **Guide complet, exemples & note :** [https://fjjjuv.github.io/Catalogue-mcp/serveurs/zap.html](https://fjjjuv.github.io/Catalogue-mcp/serveurs/zap.html)

Permet à un assistant IA de piloter OWASP ZAP via l'add-on officiel « MCP Integration » (ZAP 2.17+) : lancer des spiders, scans actifs, lire les alertes, générer des rapports.

| | |
|---|---|
| **Type** | HTTP local (`localhost:8282`) |
| **Auth** | clé de sécurité dans l'en-tête `Authorization` |
| **Clé de config** | `zap` |
| **Requis** | OWASP ZAP lancé + add-on MCP Integration installé |

## Installation

1. Dans ZAP : installez l'add-on **MCP Integration** via le Marketplace (Outils → Gérer les modules)
2. Options → MCP Integration : activez le serveur (port `8282` par défaut)
3. Copiez la **clé de sécurité** et remplacez `VOTRE_CLE_SECURITE_ZAP` dans les fichiers de config
4. Gardez ZAP ouvert — le serveur MCP n'existe que pendant que ZAP tourne

> ⚠️ **N'exposez jamais le serveur hors de localhost** — il donne le contrôle total de ZAP, la clé circule en HTTP clair, et le CORS autorise toute origine.

## Fichiers de config par plateforme

| Fichier | Plateforme | Emplacement |
|---|---|---|
| `devin.json` | Devin | fusionner dans `%APPDATA%\devin\mcp_config.json` sous `mcpServers` |
| `cursor.json` | Cursor | `.cursor/mcp.json` |
| `claude-desktop.json` | Claude Desktop | `claude_desktop_config.json` |
| `vscode.json` | VS Code | `.vscode/mcp.json` (clé `servers`) |
| `codex.toml` | Codex | `~/.codex/config.toml` |

## Dépannage (cas réels)

| Problème | Cause | Solution |
|---|---|---|
| `HTTPS required` (JSON-RPC -32000) | `secureOnly: true` par défaut | Éditez `%USERPROFILE%\ZAP\config.xml` → `<secureOnly>false</secureOnly>` **pendant que ZAP est complètement fermé** (il réécrit le fichier à la sortie) |
| Certificat auto-signé refusé (`https://localhost:8282`) | ZAP utilise sa propre CA | Préférez le HTTP simple sur localhost (voir ci-dessus) — ou acceptez le certificat manuellement |
| `NullPointerException` à l'ouverture des Options (ServerCertificatesOptionsPanel / InsightsParam) | Bug connu de certains panneaux d'add-ons ZAP | Mettez à jour tous les add-ons via le Marketplace ; la config peut aussi être éditée directement dans `config.xml` (section `<mcp>`) |
| Port 8282 non ouvert | ZAP non lancé ou add-on absent | Lancez ZAP, vérifiez le processus `javaw` + `netstat -an | findstr 8282` |
| « No implementor » sur l'API port 8080 | Le MCP n'a pas d'actions REST ZAP | Normal — configurez uniquement via `config.xml` ou le panneau Options |
| Clé inconnue / perdue | Stockée dans le fichier de config | Lisez `<securityKey>` dans `%USERPROFILE%\ZAP\config.xml` |
