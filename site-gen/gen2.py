# -*- coding: utf-8 -*-
"""Site Catalogue-mcp v2 — style prompt-flamegraph + i18n FR/EN."""
import os, json, html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

BASE = "https://fjjjuv.github.io/Catalogue-mcp"
REPO = "https://github.com/fjjjuv/Catalogue-mcp"
SITE_REPO = "https://github.com/fjjjuv/Catalogue-mcp"

T = {}  # key -> {"en":..., "fr":...}
def tr(key, en, fr): T[key] = {"en": en, "fr": fr}

# ============ UI STRINGS ===================================================
UI = {
 "nav_home":("Home","Accueil"),"nav_servers":("Servers","Serveurs"),
 "nav_compare":("Compare","Comparatif"),"nav_guide":("Guide","Guide"),
 "nav_github":("GitHub","GitHub"),"brand":"Catalogue-mcp",
 "official":("official","officiel"),"community":("community","communauté"),
 "type":("Type","Type"),"endpoint":("Endpoint / command","Endpoint / commande"),
 "auth":("Authentication","Authentification"),"cost":("Cost","Coût"),
 "difficulty":("Installation","Installation"),"score":("Score","Note"),
 "what":("What it does","Ce qu'il permet"),
 "examples":("Example requests","Exemples de demandes"),
 "ask":("You ask the agent","Demande à l'agent"),
 "result":("Result","Résultat"),
 "why":("Why it changes the game","En quoi il change la vie"),
 "config":("Configuration","Configuration"),
 "cfg_intro":("Ready-to-use config files for Devin, Cursor, Claude Desktop, VS Code and Codex are in the repo:",
              "Les fichiers prêts à l'emploi pour Devin, Cursor, Claude Desktop, VS Code et Codex sont dans le dépôt :"),
 "back_servers":("← All servers","← Tous les serveurs"),
 "cat":("Category","Catégorie"),"server":("Server","Serveur"),
 "foot_by":('© <span class="copyright-year"></span> <a href="https://github.com/fjjjuv" rel="me author">fjjjuv</a> (Julien) — France 🇫🇷 · All content free &amp; open source','© <span class="copyright-year"></span> <a href="https://github.com/fjjjuv" rel="me author">fjjjuv</a> (Julien) — France 🇫🇷 · Contenu 100 % gratuit et open source'),
 "foot_repo":("Config repo","Dépôt des configs"),
 "back_top":("Back to top","Haut de page"),
}
for k,v in UI.items():
    tr(k, *(v if isinstance(v,tuple) else (v,v)))

# Install difficulty scale: 1 = very easy … 5 = very hard
DIFF_EN = {1:"very easy",2:"easy",3:"medium",4:"hard",5:"very hard"}
DIFF_FR = {1:"très facile",2:"facile",3:"moyen",4:"difficile",5:"très difficile"}
for i in range(1,6): tr(f"diff{i}", DIFF_EN[i], DIFF_FR[i])

def difftag(s):
    return f'<span class="diff d{s["diff"]}" data-i18n="diff{s["diff"]}">{DIFF_EN[s["diff"]]}</span>'

