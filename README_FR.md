<p align="center">
  <img src="https://fjjjuv.github.io/Catalogue-mcp/logo.svg" alt="Catalogue-mcp" width="96" height="96">
</p>

<h1 align="center">Catalogue-mcp</h1>

<p align="center">
  <strong>14 serveurs MCP. 6 plateformes. Une config plug-and-play pour chacun.</strong><br>
  Donnez à votre agent IA de vrais super-pouvoirs — boards, repos, navigateur, mémoire, scans de sécurité.
</p>

<p align="center">
  <a href="https://fjjjuv.github.io/Catalogue-mcp/">🌐 Site web</a> •
  <a href="README.md">🇬🇧 English</a> •
  <a href="LICENSE">📄 Licence MIT</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/serveurs_MCP-14-6366f1" alt="13 serveurs">
  <img src="https://img.shields.io/badge/plateformes-6-38bdf8" alt="6 plateformes">
  <img src="https://img.shields.io/badge/co%C3%BBt-100%25_gratuit-34d399" alt="gratuit">
  <img src="https://img.shields.io/badge/licence-MIT-f59e0b" alt="MIT">
</p>

---

## 🚀 Pourquoi ce dépôt

Un serveur MCP = une nouvelle compétence pour votre agent. Ce catalogue
vous donne **le fichier de config exact** à déposer dans Devin, Cursor,
Claude Desktop, VS Code ou Codex — sans fouiller la doc, sans deviner le
format.

- ⚡ **Zéro copier-coller** — l'agent lit/écrit directement dans vos outils (Trello, GitHub…)
- 📚 **Vérité terrain** — Context7 et DeepWiki injectent la vraie doc à jour
- 🔒 **Sécurité continue** — Semgrep scanne pendant que l'agent écrit
- 🖥️ **Actions réelles** — Playwright navigue pour de vrai, Computer Use clique sur votre bureau
- 🧠 **Mémoire** — vos préférences survivent entre les sessions

## 📦 Les serveurs

| Dossier | Serveur | Super-pouvoir | Type | Auth | 📖 |
|---|---|---|---|---|---|
| [`trello/`](trello/) | Trello (officiel Atlassian) | Gère boards, cartes & checklists | remote | OAuth 2.0 | [→](https://fjjjuv.github.io/Catalogue-mcp/serveurs/trello.html) |
| [`github/`](github/) | GitHub MCP Server | Repos, issues, PR, recherche de code | remote | OAuth / token | [→](https://fjjjuv.github.io/Catalogue-mcp/serveurs/github.html) |
| [`asana/`](asana/) | Asana | Tâches & projets | remote | OAuth 2.0 | [→](https://fjjjuv.github.io/Catalogue-mcp/serveurs/asana.html) |
| [`deepwiki/`](deepwiki/) | DeepWiki | Q&A sur n'importe quel codebase | remote | aucune | [→](https://fjjjuv.github.io/Catalogue-mcp/serveurs/deepwiki.html) |
| [`exa-code/`](exa-code/) | Exa Code | Recherche de code sémantique | remote | compte Exa | [→](https://fjjjuv.github.io/Catalogue-mcp/serveurs/exa-code.html) |
| [`cloudflare-docs/`](cloudflare-docs/) | Cloudflare Docs | Doc officielle Cloudflare | remote | aucune | [→](https://fjjjuv.github.io/Catalogue-mcp/serveurs/cloudflare-docs.html) |
| [`playwright/`](playwright/) | Playwright | Automatisation navigateur réelle | local stdio | aucune | [→](https://fjjjuv.github.io/Catalogue-mcp/serveurs/playwright.html) |
| [`puppeteer/`](puppeteer/) | Puppeteer | Automatisation Chrome via CDP | local stdio | aucune | [→](https://fjjjuv.github.io/Catalogue-mcp/serveurs/puppeteer.html) |
| [`computer-use/`](computer-use/) | Computer Use | Souris & clavier sur votre PC | local stdio | aucune | [→](https://fjjjuv.github.io/Catalogue-mcp/serveurs/computer-use.html) |
| [`context7/`](context7/) | Context7 (Upstash) | Doc des libs à jour dans le contexte | local stdio | aucune | [→](https://fjjjuv.github.io/Catalogue-mcp/serveurs/context7.html) |
| [`memory/`](memory/) | Memory | Graphe de connaissances persistant | local stdio | aucune | [→](https://fjjjuv.github.io/Catalogue-mcp/serveurs/memory.html) |
| [`semgrep/`](semgrep/) | Semgrep | Scans de sécurité pendant le code | local stdio | aucune | [→](https://fjjjuv.github.io/Catalogue-mcp/serveurs/semgrep.html) |
| [`xerj/`](xerj/) | XERJ | Moteur de recherche + mémoire d’agent (autoindex) | local stdio | aucune | [→](https://fjjjuv.github.io/Catalogue-mcp/serveurs/xerj.html) |
| [`zap/`](zap/) | OWASP ZAP | Pilotez des scans de sécurité par IA | HTTP local | clé de sécurité | [→](https://fjjjuv.github.io/Catalogue-mcp/serveurs/zap.html) |

📊 Comparatif complet & notes → **[fjjjuv.github.io/Catalogue-mcp](https://fjjjuv.github.io/Catalogue-mcp/)**

## 🛠️ Organisation

Un dossier par serveur, un fichier de config par plateforme — le nom
dit où il va :

```
<serveur>/
  README.md            # doc du serveur (EN)
  README_FR.md         # doc (FR)
  devin.json           # → %APPDATA%\devin\mcp_config.json
  cursor.json          # → .cursor/mcp.json
  claude-desktop.json  # → claude_desktop_config.json
  vscode.json          # → .vscode/mcp.json (clé "servers")
  codex.toml           # → ~/.codex/config.toml
```

| Plateforme | Clé racine | Format |
|---|---|---|
| Devin | `mcpServers` | JSON |
| Cursor | `mcpServers` | JSON |
| Claude Desktop | `mcpServers` | JSON |
| VS Code | `servers` + `type` | JSON |
| Codex | `mcp_servers.*` | TOML |
| Claude Code | via `claude mcp add` | CLI |

## 📄 Licence

[MIT](LICENSE) — gratuit, open source, faites-en ce que vous voulez.