# ============ SERVERS ======================================================
S = [
 dict(slug="github", name="GitHub MCP Server", official=True, score=5.0, diff=2,
      cat_en="Development", cat_fr="Développement",
      typ_en="remote (HTTPS)", typ_fr="remote (HTTPS)",
      auth_en="OAuth / PAT", auth_fr="OAuth / PAT",
      cout_en="Free", cout_fr="Gratuit",
      url="https://api.githubcopilot.com/mcp",
      r_en="GitHub's official server (46 tools): read and write on your repos — files, commits, branches, issues, PRs, releases, code search.",
      r_fr="Le serveur officiel de GitHub (46 outils) : lecture et écriture sur les repos — fichiers, commits, branches, issues, PR, releases, recherche de code.",
      f_en=["Read/edit files without cloning the repo","Create branches, commits, PRs and releases","Read and answer issues and reviews","Search code across the whole org"],
      f_fr=["Lire/modifier des fichiers sans cloner le repo","Créer branches, commits, PR et releases","Lire et répondre aux issues et reviews","Rechercher du code dans toute l'org"],
      ex=[("Create a README file in Catalogue-mcp","direct push_files via the API","Crée un fichier README dans Catalogue-mcp","push_files direct via l'API"),
          ("List open PRs and summarize reviews","project status in one sentence","Liste les PR ouvertes et résume les reviews","état du projet en une phrase"),
          ("Find where function X is used","cross-repo search_code","Cherche où la fonction X est utilisée","search_code cross-repo")],
      w_en="The agent manipulates the remote repo without a local checkout — commits, PRs and releases driven in conversation.",
      w_fr="L'agent manipule le dépôt distant sans checkout local — commits, PR et releases pilotés en conversation."),
 dict(slug="playwright", name="Playwright", official=True, score=4.9, diff=1,
      cat_en="Browser", cat_fr="Navigateur",
      typ_en="local stdio (npx)", typ_fr="local stdio (npx)",
      auth_en="none", auth_fr="aucune",
      cout_en="Free", cout_fr="Gratuit",
      url="npx -y @playwright/mcp@latest",
      r_en="Full browser automation: the agent navigates, clicks, fills, extracts and screenshots real web pages.",
      r_fr="Automatisation navigateur complète : l'agent navigue, clique, remplit, extrait et photographie des pages web.",
      f_en=["Navigate and interact with real sites","Screenshots and accessibility snapshots","Fill forms, test user flows","Visually verify a web app works"],
      f_fr=["Naviguer et interagir avec des sites réels","Captures d'écran et snapshots d'accessibilité","Remplir des formulaires, tester des parcours","Vérifier qu'une app web fonctionne visuellement"],
      ex=[("Open my app and check the login works","conversational E2E test","Ouvre mon app et vérifie que le login marche","test E2E conversationnel"),
          ("Take a mobile screenshot of the page","device-emulation screenshot","Fais une capture de la page en mobile","screenshot device-émulation"),
          ("Fill the form and submit","automation without a script","Remplis le formulaire et valide","automatisation sans script")],
      w_en="The agent tests your web apps like a human — real navigation, not just HTTP requests.",
      w_fr="L'agent teste vos applications web comme un humain — navigation réelle, pas juste des requêtes HTTP."),
 dict(slug="trello", name="Trello", official=True, score=4.8, diff=3,
      cat_en="Project management", cat_fr="Gestion de projet",
      typ_en="remote (HTTPS)", typ_fr="remote (HTTPS)",
      auth_en="OAuth 2.0", auth_fr="OAuth 2.0",
      cout_en="Free", cout_fr="Gratuit",
      url="https://mcp.trello.com/v1",
      r_en="Atlassian's official Trello server: the agent reads and writes your boards, lists, cards, checklists and comments.",
      r_fr="Le serveur MCP officiel d'Atlassian pour Trello : l'agent lit et écrit vos boards, listes, cartes, checklists et commentaires.",
      f_en=["List boards and workspaces","Create/move/complete cards","Manage lists, checklists, labels, due dates","Comment, search, read the inbox"],
      f_fr=["Lister les boards et workspaces","Créer/déplacer/compléter des cartes","Gérer listes, checklists, étiquettes, dates","Commenter, chercher, consulter l'inbox"],
      ex=[("Migrate my Asana project to Trello","board+lists+cards preserving descriptions and due dates","Migre mon projet Asana vers Trello","board, listes et cartes avec descriptions et échéances"),
          ("Which cards are overdue?","scans due dates and summarizes","Quelles cartes sont en retard ?","scanne les due dates et résume"),
          ("Add a 'Tests' card in Doing with a checklist","direct creation","Ajoute une carte 'Tests' dans En cours avec checklist","création directe")],
      w_en="Chat-driven project management: no need to open Trello to update tasks — the agent does it while it codes.",
      w_fr="Gestion de projet pilotée par le chat : plus besoin d'ouvrir Trello — l'agent met à jour pendant qu'il code."),
 dict(slug="context7", name="Context7", official=False, score=4.7, diff=1,
      cat_en="Documentation", cat_fr="Documentation",
      typ_en="local stdio (npx)", typ_fr="local stdio (npx)",
      auth_en="none (optional API key)", auth_fr="aucune (clé API optionnelle)",
      cout_en="Free", cout_fr="Gratuit",
      url="npx -y @upstash/context7-mcp@1.0.31",
      r_en="Injects up-to-date library documentation into context — real versions, official examples.",
      r_fr="Injecte dans le contexte la documentation à jour des bibliothèques — versions réelles, exemples officiels.",
      f_en=["Fetch official docs of a specific library","Provide current code examples","Avoid answers based on outdated versions"],
      f_fr=["Récupérer la doc officielle d'une lib précise","Fournir des exemples de code actuels","Éviter les réponses basées sur des versions obsolètes"],
      ex=[("Use Next.js 15 — use context7","agent reads the recent official doc","Utilise Next.js 15 — use context7","l'agent lit la doc officielle récente"),
          ("How does onUploadProgress work in axios?","official example injected","Comment marche onUploadProgress dans axios ?","exemple officiel injecté"),
          ("Show me the PySide6 QTableWidget API","up-to-date Qt docs","Montre l'API PySide6 QTableWidget","doc Qt à jour")],
      w_en="Cuts hallucinations: the agent quotes the real doc of the right version instead of reciting memory.",
      w_fr="Réduit les hallucinations : l'agent cite la vraie doc de la bonne version au lieu de réciter sa mémoire."),
 dict(slug="deepwiki", name="DeepWiki", official=False, score=4.6, diff=1,
      cat_en="Documentation", cat_fr="Documentation",
      typ_en="remote (HTTPS)", typ_fr="remote (HTTPS)",
      auth_en="none", auth_fr="aucune",
      cout_en="Free", cout_fr="Gratuit",
      url="https://mcp.deepwiki.com/mcp",
      r_en="AI-powered docs for GitHub repos: generated wiki structure, architecture explanations, Q&A on any codebase.",
      r_fr="Documentation IA des dépôts GitHub : structure wiki générée, explications d'architecture, questions-réponses sur un codebase.",
      f_en=["Read a repo's wiki structure","Ask questions about any GitHub project","Understand unknown code fast"],
      f_fr=["Lire la structure wiki d'un repo","Poser des questions sur un projet GitHub","Comprendre vite un code inconnu"],
      ex=[("Explain fast-plate-ocr's architecture","answer based on the real code","Explique l'architecture de fast-plate-ocr","réponse fondée sur le vrai code"),
          ("How does this project handle auth?","on-demand generated wiki","Comment ce projet gère-t-il l'auth ?","wiki généré à la demande"),
          ("List this repo's main modules","instant overview","Liste les modules principaux de ce repo","vue d'ensemble instantanée")],
      w_en="Understand an open-source repo in 2 minutes instead of an hour of reading — perfect to evaluate a dependency.",
      w_fr="Comprendre un repo open source en 2 minutes au lieu d'une heure de lecture — parfait pour évaluer une dépendance."),
 dict(slug="asana", name="Asana", official=True, score=4.5, diff=2,
      cat_en="Project management", cat_fr="Gestion de projet",
      typ_en="remote (HTTPS)", typ_fr="remote (HTTPS)",
      auth_en="OAuth 2.0", auth_fr="OAuth 2.0",
      cout_en="Free", cout_fr="Gratuit",
      url="https://mcp.asana.com/v2/mcp",
      r_en="The official Asana MCP: access to projects, tasks, sections and comments across the workspace.",
      r_fr="Le MCP officiel Asana : accès aux projets, tâches, sections et commentaires du workspace.",
      f_en=["Enumerate projects and tasks","Read descriptions, sections, due dates","Update and complete tasks","Search the whole workspace"],
      f_fr=["Énumérer projets et tâches","Lire descriptions, sections, échéances","Mettre à jour et compléter des tâches","Rechercher dans tout le workspace"],
      ex=[("List my tasks for this week","consolidated view without opening Asana","Liste mes tâches de la semaine","vue consolidée sans ouvrir Asana"),
          ("Which tasks in project X are blocked?","section analysis","Quelles tâches du projet X sont bloquées ?","analyse des sections"),
          ("Prepare the migration to Trello","full project export","Prépare la migration vers Trello","export complet des projets")],
      w_en="Ideal to extract and reorganize an existing project — it's what powered our Asana→Trello migration.",
      w_fr="Idéal pour extraire et réorganiser un projet existant — c'est ce qui a servi à la migration Asana→Trello."),
 dict(slug="semgrep", name="Semgrep", official=False, score=4.5, diff=5,
      cat_en="Security", cat_fr="Sécurité",
      typ_en="local stdio", typ_fr="local stdio",
      auth_en="none (optional login)", auth_fr="aucune (login optionnel)",
      cout_en="Free", cout_fr="Gratuit",
      url="semgrep mcp (local CLI → MCP server)",
      r_en="Static security analysis turned into an MCP: we hacked the `semgrep mcp` CLI command into a server.",
      r_fr="Analyse statique de sécurité transformée en MCP : on a bricolé la commande `semgrep mcp` pour en faire un serveur.",
      f_en=["Scan code for vulnerabilities and secrets","Check quality/security on every edit (hooks)","Write custom rules for the project","Supply-chain audit of dependencies"],
      f_fr=["Scanner du code pour vulnérabilités et secrets","Vérifier la sécurité à chaque édition (hooks)","Écrire des règles custom pour le projet","Audit supply-chain des dépendances"],
      ex=[("Scan the project for flaws","248 rules from the auto registry","Scanne le projet pour des failles","248 règles du registre auto"),
          ("Check this file you just modified","continuous security","Vérifie ce fichier que tu viens de modifier","sécurité en continu"),
          ("Write a rule to forbid eval()","generated custom rule","Écris une règle pour interdire eval()","règle custom générée")],
      w_en="Security becomes continuous: the agent detects and fixes flaws while writing code, not after.",
      w_fr="La sécurité devient continue : l'agent détecte et corrige les failles pendant qu'il écrit le code, pas après."),
 dict(slug="memory", name="Memory", official=True, score=4.4, diff=1,
      cat_en="Persistence", cat_fr="Persistance",
      typ_en="local stdio (npx)", typ_fr="local stdio (npx)",
      auth_en="none", auth_fr="aucune",
      cout_en="Free", cout_fr="Gratuit",
      url="npx -y @modelcontextprotocol/server-memory",
      r_en="Persistent knowledge graph: the agent remembers facts, preferences and relations across sessions.",
      r_fr="Graphe de connaissances persistant : l'agent mémorise des faits, préférences et relations entre les sessions.",
      f_en=["Create durable entities and relations","Remember user preferences","Retrieve past decisions"],
      f_fr=["Créer des entités et relations durables","Se souvenir des préférences utilisateur","Retrouver des décisions passées"],
      ex=[("Remember I prefer commits in French","stored for next sessions","Souviens-toi que je préfère les commits en français","stocké pour les sessions suivantes"),
          ("How is this project organized?","graph re-read","Rappelle-moi comment est organisé ce projet","relecture du graphe"),
          ("Note that prod uses PostgreSQL","project memory","Note que le serveur prod utilise PostgreSQL","mémoire projet")],
      w_en="The agent doesn't restart from zero each session: conventions, decisions and context survive.",
      w_fr="L'agent ne repart pas de zéro à chaque session : conventions, décisions et contexte survivent."),
 dict(slug="puppeteer", name="Puppeteer", official=True, score=4.3, diff=1,
      cat_en="Browser", cat_fr="Navigateur",
      typ_en="local stdio (npx)", typ_fr="local stdio (npx)",
      auth_en="none", auth_fr="aucune",
      cout_en="Free", cout_fr="Gratuit",
      url="npx -y @modelcontextprotocol/server-puppeteer",
      r_en="Chrome automation via the DevTools protocol: navigation, screenshots, JavaScript execution in the page.",
      r_fr="Automatisation Chrome via le protocole DevTools : navigation, screenshots, exécution JavaScript dans la page.",
      f_en=["Drive a Chrome instance","Run JS inside the page","Screenshots and DOM extraction"],
      f_fr=["Piloter une instance Chrome","Exécuter du JS dans la page","Captures d'écran et extraction DOM"],
      ex=[("Screenshot the homepage","quick capture","Screenshot de la page d'accueil","capture rapide"),
          ("Run this script in the page","JS in the site's real context","Exécute ce script dans la page","JS dans le vrai contexte du site"),
          ("Check the button is visible","DOM assertion","Vérifie que le bouton est visible","assertion DOM")],
      w_en="A lightweight Chrome-focused alternative to Playwright — handy to script directly inside the page.",
      w_fr="Alternative légère à Playwright centrée Chrome — utile pour scripter directement dans la page."),
 dict(slug="exa-code", name="Exa Code", official=False, score=4.2, diff=3,
      cat_en="Search", cat_fr="Recherche",
      typ_en="remote (HTTPS)", typ_fr="remote (HTTPS)",
      auth_en="Exa API key", auth_fr="clé API Exa",
      cout_en="Freemium", cout_fr="Freemium",
      url="https://mcp.exa.ai/mcp",
      r_en="Code-oriented semantic web search: finds relevant examples, libraries and docs beyond keywords.",
      r_fr="Recherche web sémantique orientée code : trouve des exemples, libs et docs pertinents au-delà des mots-clés.",
      f_en=["Search real code examples","Find libraries matching a need","Explore docs and technical discussions"],
      f_fr=["Rechercher des exemples de code réels","Trouver des bibliothèques adaptées à un besoin","Explorer des docs et discussions techniques"],
      ex=[("Find ByteTrack + ONNX Runtime examples","targeted semantic results","Trouve des exemples de ByteTrack + ONNX Runtime","résultats sémantiques ciblés"),
          ("Which OCR libs exist for French plates?","augmented search","Quelles libs OCR pour plaques FR existent ?","recherche augmentée"),
          ("Compare recent ALPR frameworks","tech watch","Compare les frameworks ALPR récents","veille technique")],
      w_en="Complements classic search when the need is fuzzy or very specific — semantics find what keywords miss.",
      w_fr="Complète la recherche classique quand le besoin est flou ou très spécifique — la sémantique trouve ce que les mots-clés ratent."),
 dict(slug="cloudflare-docs", name="Cloudflare Docs", official=True, score=4.0, diff=1,
      cat_en="Documentation", cat_fr="Documentation",
      typ_en="remote (HTTPS)", typ_fr="remote (HTTPS)",
      auth_en="none", auth_fr="aucune",
      cout_en="Free", cout_fr="Gratuit",
      url="https://docs.mcp.cloudflare.com/mcp",
      r_en="Direct access to official Cloudflare docs: Workers, Pages, R2, DNS, security.",
      r_fr="Accès direct à la documentation officielle Cloudflare : Workers, Pages, R2, DNS, sécurité.",
      f_en=["Search Cloudflare documentation","Step-by-step Workers/Pages guides","Answers grounded in up-to-date docs"],
      f_fr=["Rechercher dans la doc Cloudflare","Guides pas à pas Workers/Pages","Réponses fondées sur les docs à jour"],
      ex=[("How to deploy a Worker with R2?","official doc directly","Comment déployer un Worker avec R2 ?","doc officielle directement"),
          ("Set up a 301 redirect on Pages","exact _redirects syntax","Configure un redirect 301 sur Pages","syntaxe exacte _redirects"),
          ("What are Workers' free limits?","official numbers","Quelles limites gratuites pour Workers ?","chiffres officiels")],
      w_en="If you host on Cloudflare, the agent answers with official docs, not approximate memories.",
      w_fr="Si vous hébergez chez Cloudflare, l'agent répond avec la doc officielle, pas avec des souvenirs approximatifs."),
 dict(slug="computer-use", name="Computer Use", official=False, score=3.8, diff=4,
      cat_en="Automation", cat_fr="Automatisation",
      typ_en="local stdio (npx)", typ_fr="local stdio (npx)",
      auth_en="none", auth_fr="aucune",
      cout_en="Free", cout_fr="Gratuit",
      url="npx -y computer-use-mcp",
      r_en="Real desktop control: mouse, keyboard, screenshots — the agent operates the machine like a user.",
      r_fr="Contrôle réel du poste : souris, clavier, captures d'écran — l'agent opère le bureau comme un utilisateur.",
      f_en=["Move/click the mouse","Type on the keyboard","See the screen and react"],
      f_fr=["Déplacer/cliquer la souris","Taper au clavier","Voir l'écran et réagir"],
      ex=[("Click that button in the native app","GUI action without API","Clique sur tel bouton de l'appli native","action GUI sans API"),
          ("Open the software and export the report","automation of apps without CLI","Ouvre le logiciel et exporte le rapport","automatisation d'apps sans CLI"),
          ("Read what's on screen","desktop vision","Lis ce qui s'affiche à l'écran","vision du bureau")],
      w_en="⚠️ Powerful: for apps with no API or scriptable interface. Use knowingly — the agent acts on your real machine.",
      w_fr="⚠️ Puissant : pour les applications sans API ni interface scriptable. À utiliser en connaissance de cause — l'agent agit sur votre poste réel."),
 dict(slug="xerj", name="XERJ", official=False, score=4.6, diff=3,
     cat_en="Search & memory", cat_fr="Recherche & mémoire",
     typ_en="local stdio + local node", typ_fr="local stdio + nœud local",
     auth_en="none (--insecure) or ApiKey", auth_fr="aucune (--insecure) ou ApiKey",
     cout_en="Free", cout_fr="Gratuit",
     url="xerj mcp (built into the engine binary)",
     r_en="Rust search engine (ES-compatible) with the MCP server inside the binary: autoindex turns any folder into queryable indices, plus durable agent memory.",
     r_fr="Moteur de recherche Rust (compatible ES) avec le serveur MCP dans le binaire : autoindex rend tout dossier interrogeable, plus une mémoire d'agent durable.",
     f_en=["Index code, docs, logs and PDFs (xerj autoindex)","Definition-first code search over ax-* indices","Long-term agent memory (xerj_memory_*)","Semantic, vector and hybrid search"],
     f_fr=["Indexer code, docs, logs et PDFs (xerj autoindex)","Recherche code « définition d'abord » sur les index ax-*","Mémoire d'agent long terme (xerj_memory_*)","Recherche sémantique, vectorielle et hybride"],
     ex=[("Index this folder then find where login() is defined","autoindex + ranked passage","Indexe ce dossier puis trouve où login() est défini","autoindex + passage classé"),
         ("Remember that prod runs PostgreSQL","stored in the node's memory index","Souviens-toi que la prod utilise PostgreSQL","stocké dans l'index mémoire du nœud"),
         ("Map what's indexed on this node","per-index field map via xerj_map","Cartographie ce qui est indexé sur ce nœud","carte des champs par index via xerj_map")],
     w_en="Retrieval and memory stay local: no per-query API cost, and the agent searches your real files instead of recalling approximations.",
     w_fr="Recherche et mémoire restent en local : aucun coût API par requête, et l'agent fouille vos vrais fichiers au lieu de souvenirs approximatifs."),
]

# i18n keys per server
for s in S:
    k = s["slug"].replace("-","_")
    tr(f"s_{k}_cat", s["cat_en"], s["cat_fr"])
    tr(f"s_{k}_resume", s["r_en"], s["r_fr"])
    tr(f"s_{k}_why", s["w_en"], s["w_fr"])
    tr(f"s_{k}_typ", s["typ_en"], s["typ_fr"])
    tr(f"s_{k}_auth", s["auth_en"], s["auth_fr"])
    tr(f"s_{k}_cout", s["cout_en"], s["cout_fr"])
    for i,(e,f) in enumerate(zip(s["f_en"],s["f_fr"])):
        tr(f"s_{k}_f{i}", e, f)
    for i,(pe,re_,pf,rf) in enumerate(s["ex"]):
        tr(f"s_{k}_ex{i}p", pe, pf); tr(f"s_{k}_ex{i}r", re_, rf)

def di(key, tag=None, cls=None, as_html=False):
    """Wraps translated text with data-i18n."""
    a = f' data-i18n="{key}"' + (' data-i18n-html="1"' if as_html else '')
    if tag:
        c = f' class="{cls}"' if cls else ''
        return f"<{tag}{c}{a}>{html.escape(T[key]['en'])}</{tag}>"
    return a

def stars(x):
    full=int(x); half=(x-full)>=.5
    return "★"*full+("⯨" if half else "")+"☆"*(5-full-(1 if half else 0))

GSC_CODE = "nocbSCyC5NzmpgTq9Kfx1Qlyb-241ZbIsLIIe8kpEl4"  # ← remplacer par votre code Google Search Console

def head(page,title_en,desc_en,url,extra="",title_fr=None,desc_fr=None):
    tr(f"{page}_title", title_en, title_fr or title_en)
    tr(f"{page}_desc", desc_en, desc_fr or desc_en)
    return f"""<!DOCTYPE html>
<html lang="en" data-page="{page}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title_en)}</title>
<meta name="description" content="{html.escape(desc_en)}">
<meta name="google-site-verification" content="{GSC_CODE}">
<script data-goatcounter="https://Catalogue-mcp.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
<link rel="canonical" href="{url}">
<meta property="og:title" content="{html.escape(title_en)}">
<meta property="og:description" content="{html.escape(desc_en)}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta name="robots" content="index,follow,max-image-preview:large">
<meta name="theme-color" content="#0c0c10">
<meta name="color-scheme" content="dark">
<meta name="keywords" content="MCP, Model Context Protocol, MCP servers, MCP server list, MCP catalog, AI agent tools, Trello MCP, GitHub MCP, Playwright MCP, Semgrep MCP, Context7, DeepWiki, Devin MCP, Cursor MCP, Claude MCP, serveurs MCP, protocole MCP">
<meta name="author" content="fjjjuv">
<meta name="generator" content="Catalogue-mcp">
<meta property="og:site_name" content="Catalogue-mcp">
<meta property="og:image" content="{BASE}/og-image.png">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:locale" content="en_US">
<meta property="og:locale:alternate" content="fr_FR">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{html.escape(title_en)}">
<meta name="twitter:description" content="{html.escape(desc_en)}">
<meta name="twitter:image" content="{BASE}/og-image.png">
<link rel="alternate" hreflang="en" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<link rel="alternate" type="text/plain" title="LLMs" href="{BASE}/llms.txt">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
<link rel="icon" type="image/svg+xml" href="{BASE}/logo.svg">
<link rel="apple-touch-icon" href="{BASE}/logo.png">
<link rel="manifest" href="{BASE}/site.webmanifest">
<link rel="stylesheet" href="{BASE}/style.css">
{extra}
</head>
<body>
<header class="site-header"><div class="container nav">
<a class="logo" href="{BASE}/"><img class="logo-icon" src="{BASE}/logo.svg" alt="Catalogue-mcp" width="28" height="28"> Catalogue-mcp</a>
<nav><ul class="nav-links">
<li><a href="{BASE}/" data-i18n="nav_home">Home</a></li>
<li><a href="{BASE}/serveurs.html" data-i18n="nav_servers">Servers</a></li>
<li><a href="{BASE}/comparatif.html" data-i18n="nav_compare">Compare</a></li>
<li><a href="{BASE}/guide.html" data-i18n="nav_guide">Guide</a></li>
</ul></nav>
<div class="nav-actions">
<select class="lang-switch" id="lang-switch" aria-label="Language">
<option value="en">🇬🇧 EN</option><option value="fr">🇫🇷 FR</option>
</select>
<a class="btn btn-secondary" style="padding:.45rem .9rem;font-size:.85rem" href="{REPO}">GitHub ↗</a>
</div>
</div></header>
"""

FOOT = f"""
<footer class="site-footer"><div class="container footer-inner">
<p class="footer-brand"><img src="{BASE}/logo.svg" alt="" width="20" height="20" style="vertical-align:-4px"> <b>Catalogue-mcp</b></p>
<p data-i18n="foot_by" data-i18n-html="1">© <span class="copyright-year"></span> <a href="https://github.com/fjjjuv" rel="me author">fjjjuv</a> (Julien) — France 🇫🇷 · All content free &amp; open source</p>
<p class="footer-links">
<a href="https://github.com/fjjjuv" rel="me">GitHub · fjjjuv</a> ·
<a href="https://fjjjuv.github.io/Mon-porte-folio/#profil">Portfolio</a> ·
<a href="{REPO}" data-i18n="foot_repo">Config repo</a> ·
<a href="{BASE}/llms.txt">llms.txt</a>
</p>
</div></footer>
<button class="back-to-top" id="backTop" aria-label="Top">↑</button>
<script src="{BASE}/i18n.js"></script>
<script src="{BASE}/app.js"></script>
<script>document.addEventListener('DOMContentLoaded',()=>{{const y=new Date().getFullYear();const f=()=>document.querySelectorAll('.copyright-year').forEach(e=>e.textContent=y);f();new MutationObserver(f).observe(document.body,{{childList:true,subtree:true}});}});</script>
</body></html>
"""

import re
def fill_empty_i18n(body):
    """Remplit les éléments data-i18n vides avec le contenu EN (sinon ils restent vides)."""
    def repl(m):
        tag,attrs,key,inner=m.group(1),m.group(2),m.group(3),m.group(4)
        if inner.strip():
            return m.group(0)
        val=T.get(key,{}).get("en","")
        if 'data-i18n-html' in attrs:
            return f"<{tag}{attrs}>{val}</{tag}>"
        return f"<{tag}{attrs}>{html.escape(val)}</{tag}>"
    return re.sub(r'<(\w+)([^>]*?data-i18n="([^"]+)"[^>]*)>(.*?)</\1>',repl,body,flags=re.S)

def write(path,body):
    p=os.path.join(OUT,path); os.makedirs(os.path.dirname(p) or OUT,exist_ok=True)
    open(p,"w",encoding="utf-8").write(fill_empty_i18n(body))

# ============ SERVER PAGES =================================================
def server_page(s):
    k=s["slug"].replace("-","_")
    ld={"@context":"https://schema.org","@type":"SoftwareApplication",
        "name":f"{s['name']} MCP Server","applicationCategory":"DeveloperApplication",
        "description":s["r_en"],"operatingSystem":"Windows, macOS, Linux",
        "offers":{"@type":"Offer","price":"0","priceCurrency":"EUR"},
        "aggregateRating":{"@type":"AggregateRating","ratingValue":str(s["score"]),"bestRating":"5","ratingCount":"1"}}
    bc={"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
        {"@type":"ListItem","position":1,"name":"Catalogue-mcp","item":BASE+"/"},
        {"@type":"ListItem","position":2,"name":"Servers","item":BASE+"/serveurs.html"},
        {"@type":"ListItem","position":3,"name":s["name"],"item":f"{BASE}/serveurs/{s['slug']}.html"}]}
    badge='<span class="badge" data-i18n="official">official</span>' if s['official'] else '<span class="badge" data-i18n="community">community</span>'
    fait="".join(di(f"s_{k}_f{i}","li") for i in range(len(s["f_en"])))
    ex="".join(f'<tr><td>«&nbsp;<span data-i18n="s_{k}_ex{i}p">{html.escape(pe)}</span>&nbsp;»</td><td data-i18n="s_{k}_ex{i}r">{html.escape(re_)}</td></tr>' for i,(pe,re_,_,_) in enumerate(s["ex"]))
    body=head(f"s_{k}",f"{s['name']} — MCP Server: what it does, examples, config | Catalogue-mcp",
              s["r_en"],f"{BASE}/serveurs/{s['slug']}.html",
              f'<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(bc,ensure_ascii=False)}</script>',
              title_fr=f"{s['name']} — Serveur MCP : rôle, exemples, config | Catalogue-mcp",
              desc_fr=s["r_fr"])
    body+=f"""<div class="container page-section">
<p><a href="{BASE}/serveurs.html" data-i18n="back_servers">← All servers</a></p>
<h1 style="margin-bottom:.2em">{s['name']} {badge}</h1>
<p data-i18n="s_{k}_cat" style="color:var(--brand-2);font-weight:600;text-transform:uppercase;font-size:.85em;letter-spacing:.06em">{s['cat_en']}</p>
<p class="lead" style="margin:1rem 0 2rem" data-i18n="s_{k}_resume">{s['r_en']}</p>
<div class="table-wrap"><table>
<tr><th data-i18n="type">Type</th><td><code data-i18n="s_{k}_typ">{s['typ_en']}</code></td></tr>
<tr><th data-i18n="endpoint">Endpoint / command</th><td><code>{html.escape(s['url'])}</code></td></tr>
<tr><th data-i18n="auth">Authentication</th><td data-i18n="s_{k}_auth">{s['auth_en']}</td></tr>
<tr><th data-i18n="cost">Cost</th><td data-i18n="s_{k}_cout">{s['cout_en']}</td></tr>
<tr><th data-i18n="difficulty">Installation</th><td>{difftag(s)}</td></tr>
<tr><th data-i18n="score">Score</th><td><span style="color:#ffd700">{stars(s['score'])}</span> <b>{s['score']}/5</b></td></tr>
</table></div>
<h2 data-i18n="what" style="text-align:left">What it does</h2><ul>{fait}</ul>
<h2 data-i18n="examples" style="text-align:left">Example requests</h2>
<div class="table-wrap"><table><tr><th data-i18n="ask">You ask the agent</th><th data-i18n="result">Result</th></tr>{ex}</table></div>
<h2 data-i18n="why" style="text-align:left">Why it changes the game</h2>
<p data-i18n="s_{k}_why">{s['w_en']}</p>
<h2 data-i18n="config" style="text-align:left">Configuration</h2>
<p><span data-i18n="cfg_intro">Ready-to-use config files…</span>
<a href="{REPO}/tree/main/{s['slug']}/"><code>{s['slug']}/</code> ↗</a></p>
</div>"""+FOOT
    write(f"serveurs/{s['slug']}.html",body)

for s in S: server_page(s)

# ============ INDEX ========================================================
tr("idx_hero","Model Context Protocol, in practice","Le Model Context Protocol, en pratique")
tr("idx_lead","MCP servers are capability plug-ins for your AI agent. Once configured, it acts: reads your Trello boards, pushes to GitHub, drives the browser, scans code security…","Les MCP sont des serveurs de capacités qu'on branche à un agent IA. Une fois configuré, il agit : lit vos boards Trello, pousse sur GitHub, pilote le navigateur, scanne la sécurité du code…")
tr("idx_cta",f"Browse the {len(S)} servers →",f"Explorer les {len(S)} serveurs →")
tr("idx_h2","What is an MCP?","C'est quoi un MCP ?")
tr("idx_p1","The Model Context Protocol is an open standard (Anthropic, 2024) letting an AI agent talk to external tools through one interface. Instead of one integration per tool per AI, you configure an MCP server once — it works with Devin, Cursor, Claude Desktop, VS Code, Codex…","Le Model Context Protocol est un standard ouvert (Anthropic, 2024) qui permet à un agent IA de dialoguer avec des outils externes via une interface unifiée. Au lieu d'une intégration par outil et par IA, on configure un serveur MCP une fois — et il marche avec Devin, Cursor, Claude Desktop, VS Code, Codex…")
tr("idx_p2","Two transports: remote (HTTPS URL, often OAuth) or local stdio (a command like npx launched by the client). Our repo ships one folder per server with the config for each platform.","Deux modes de transport : remote (URL HTTPS, souvent OAuth) ou local stdio (une commande comme npx lancée par le client). Notre dépôt fournit un dossier par serveur avec la config adaptée à chaque plateforme.")
tr("idx_h3",f"Our {len(S)} servers",f"Nos {len(S)} serveurs")
tr("idx_why","Why it changes the game","Pourquoi ça change la vie")
tr("idx_b1","<b>Zero copy-paste</b> — the agent reads/writes directly in your tools (Trello, GitHub…)","<b>Zéro copier-coller</b> — l'agent lit/écrit directement dans vos outils (Trello, GitHub…)")
tr("idx_b2","<b>Ground truth</b> — Context7 and DeepWiki inject real docs: no more outdated answers","<b>Vérité terrain</b> — Context7 et DeepWiki injectent la vraie doc : fini les réponses sur des versions obsolètes")
tr("idx_b3","<b>Continuous security</b> — Semgrep scans while the agent writes","<b>Sécurité continue</b> — Semgrep scanne pendant que l'agent écrit")
tr("idx_b4","<b>Real actions</b> — Playwright browses for real, Computer Use clicks on your desktop","<b>Actions réelles</b> — Playwright navigue pour de vrai, Computer Use clique sur votre bureau")
tr("idx_b5","<b>Memory</b> — the Memory server keeps your preferences across sessions","<b>Mémoire</b> — le serveur Memory fait survivre vos préférences entre les sessions")

cards=""
for s in S:
    k=s["slug"].replace("-","_")
    badge='<span class="badge" data-i18n="official">official</span>' if s['official'] else ''
    cards+=f"""<div class="card reveal"><span style="font-size:.75em;color:var(--brand-2);text-transform:uppercase;letter-spacing:.06em" data-i18n="s_{k}_cat">{s['cat_en']}</span>
<h3><a style="color:var(--text)" href="{BASE}/serveurs/{s['slug']}.html">{s['name']}</a> {badge}</h3>
<p data-i18n="s_{k}_resume" style="color:var(--text-muted);font-size:.93em">{s['r_en']}</p>
<p><span style="color:#ffd700">{stars(s['score'])}</span> <b>{s['score']}/5</b> · <code style="font-size:.8em" data-i18n="s_{k}_typ">{s['typ_en']}</code></p></div>"""

ld_idx={"@context":"https://schema.org","@type":"WebSite","name":"Catalogue-mcp",
 "url":BASE+"/","description":"Explained catalog of MCP servers: roles, examples, ratings, ready-to-use configs.",
 "author":{"@type":"Person","name":"fjjjuv","url":"https://github.com/fjjjuv"},"inLanguage":["en","fr"]}
ld_list={"@context":"https://schema.org","@type":"ItemList","name":"MCP servers catalog",
 "numberOfItems":len(S),"itemListElement":[{"@type":"ListItem","position":i+1,
 "url":f"{BASE}/serveurs/{s['slug']}.html","name":f"{s['name']} MCP Server",
 "description":s["r_en"]} for i,s in enumerate(S)]}
ld_faq={"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
 {"@type":"Question","name":"What is an MCP server?","acceptedAnswer":{"@type":"Answer","text":"A Model Context Protocol server is a standardized plugin that gives an AI agent real tools: reading and writing in Trello, GitHub, browsing the web, scanning code for vulnerabilities, or remembering preferences across sessions."}},
 {"@type":"Question","name":"Are MCP servers free?","acceptedAnswer":{"@type":"Answer","text":"Yes. All 12 servers in this catalog are free to use; remote servers authenticate via OAuth and local servers run through stdio (npx / CLI)."}},
 {"@type":"Question","name":"Which clients support MCP?","acceptedAnswer":{"@type":"Answer","text":"Devin, Cursor, Claude Desktop, VS Code, Codex and Claude Code. Each config file in the Catalogue-mcp repo is named after its target platform."}},
 {"@type":"Question","name":"How do I install an MCP server?","acceptedAnswer":{"@type":"Answer","text":"Copy the JSON/TOML block for your platform into its config file (e.g. mcp_config.json for Devin, .cursor/mcp.json for Cursor), restart the client, then complete OAuth if the server requires it."}}]}
idx=head("idx","Catalogue-mcp · MCP Servers Explained — catalog, examples, ratings","Explained catalog of 13 Model Context Protocol servers: what they do, example requests, ratings, and ready configs for Devin, Cursor, Claude, VS Code, Codex.",BASE+"/",f'<script type="application/ld+json">{json.dumps(ld_idx,ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(ld_list,ensure_ascii=False)}</script><script type="application/ld+json">{json.dumps(ld_faq,ensure_ascii=False)}</script>',title_fr="Catalogue-mcp · Les serveurs MCP expliqués — catalogue, exemples, notes",desc_fr="Catalogue expliqué de 13 serveurs Model Context Protocol : rôle, exemples de demandes, notes et configs prêtes pour Devin, Cursor, Claude, VS Code, Codex.")
idx+=f"""<section class="hero"><div class="container hero-inner">
<img src="{BASE}/logo.svg" alt="Catalogue-mcp" width="88" height="88" style="margin-bottom:1.2rem;filter:drop-shadow(0 8px 24px rgba(56,189,248,.35))">
<h1 data-i18n="idx_hero">Model Context Protocol, in practice</h1>
<p class="lead" data-i18n="idx_lead"></p>
<div class="hero-actions"><a class="btn btn-primary" href="{BASE}/serveurs.html" data-i18n="idx_cta"></a>
<a class="btn btn-secondary" href="{REPO}">Catalogue-mcp ↗</a></div>
<div class="badges"><span class="badge">{len(S)} serveurs</span><span class="badge">FR · EN</span><span class="badge">Devin · Cursor · Claude · VS Code · Codex</span></div>
</div></section>
<div class="container">
<section class="page-section"><h2 data-i18n="idx_h2"></h2>
<p style="max-width:800px;margin:0 auto 1rem" data-i18n="idx_p1"></p>
<p style="max-width:800px;margin:0 auto" data-i18n="idx_p2"></p></section>
<section class="page-section"><h2 data-i18n="idx_why"></h2>
<ul style="max-width:700px;margin:0 auto;list-style:none;padding:0">
<li style="padding:.4rem 0" data-i18n="idx_b1" data-i18n-html="1"></li>
<li style="padding:.4rem 0" data-i18n="idx_b2" data-i18n-html="1"></li>
<li style="padding:.4rem 0" data-i18n="idx_b3" data-i18n-html="1"></li>
<li style="padding:.4rem 0" data-i18n="idx_b4" data-i18n-html="1"></li>
<li style="padding:.4rem 0" data-i18n="idx_b5" data-i18n-html="1"></li>
</ul></section>
<section class="page-section"><h2 data-i18n="idx_h3"></h2>
<div class="feature-grid" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:1rem">{cards}</div></section>
</div>"""+FOOT
write("index.html",idx)

# ============ serveurs.html ================================================
tr("srv_h1","Catalog — MCP servers","Catalogue — serveurs MCP")
tr("srv_intro","Each server has a detail page (usages, example requests, config). The config files live in the Catalogue-mcp repo — one folder per server.","Chaque serveur a sa page détaillée (usages, exemples, config). Les fichiers sont dans le dépôt Catalogue-mcp — un dossier par serveur.")
tr("srv_by_cat","By category","Par catégorie")
rows=""
for s in sorted(S,key=lambda x:(x["cat_en"],x["name"])):
    k=s["slug"].replace("-","_")
    rows+=f"""<tr><td><a href="{BASE}/serveurs/{s['slug']}.html"><b>{s['name']}</b></a></td>
<td data-i18n="s_{k}_cat">{s['cat_en']}</td><td data-i18n="s_{k}_typ">{s['typ_en']}</td>
<td data-i18n="s_{k}_auth">{s['auth_en']}</td>
<td><span style="color:#ffd700">{stars(s['score'])}</span> {s['score']}/5</td>
<td>{'<span class="badge" data-i18n="official">official</span>' if s['official'] else '<span class="badge" data-i18n="community">community</span>'}</td></tr>"""
cats={}
for s in S: cats.setdefault(s["cat_en"],[]).append(s)
catlist="".join(f"<li><b>{c}</b> : "+", ".join(f'<a href="{BASE}/serveurs/{s["slug"]}.html">{s["name"]}</a>' for s in v)+"</li>" for c,v in sorted(cats.items()))
srv=head("srv","All MCP servers — full catalog | Catalogue-mcp","Full catalog of 13 MCP servers: Trello, GitHub, Playwright, Semgrep, Context7, DeepWiki, Memory… role, auth, score, config.",BASE+"/serveurs.html",title_fr="Tous les serveurs MCP — catalogue complet | Catalogue-mcp",desc_fr="Catalogue complet de 13 serveurs MCP : Trello, GitHub, Playwright, Semgrep, Context7, DeepWiki, Memory… rôle, auth, note, config.")
srv+=f"""<div class="container page-section"><h1 data-i18n="srv_h1"></h1>
<p class="section-desc" data-i18n="srv_intro"></p>
<div class="table-wrap"><table><tr><th data-i18n="server">Server</th><th data-i18n="cat">Category</th>
<th data-i18n="type">Type</th><th data-i18n="auth">Authentication</th><th data-i18n="score">Score</th><th></th></tr>{rows}</table></div>
<h2 data-i18n="srv_by_cat" style="text-align:left"></h2><ul>{catlist}</ul></div>"""+FOOT
write("serveurs.html",srv)

# ============ comparatif.html ==============================================
tr("cmp_h1","Comparison","Comparatif")
tr("cmp_intro","Subjective ratings from real use: daily usefulness, tool richness, reliability. Install difficulty: <b>very easy</b> = copy-paste is enough · <b>easy</b> = one simple auth step · <b>medium</b> = a few prerequisites (API key, OAuth scopes) · <b>hard</b> = tricky setup · <b>very hard</b> = homemade tinkering required.","Notes subjectives fondées sur l'usage réel : utilité quotidienne, richesse des outils, fiabilité. Difficulté d'installation : <b>très facile</b> = copier-coller suffisant · <b>facile</b> = une étape d'auth simple · <b>moyen</b> = quelques prérequis (clé API, scopes OAuth) · <b>difficile</b> = setup délicat · <b>très difficile</b> = bidouillage maison requis.")
tr("cmp_start","Where to start?","Par où commencer ?")
tr("cmp_s1",f"<b>First MCP</b> — <a href='{BASE}/serveurs/context7.html'>Context7</a> or <a href='{BASE}/serveurs/deepwiki.html'>DeepWiki</a>: no auth, instant effect on answer quality",f"<b>Premier MCP</b> — <a href='{BASE}/serveurs/context7.html'>Context7</a> ou <a href='{BASE}/serveurs/deepwiki.html'>DeepWiki</a> : aucun auth, effet immédiat sur la qualité")
tr("cmp_s2",f"<b>Productivity</b> — <a href='{BASE}/serveurs/github.html'>GitHub</a> then <a href='{BASE}/serveurs/trello.html'>Trello</a>: the agent acts on your daily tools",f"<b>Productivité</b> — <a href='{BASE}/serveurs/github.html'>GitHub</a> puis <a href='{BASE}/serveurs/trello.html'>Trello</a> : l'agent agit sur vos outils du quotidien")
tr("cmp_s3",f"<b>Security</b> — <a href='{BASE}/serveurs/semgrep.html'>Semgrep</a>: continuous scanning while the agent codes",f"<b>Sécurité</b> — <a href='{BASE}/serveurs/semgrep.html'>Semgrep</a> : scan continu pendant que l'agent code")
tr("cmp_s4",f"<b>Browser</b> — <a href='{BASE}/serveurs/playwright.html'>Playwright</a>: real web testing without writing scripts",f"<b>Navigateur</b> — <a href='{BASE}/serveurs/playwright.html'>Playwright</a> : tests web réels sans écrire de script")
crows="".join(f"""<tr><td><a href="{BASE}/serveurs/{s['slug']}.html">{s['name']}</a></td>
<td><span style="color:#ffd700">{stars(s['score'])}</span> {s['score']}/5</td>
<td>{difftag(s)}</td><td data-i18n="s_{s['slug'].replace('-','_')}_cout">{s['cout_en']}</td>
<td data-i18n="s_{s['slug'].replace('-','_')}_auth">{s['auth_en']}</td></tr>""" for s in sorted(S,key=lambda x:-x['score']))
cmp=head("cmp","MCP servers comparison — ratings, difficulty, cost | Catalogue-mcp","Rated comparison of 13 MCP servers: usefulness, install difficulty, cost, authentication. Which server to install first?",BASE+"/comparatif.html",title_fr="Comparatif des serveurs MCP — notes, difficulté, coût | Catalogue-mcp",desc_fr="Comparatif noté de 13 serveurs MCP : utilité, difficulté d'installation, coût, authentification. Quel serveur installer en premier ?")
cmp+=f"""<div class="container page-section"><h1 data-i18n="cmp_h1"></h1>
<p class="section-desc" data-i18n="cmp_intro" data-i18n-html="1"></p>
<div class="table-wrap"><table><tr><th data-i18n="server">Server</th><th data-i18n="score">Score</th>
<th data-i18n="difficulty">Installation</th><th data-i18n="cost">Cost</th><th data-i18n="auth">Authentication</th></tr>{crows}</table></div>
<h2 data-i18n="cmp_start" style="text-align:left"></h2>
<ul>
<li data-i18n="cmp_s1" data-i18n-html="1"></li>
<li data-i18n="cmp_s2" data-i18n-html="1"></li>
<li data-i18n="cmp_s3" data-i18n-html="1"></li>
<li data-i18n="cmp_s4" data-i18n-html="1"></li>
</ul></div>"""+FOOT
write("comparatif.html",cmp)

# ============ guide.html ===================================================
tr("gd_h1","Guide: understanding & installing an MCP","Guide : comprendre et installer un MCP")
tr("gd_prin","The principle","Le principe")
tr("gd_p1","An MCP server exposes tools (functions) the AI agent can call: list_boards, create_file, browser_navigate… The AI client (Devin, Claude, Cursor…) launches the server at startup and discovers its tools automatically.","Un serveur MCP expose des outils (fonctions) que l'agent IA peut appeler : list_boards, create_file, browser_navigate… Le client IA (Devin, Claude, Cursor…) lance le serveur au démarrage et découvre ses outils automatiquement.")
tr("gd_rl","Remote vs local","Remote vs local")
tr("gd_launch","Launch","Lancement"); tr("gd_launch_r","already hosted, just a URL","déjà hébergé, juste une URL")
tr("gd_launch_l","npx/binary command run by the client","commande npx/binaire exécutée par le client")
tr("gd_auth_r","often OAuth (browser) or API key","souvent OAuth (navigateur) ou clé API")
tr("gd_auth_l","usually none — runs on your machine","généralement aucune — tourne sur votre machine")
tr("gd_devin","Install on Devin","Installer sur Devin")
tr("gd_devin_p","Merge into %APPDATA%\\devin\\mcp_config.json under mcpServers:","Fusionner dans %APPDATA%\\devin\\mcp_config.json sous mcpServers :")
tr("gd_devin_p2","Restart Devin → the server shows in active MCPs. On Windows prefer cmd.exe /c npx when npx isn't found.","Redémarrer Devin → le serveur apparaît dans les MCP actifs. Sous Windows, préférer cmd.exe /c npx quand npx n'est pas trouvé.")
tr("gd_plat","Other platforms","Les autres plateformes")
tr("gd_file","File","Fichier"); tr("gd_key","Root key","Clé racine")
tr("gd_pit","Pitfalls (real experience)","Pièges rencontrés (vrai vécu)")
tr("gd_pit1","<b>Trello OAuth</b>: the generic consent fails → relaunch with explicit scopes (read:board:trello write:board:trello…)","<b>OAuth Trello</b> : le consentement générique échoue → relancer avec les scopes explicites (read:board:trello write:board:trello…)")
tr("gd_pit2","<b>Windows + npx</b>: GUI apps don't always find npx in PATH → use cmd.exe /c npx or the binary's absolute path","<b>Windows + npx</b> : l'app graphique ne trouve pas toujours npx dans le PATH → utiliser cmd.exe /c npx ou le chemin absolu")
tr("gd_pit3","<b>Auto-disabled server</b>: a startup failure adds \"disabled\": true to the config — check it","<b>Serveur auto-désactivé</b> : un échec de démarrage ajoute \"disabled\": true à la config — vérifiez-la")
tr("gd_pit4","<b>Absolute path sometimes required</b>: e.g. Semgrep — full semgrep.exe path rather than semgrep","<b>Chemin absolu parfois requis</b> : ex. Semgrep — semgrep.exe complet plutôt que semgrep")
tr("gd_sec","Security","Sécurité")
tr("gd_sec1","Never commit tokens/secrets in configs — use environment variables","Ne jamais commiter de token/secret dans les configs — utiliser des variables d'environnement")
tr("gd_sec2","A local MCP runs with YOUR rights: computer-use really clicks, semgrep reads your files","Un MCP local tourne avec VOS droits : computer-use clique réellement, semgrep lit vos fichiers")
tr("gd_sec3","OAuth = revocable token: prefer it over hardcoded keys","OAuth = jeton révocable : préférez-le aux clés en dur")

gd=head("gd","Guide — what is MCP and how to install a server | Catalogue-mcp","Understand the Model Context Protocol: how it works, remote vs stdio, and install an MCP server on Devin, Cursor, Claude Desktop, VS Code and Codex.",BASE+"/guide.html",title_fr="Guide — c'est quoi le MCP et comment installer un serveur | Catalogue-mcp",desc_fr="Comprendre le Model Context Protocol : fonctionnement, remote vs stdio, et installer un serveur MCP sur Devin, Cursor, Claude Desktop, VS Code et Codex.")
gd+=f"""<div class="container page-section"><h1 data-i18n="gd_h1"></h1>
<h2 data-i18n="gd_prin" style="text-align:left"></h2><p data-i18n="gd_p1"></p>
<h2 data-i18n="gd_rl" style="text-align:left"></h2>
<div class="table-wrap"><table><tr><th></th><th>Remote (HTTPS)</th><th>Local (stdio)</th></tr>
<tr><td><b data-i18n="gd_launch">Launch</b></td><td data-i18n="gd_launch_r"></td><td data-i18n="gd_launch_l"></td></tr>
<tr><td><b data-i18n="auth">Authentication</b></td><td data-i18n="gd_auth_r"></td><td data-i18n="gd_auth_l"></td></tr>
<tr><td><b>Exemples</b></td><td>Trello, GitHub, DeepWiki, Exa</td><td>Playwright, Memory, Semgrep, Context7</td></tr></table></div>
<h2 data-i18n="gd_devin" style="text-align:left"></h2>
<p data-i18n="gd_devin_p"></p>
<pre>{{<br>&nbsp;&nbsp;"mcpServers": {{<br>&nbsp;&nbsp;&nbsp;&nbsp;"trello": {{ "url": "https://mcp.trello.com/v1", "transport": "http" }},<br>&nbsp;&nbsp;&nbsp;&nbsp;"memory": {{ "command": "npx", "args": ["-y", "@modelcontextprotocol/server-memory"] }}<br>&nbsp;&nbsp;}}<br>}}</pre>
<p data-i18n="gd_devin_p2"></p>
<h2 data-i18n="gd_plat" style="text-align:left"></h2>
<div class="table-wrap"><table><tr><th>Plateforme</th><th data-i18n="gd_file">File</th><th data-i18n="gd_key">Root key</th></tr>
<tr><td>Cursor</td><td><code>.cursor/mcp.json</code></td><td><code>mcpServers</code></td></tr>
<tr><td>Claude Desktop</td><td><code>claude_desktop_config.json</code></td><td><code>mcpServers</code></td></tr>
<tr><td>VS Code</td><td><code>.vscode/mcp.json</code></td><td><code>servers</code> + <code>type</code></td></tr>
<tr><td>Codex</td><td><code>~/.codex/config.toml</code></td><td><code>[mcp_servers.*]</code></td></tr>
<tr><td>Claude Code</td><td>via CLI</td><td><code>claude mcp add</code></td></tr></table></div>
<h2 data-i18n="gd_pit" style="text-align:left"></h2><ul>
<li data-i18n="gd_pit1" data-i18n-html="1"></li>
<li data-i18n="gd_pit2" data-i18n-html="1"></li>
<li data-i18n="gd_pit3" data-i18n-html="1"></li>
<li data-i18n="gd_pit4" data-i18n-html="1"></li></ul>
<h2 data-i18n="gd_sec" style="text-align:left"></h2><ul>
<li data-i18n="gd_sec1"></li><li data-i18n="gd_sec2"></li><li data-i18n="gd_sec3"></li></ul>
</div>"""+FOOT
write("guide.html",gd)

# ============ i18n.js ======================================================
d={lang:{k:v[lang] for k,v in T.items()} for lang in ("en","fr")}
i18n=f"""(function(){{
'use strict';
const I18N={json.dumps(d["fr"],ensure_ascii=False)};
const D=document.documentElement;
function apply(lang){{
 if(lang==='fr'){{
  document.querySelectorAll('[data-i18n]').forEach(el=>{{
   const t=I18N[el.dataset.i18n];
   if(t!==undefined){{ if(el.dataset.i18nHtml) el.innerHTML=t; else el.textContent=t; }}
  }});
  const m=document.querySelector('meta[name="description"]');
 }} else {{
  location.reload(); // restore EN originals
  return;
 }}
 D.lang=lang;
 localStorage.setItem('mcp-lang',lang);
 const sw=document.getElementById('lang-switch'); if(sw) sw.value=lang;
}}
document.addEventListener('DOMContentLoaded',()=>{{
 const sw=document.getElementById('lang-switch');
 const saved=localStorage.getItem('mcp-lang')||'en';
 if(sw){{ sw.value=saved; sw.addEventListener('change',()=>apply(sw.value)); }}
 if(saved==='fr') apply('fr');
}});
}})();"""
# simpler & correct: keep both dicts, swap content (no reload)
i18n=f"""(function(){{
'use strict';
const I18N={json.dumps(d,ensure_ascii=False)};
const ORIG={{}}; // caches english originals per element key
const PAGE=document.documentElement.dataset.page||'';
function apply(lang,store){{
 document.querySelectorAll('[data-i18n]').forEach(el=>{{
  const k=el.dataset.i18n;
  if(!(k in ORIG)) ORIG[k]={{t:el.textContent,h:el.innerHTML}};
  const dict=I18N[lang]||I18N.en;
  const val=(dict[k]!==undefined)?dict[k]:(el.dataset.i18nHtml?ORIG[k].h:ORIG[k].t);
  if(el.dataset.i18nHtml) el.innerHTML=val; else el.textContent=val;
 }});
 const dict=I18N[lang]||I18N.en;
 if(dict[PAGE+'_title']) document.title=dict[PAGE+'_title'];
 const md=document.querySelector('meta[name="description"]');
 if(md&&dict[PAGE+'_desc']) md.setAttribute('content',dict[PAGE+'_desc']);
 document.documentElement.lang=lang;
 if(store) localStorage.setItem('mcp-lang',lang);
 const sw=document.getElementById('lang-switch'); if(sw) sw.value=lang;
}}
function detect(){{
 const saved=localStorage.getItem('mcp-lang');
 if(saved) return saved; // choix explicite de l'utilisateur → priorité
 const nl=(navigator.language||'').toLowerCase();
 return nl.startsWith('fr')?'fr':'en'; // détection auto du navigateur
}}
document.addEventListener('DOMContentLoaded',()=>{{
 const sw=document.getElementById('lang-switch');
 if(sw) sw.addEventListener('change',()=>apply(sw.value,true));
 apply(detect(),false); // applique sans écraser le localStorage
}});
}})();"""
write("i18n.js",i18n)

# ============ app.js =======================================================
app="""(function(){
'use strict';
const bt=document.getElementById('backTop');
if(bt){window.addEventListener('scroll',()=>{bt.classList.toggle('visible',scrollY>400)});
bt.addEventListener('click',()=>scrollTo({top:0,behavior:'smooth'}));}
const io=new IntersectionObserver(es=>es.forEach(e=>{if(e.isIntersecting){e.target.classList.add('visible');io.unobserve(e.target)}}),{threshold:.1});
document.querySelectorAll('.reveal').forEach(el=>io.observe(el));
})();"""
write("app.js",app)

# ============ CSS (reuse flamegraph style + extras) ========================
css=open(os.path.join(HERE,"ref-style.css"),encoding="utf-8").read()
extra="""
/* Catalogue-mcp : palette propre (cyan → indigo) — distincte de prompt-flamegraph */
:root{
  --brand-1:#67e8f9;
  --brand-2:#38bdf8;
  --brand-3:#818cf8;
  --brand-gradient:linear-gradient(135deg,#67e8f9 0%,#38bdf8 50%,#818cf8 100%);
  --accent:#38bdf8;
}
a{color:var(--brand-2)}
.btn-primary{color:#04121f;box-shadow:0 6px 24px rgba(56,189,248,.25)}
.badge{background:rgba(56,189,248,.1);color:var(--brand-2);border-color:rgba(56,189,248,.2)}
.hero::before{background:radial-gradient(circle at 50% 0%,rgba(56,189,248,.16),transparent 60%)}

/* Catalogue-mcp extras */
.page-section{padding:3rem 0}
h1{font-size:2.4rem;font-weight:800;line-height:1.15;margin:0 0 1rem;
background:var(--brand-gradient);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text}
.table-wrap{overflow-x:auto;border:1px solid var(--border);border-radius:var(--radius);margin:1rem 0 2rem;background:var(--surface);box-shadow:var(--shadow)}
table{width:100%;border-collapse:collapse;font-size:.92rem}
th,td{padding:.65rem .9rem;text-align:left;border-bottom:1px solid var(--border);vertical-align:top}
th{background:var(--surface-2);font-weight:600;white-space:nowrap}
tr:last-child td{border-bottom:none}
tbody tr:hover td{background:var(--surface-2)}
.card{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);padding:1.25rem;transition:transform .2s,border-color .2s}
.card:hover{transform:translateY(-3px);border-color:var(--border-strong)}
.card h3{margin:.4rem 0 .6rem;font-size:1.05rem}
ul li{margin:.35rem 0}
.site-footer{border-top:1px solid var(--border);padding:1.5rem 0;color:var(--text-muted);font-size:.85rem;text-align:center}
h1:first-of-type{margin-top:0}
.diff{display:inline-block;border-radius:999px;padding:.15rem .65rem;font-size:.78rem;font-weight:600;border:1px solid}
.d1{color:#3fb950;border-color:#3fb950;background:#3fb95022}
.d2{color:#7ee787;border-color:#7ee787;background:#7ee78718}
.d3{color:#d29922;border-color:#d29922;background:#d2992218}
.d4{color:#f0883e;border-color:#f0883e;background:#f0883e18}
.d5{color:#f85149;border-color:#f85149;background:#f8514918}
"""
write("style.css",css+extra)

# ============ logo + robots + sitemap ======================================
import shutil
shutil.copy(os.path.join(HERE,"logo.svg"), os.path.join(OUT,"logo.svg"))


robots="User-agent: *\nAllow: /\n\n"
for bot in ["GPTBot","ClaudeBot","PerplexityBot","Google-Extended","CCBot","anthropic-ai","OAI-SearchBot","ChatGPT-User"]:
    robots+=f"User-agent: {bot}\nAllow: /\n\n"
robots+=f"Sitemap: {BASE}/sitemap.xml\n"
write("robots.txt",robots)

llms="# Catalogue-mcp\n\n> Bilingual (EN/FR) catalog explaining the 13 Model Context Protocol servers we use: what each does, example requests, difficulty, ratings, and ready-to-use config files for Devin, Cursor, Claude Desktop, VS Code and Codex. All servers are free.\n\n## Servers\n\n"
llms+="\n".join(f"- [{s['name']}]({BASE}/serveurs/{s['slug']}.html): {s['r_en']}" for s in S)
llms+=f"\n\n## Site\n\n- [Home]({BASE}/): what MCP is and why it matters\n- [Catalog]({BASE}/serveurs.html): all 12 servers\n- [Comparison]({BASE}/comparatif.html): ratings, difficulty, where to start\n- [Guide]({BASE}/guide.html): remote vs stdio, per-platform config, pitfalls\n- Config repo: {REPO}\n"
write("llms.txt",llms)
full="# Catalogue-mcp — full reference\n\n"
for s in S:
    full+=f"## {s['name']}\n\n{s['r_en']}\n\n- Type: {s['typ_en']}\n- Endpoint/command: {s['url']}\n- Auth: {s['auth_en']}\n- Cost: {s['cout_en']}\n- Score: {s['score']}/5\n- Page: {BASE}/serveurs/{s['slug']}.html\n- Config folder: {REPO}/tree/main/{s['slug']}/\n\n"
write("llms-full.txt",full)
urls=["/","/serveurs.html","/comparatif.html","/guide.html"]+[f"/serveurs/{s['slug']}.html" for s in S]
import datetime
today=datetime.date.today().isoformat()
sm='<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sm+="".join(f"  <url><loc>{BASE}{u}</loc><lastmod>{today}</lastmod></url>\n" for u in urls)+"</urlset>\n"
write("sitemap.xml",sm)

# ============ og-image + apple-touch-icon (PNG) ============================
from PIL import Image, ImageDraw
try:
    from PIL import ImageFont
except ImportError:
    ImageFont=None

def make_og(path):
    W,H=1200,630
    img=Image.new("RGB",(W,H),(12,12,16))
    d=ImageDraw.Draw(img)
    d.rectangle([0,H-12,W,H],fill=(88,166,255))
    f_big=ImageFont.load_default(64) if ImageFont else None
    f_sm=ImageFont.load_default(32) if ImageFont else None
    d.text((60,H//2-90),"Catalogue-mcp",fill=(240,240,245),font=f_big)
    d.text((60,H//2+10),"13 MCP servers explained — configs, examples, ratings",
           fill=(160,160,175),font=f_sm)
    d.text((60,H//2+60),"fjjjuv.github.io/Catalogue-mcp",fill=(88,166,255),font=f_sm)
    img.save(path,"PNG")

def make_icon(path):
    img=Image.new("RGB",(180,180),(12,12,16))
    d=ImageDraw.Draw(img)
    d.rectangle([10,10,169,169],outline=(88,166,255),width=6)
    f=ImageFont.load_default(72) if ImageFont else None
    d.text((52,48),"M",fill=(240,240,245),font=f)
    img.save(path,"PNG")

make_og(os.path.join(OUT,"og-image.png"))
make_icon(os.path.join(OUT,"logo.png"))

def make_icon512(path, maskable=False):
    img=Image.new("RGB",(512,512),(12,12,16))
    d=ImageDraw.Draw(img)
    if maskable:
        d.rectangle([86,86,425,425],outline=(88,166,255),width=12)
        f=ImageFont.load_default(140) if ImageFont else None
        d.text((200,170),"M",fill=(240,240,245),font=f)
    else:
        d.rectangle([28,28,483,483],outline=(88,166,255),width=16)
        f=ImageFont.load_default(200) if ImageFont else None
        d.text((148,136),"M",fill=(240,240,245),font=f)
    img.save(path,"PNG")

make_icon512(os.path.join(OUT,"icon-512.png"))
make_icon512(os.path.join(OUT,"icon-512-maskable.png"), maskable=True)

def make_screenshot(path, w, h):
    img=Image.new("RGB",(w,h),(12,12,16))
    d=ImageDraw.Draw(img)
    d.rectangle([0,0,w,64],fill=(20,20,28))
    d.ellipse([20,22,40,42],fill=(88,166,255))
    f_h=ImageFont.load_default(24) if ImageFont else None
    f_t=ImageFont.load_default(48) if ImageFont else None
    f_s=ImageFont.load_default(20) if ImageFont else None
    d.text((56,18),"Catalogue-mcp",fill=(240,240,245),font=f_h)
    d.text((60,h//2-70),"Model Context Protocol, in practice",
           fill=(240,240,245),font=f_t)
    d.text((60,h//2+10),"13 MCP servers explained: what they do, "
           "example requests, ratings, ready configs.",
           fill=(160,160,175),font=f_s)
    cols=min(4,w//320)
    cardw=(w-60-(cols-1)*20)//cols
    for i in range(cols):
        x=60+i*(cardw+20)
        d.rectangle([x,h-220,x+cardw,h-80],outline=(60,60,75),width=2)
        d.rectangle([x+16,h-190,x+cardw-16,h-170],fill=(40,40,52))
        d.rectangle([x+16,h-155,x+cardw-60,h-140],fill=(30,30,40))
        d.rectangle([x+16,h-125,x+cardw-90,h-110],fill=(30,30,40))
    img.save(path,"PNG")

make_screenshot(os.path.join(OUT,"screenshot-wide.png"),1280,720)
make_screenshot(os.path.join(OUT,"screenshot-mobile.png"),540,960)

manifest={
 "id":BASE+"/",
 "name":"Catalogue-mcp — MCP Servers Explained",
 "short_name":"Catalogue-mcp",
 "description":"Explained catalog of 13 Model Context Protocol servers: configs, examples, ratings.",
 "start_url":BASE+"/",
 "scope":BASE+"/",
 "display":"standalone",
 "display_override":["window-controls-overlay","standalone"],
 "background_color":"#0c0c10",
 "theme_color":"#0c0c10",
 "icons":[
  {"src":BASE+"/logo.png","sizes":"180x180","type":"image/png"},
  {"src":BASE+"/icon-512.png","sizes":"512x512","type":"image/png","purpose":"any"},
  {"src":BASE+"/icon-512-maskable.png","sizes":"512x512","type":"image/png","purpose":"maskable"},
 ],
 "screenshots":[
  {"src":BASE+"/screenshot-wide.png","sizes":"1280x720","type":"image/png",
   "form_factor":"wide","label":"Catalogue-mcp — catalog of 13 MCP servers"},
  {"src":BASE+"/screenshot-mobile.png","sizes":"540x960","type":"image/png",
   "label":"Catalogue-mcp on mobile"},
 ],
}
write("site.webmanifest",json.dumps(manifest,ensure_ascii=False,indent=2))
print("OK — fichiers:",sum(len(f) for _,_,f in os.walk(OUT)))
