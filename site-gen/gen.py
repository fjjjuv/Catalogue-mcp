# -*- coding: utf-8 -*-
"""Génère le site GitHub Pages pour mcp-configs (statique, SEO + GEO)."""
import os, json, html

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "out")
os.makedirs(OUT, exist_ok=True)

BASE = "https://fjjjuv.github.io/catalogue-mcp"
REPO = "https://github.com/fjjjuv/mcp-configs"

# ---- Données des 12 serveurs --------------------------------------------
S = [
 dict(slug="trello", name="Trello", cat="Gestion de projet", official=True,
      typ="remote (HTTPS)", auth="OAuth 2.0", score=4.8, diff=3, cout="Gratuit",
      url="https://mcp.trello.com/v1",
      resume="Le serveur MCP officiel d'Atlassian pour Trello : l'agent lit et écrit vos boards, listes, cartes, checklists et commentaires.",
      fait=["Lister les boards et workspaces", "Créer/déplacer/compléter des cartes", "Gérer listes, checklists, étiquettes, dates", "Commenter, chercher, consulter l'inbox"],
      exemples=[("Migre mon projet Asana vers Trello", "crée le board, les listes et les cartes en préservant descriptions et échéances"),
                ("Quelles cartes sont en retard ?", "scanne les due dates et résume"),
                ("Ajoute une carte 'Tests' dans En cours avec checklist", "création directe")],
      pourquoi="Gestion de projet pilotée par le chat : plus besoin d'ouvrir Trello pour mettre à jour les tâches — l'agent s'en charge pendant qu'il code."),
 dict(slug="asana", name="Asana", cat="Gestion de projet", official=True,
      typ="remote (HTTPS)", auth="OAuth 2.0", score=4.5, diff=2, cout="Gratuit",
      url="https://mcp.asana.com/v2/mcp",
      resume="Le MCP officiel Asana : accès aux projets, tâches, sections et commentaires du workspace.",
      fait=["Énumérer projets et tâches", "Lire descriptions, sections, échéances", "Mettre à jour et compléter des tâches", "Rechercher dans tout le workspace"],
      exemples=[("Liste mes tâches de la semaine", "vue consolidée sans ouvrir Asana"),
                ("Quelles tâches du projet X sont bloquées ?", "analyse des sections"),
                ("Prépare la migration vers Trello", "export complet des projets")],
      pourquoi="Idéal pour extraire et réorganiser un projet existant — c'est ce qui a servi à la migration Asana→Trello."),
 dict(slug="github", name="GitHub MCP Server", cat="Développement", official=True,
      typ="remote (HTTPS)", auth="OAuth / PAT", score=5.0, diff=2, cout="Gratuit",
      url="https://api.githubcopilot.com/mcp",
      resume="Le serveur officiel de GitHub (46 outils) : lecture et écriture sur les repos — fichiers, commits, branches, issues, PR, releases, recherche de code.",
      fait=["Lire/modifier des fichiers sans cloner le repo", "Créer branches, commits, PR et releases", "Lire et répondre aux issues et reviews", "Rechercher du code dans toute l'org"],
      exemples=[("Crée un fichier README dans mcp-configs", "push_files direct via l'API"),
                ("Liste les PR ouvertes et résume les reviews", "état du projet en une phrase"),
                ("Cherche où la fonction X est utilisée", "search_code cross-repo")],
      pourquoi="L'agent manipule le dépôt distant sans checkout local — commits, PR et releases pilotés en conversation."),
 dict(slug="context7", name="Context7", cat="Documentation", official=False,
      typ="local stdio (npx)", auth="aucune", score=4.7, diff=1, cout="Gratuit",
      url="npx -y @upstash/context7-mcp@1.0.31",
      resume="Injecte dans le contexte la documentation à jour des bibliothèques — versions réelles, exemples officiels.",
      fait=["Récupérer la doc officielle d'une lib précise", "Fournir des exemples de code actuels", "Éviter les réponses basées sur des versions obsolètes"],
      exemples=[("Utilise Next.js 15 — use context7", "l'agent lit la doc officielle récente"),
                ("Comment marque onUploadProgress dans axios ?", "exemple officiel injecté"),
                ("Montre l'API PySide6 QTableWidget", "doc Qt à jour")],
      pourquoi="Réduit les hallucinations : l'agent cite la vraie doc de la bonne version au lieu de réciter sa mémoire."),
 dict(slug="exa-code", name="Exa Code", cat="Recherche", official=False,
      typ="remote (HTTPS)", auth="clé API Exa", score=4.2, diff=3, cout="Freemium",
      url="https://mcp.exa.ai/mcp",
      resume="Recherche web sémantique orientée code : trouve des exemples, libs et docs pertinents au-delà des mots-clés.",
      fait=["Rechercher des exemples de code réels", "Trouver des bibliothèques adaptées à un besoin", "Explorer des docs et discussions techniques"],
      exemples=[("Trouve des exemples de ByteTrack + ONNX Runtime", "résultats sémantiques ciblés"),
                ("Quelles libs OCR pour plaques FR existent ?", "recherche augmentée"),
                ("Compare les frameworks ALPR récents", "veille technique")],
      pourquoi="Complète la recherche classique quand le besoin est flou ou très spécifique — la sémantique trouve ce que les mots-clés ratent."),
 dict(slug="deepwiki", name="DeepWiki", cat="Documentation", official=False,
      typ="remote (HTTPS)", auth="aucune", score=4.6, diff=1, cout="Gratuit",
      url="https://mcp.deepwiki.com/mcp",
      resume="Documentation IA des dépôts GitHub : structure wiki générée, explications d'architecture, questions-réponses sur un codebase.",
      fait=["Lire la structure wiki d'un repo", "Poser des questions sur un projet GitHub", "Comprendre vite un code inconnu"],
      exemples=[("Explique l'architecture de fast-plate-ocr", "réponse fondée sur le vrai code"),
                ("Comment ce projet gère-t-il l'auth ?", "wiki généré à la demande"),
                ("Liste les modules principaux de ce repo", "vue d'ensemble instantanée")],
      pourquoi="Comprendre un repo open source en 2 minutes au lieu d'une heure de lecture — parfait pour évaluer une dépendance."),
 dict(slug="cloudflare-docs", name="Cloudflare Docs", cat="Documentation", official=True,
      typ="remote (HTTPS)", auth="aucune", score=4.0, diff=1, cout="Gratuit",
      url="https://docs.mcp.cloudflare.com/mcp",
      resume="Accès direct à la documentation officielle Cloudflare : Workers, Pages, R2, DNS, sécurité.",
      fait=["Rechercher dans la doc Cloudflare", "Guides pas à pas Workers/Pages", "Réponses fondées sur les docs à jour"],
      exemples=[("Comment déployer un Worker avec R2 ?", "doc officielle directement"),
                ("Configure un redirect 301 sur Pages", "syntaxe exacte _redirects"),
                ("Quelles limites gratuites pour Workers ?", "chiffres officiels")],
      pourquoi="Si vous hébergez chez Cloudflare, l'agent répond avec la doc officielle, pas avec des souvenirs approximatifs."),
 dict(slug="playwright", name="Playwright", cat="Navigateur", official=True,
      typ="local stdio (npx)", auth="aucune", score=4.9, diff=1, cout="Gratuit",
      url="npx -y @playwright/mcp@latest",
      resume="Automatisation navigateur complète : l'agent navigue, clique, remplit, extrait et photographie des pages web.",
      fait=["Naviguer et interagir avec des sites réels", "Captures d'écran et snapshots d'accessibilité", "Remplir des formulaires, tester des parcours", "Vérifier qu'une app web fonctionne visuellement"],
      exemples=[("Ouvre mon app et vérifie que le login marche", "test E2E conversationnel"),
                ("Fais une capture de la page en mobile", "screenshot device-émulation"),
                ("Remplis le formulaire et valide", "automatisation sans script")],
      pourquoi="L'agent teste vos applications web comme un humain — navigation réelle, pas juste des requêtes HTTP."),
 dict(slug="puppeteer", name="Puppeteer", cat="Navigateur", official=True,
      typ="local stdio (npx)", auth="aucune", score=4.3, diff=1, cout="Gratuit",
      url="npx -y @modelcontextprotocol/server-puppeteer",
      resume="Automatisation Chrome via le protocole DevTools : navigation, screenshots, exécution JavaScript dans la page.",
      fait=["Piloter une instance Chrome", "Exécuter du JS dans la page", "Captures d'écran et extraction DOM"],
      exemples=[("Screenshot de la page d'accueil", "capture rapide"),
                ("Exécute ce script dans la page", "JS dans le vrai contexte du site"),
                ("Vérifie que le bouton est visible", "assertion DOM")],
      pourquoi="Alternative légère à Playwright centrée Chrome — utile quand on veut scripter directement dans la page."),
 dict(slug="computer-use", name="Computer Use", cat="Automatisation", official=False,
      typ="local stdio (npx)", auth="aucune", score=3.8, diff=4, cout="Gratuit",
      url="npx -y computer-use-mcp",
      resume="Contrôle réel du poste : souris, clavier, captures d'écran — l'agent opère le bureau comme un utilisateur.",
      fait=["Déplacer/cliquer la souris", "Taper au clavier", "Voir l'écran et réagir"],
      exemples=[("Clique sur tel bouton de l'appli native", "action GUI sans API"),
                ("Ouvre le logiciel et exporte le rapport", "automatisation d'apps sans CLI"),
                ("Lis ce qui s'affiche à l'écran", "vision du bureau")],
      pourquoi="⚠️ Puissant : pour les applications sans API ni interface scriptable. À utiliser en connaissance de cause — l'agent agit sur votre poste réel."),
 dict(slug="memory", name="Memory", cat="Persistance", official=True,
      typ="local stdio (npx)", auth="aucune", score=4.4, diff=1, cout="Gratuit",
      url="npx -y @modelcontextprotocol/server-memory",
      resume="Graphe de connaissances persistant : l'agent mémorise des faits, préférences et relations entre les sessions.",
      fait=["Créer des entités et relations durables", "Se souvenir des préférences utilisateur", "Retrouver des décisions passées"],
      exemples=[("Souviens-toi que je préfère les commits en français", "stocké pour les sessions suivantes"),
                ("Rappelle-moi comment est organisé ce projet", "relecture du graphe"),
                ("Note que le serveur prod utilise PostgreSQL", "mémoire projet")],
      pourquoi="L'agent ne repart pas de zéro à chaque session : conventions, décisions et contexte survivent."),
 dict(slug="semgrep", name="Semgrep", cat="Sécurité", official=False,
      typ="local stdio", auth="aucune", score=4.5, diff=5, cout="Gratuit",
      url="semgrep mcp (CLI locale → serveur MCP)",
      resume="Analyse statique de sécurité transformée en MCP : on a bricolé la CLI `semgrep mcp` pour en faire un serveur.",
      fait=["Scanner du code pour vulnérabilités et secrets", "Vérifier la qualité/sécurité à chaque édition (hooks)", "Écrire des règles custom pour le projet", "Audit supply-chain des dépendances"],
      exemples=[("Scanne le projet pour des failles", "248 règles du registre auto"),
                ("Vérifie ce fichier que tu viens de modifier", "sécurité en continu"),
                ("Écris une règle pour interdire eval()", "règle custom générée")],
      pourquoi="La sécurité devient continue : l'agent détecte et corrige les failles pendant qu'il écrit le code, pas après."),
]

CATS = sorted({s["cat"] for s in S})

# Échelle de difficulté d'installation : 1 = très facile … 5 = très difficile
DIFF = {1:"très facile", 2:"facile", 3:"moyen", 4:"difficile", 5:"très difficile"}

def difftag(s):
    return f'<span class="diff d{s["diff"]}">{DIFF[s["diff"]]}</span>'

# ---- CSS -----------------------------------------------------------------
CSS = """
:root{--bg:#0d1117;--panel:#161b22;--border:#30363d;--txt:#e6edf3;--mut:#8b949e;--acc:#58a6ff;--ok:#3fb950;--warn:#d29922}
*{box-sizing:border-box}body{margin:0;font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;background:var(--bg);color:var(--txt);line-height:1.6}
a{color:var(--acc);text-decoration:none}a:hover{text-decoration:underline}
header{border-bottom:1px solid var(--border);padding:14px 24px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;background:var(--bg);z-index:10}
nav a{margin-left:18px;color:var(--mut)}nav a:hover{color:var(--txt)}
.wrap{max-width:1050px;margin:0 auto;padding:24px}
.hero{text-align:center;padding:56px 20px}
.hero h1{font-size:2.4em;margin:.2em 0}.hero p{color:var(--mut);max-width:640px;margin:0 auto;font-size:1.15em}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(300px,1fr));gap:16px}
.card{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:18px}
.card h3{margin:.2em 0}.card .cat{font-size:.8em;color:var(--acc);text-transform:uppercase;letter-spacing:.05em}
.card p{color:var(--mut);font-size:.93em}
.badge{display:inline-block;background:#1f6feb33;border:1px solid #1f6feb;border-radius:20px;padding:2px 10px;font-size:.75em;color:#79c0ff}
table{width:100%;border-collapse:collapse;margin:16px 0}th,td{border:1px solid var(--border);padding:9px 12px;text-align:left;font-size:.92em}th{background:var(--panel)}
tr:hover td{background:#161b2288}
code{background:#1f242c;padding:2px 6px;border-radius:5px;font-size:.9em}
pre{background:var(--panel);border:1px solid var(--border);border-radius:8px;padding:14px;overflow-x:auto}
.stars{color:#f5c518;letter-spacing:2px}
footer{border-top:1px solid var(--border);margin-top:48px;padding:20px;text-align:center;color:var(--mut);font-size:.85em}
.toc a{display:block;padding:3px 0}
.tag{font-size:.75em;border:1px solid var(--border);border-radius:12px;padding:1px 8px;color:var(--mut);margin-right:6px}
.diff{display:inline-block;border-radius:12px;padding:2px 10px;font-size:.8em;font-weight:600;border:1px solid}
.d1{color:#3fb950;border-color:#3fb950;background:#3fb95022}
.d2{color:#7ee787;border-color:#7ee787;background:#7ee78718}
.d3{color:#d29922;border-color:#d29922;background:#d2992218}
.d4{color:#f0883e;border-color:#f0883e;background:#f0883e18}
.d5{color:#f85149;border-color:#f85149;background:#f8514918}
"""

def head(title, desc, page_url, extra=""):
    t = html.escape(title); d = html.escape(desc)
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="{page_url}">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:type" content="website">
<meta property="og:url" content="{page_url}">
<meta name="robots" content="index,follow">
<link rel="stylesheet" href="{BASE}/style.css">
{extra}
</head>
<body>
<header><a href="{BASE}/" style="color:var(--txt);font-weight:700">🧩 mcp-configs</a>
<nav>
<a href="{BASE}/">Accueil</a>
<a href="{BASE}/serveurs.html">Serveurs</a>
<a href="{BASE}/comparatif.html">Comparatif</a>
<a href="{BASE}/guide.html">Guide</a>
<a href="{REPO}">GitHub ↗</a>
</nav></header>
"""

FOOT = f"""
<footer>Déployé via GitHub Pages depuis la branche <code>gh-pages</code> ·
<a href="{REPO}">dépôt mcp-configs</a> · config MCP — Model Context Protocol</footer>
</body></html>
"""

def stars(x):
    full = int(x); half = (x-full)>=.5
    return "★"*full + ("⯨" if half else "") + "☆"*(5-full-(1 if half else 0))

def write(path, body):
    p = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(p) or OUT, exist_ok=True)
    open(p,"w",encoding="utf-8").write(body)

# ---- page serveur --------------------------------------------------------
def server_page(s):
    ex = "".join(f"<tr><td>« {html.escape(p)} »</td><td>{html.escape(r)}</td></tr>" for p,r in s["exemples"])
    fait = "".join(f"<li>{html.escape(f)}</li>" for f in s["fait"])
    ld = {"@context":"https://schema.org","@type":"SoftwareApplication",
          "name":f"{s['name']} MCP Server","applicationCategory":"DeveloperApplication",
          "description":s["resume"],"operatingSystem":"Windows, macOS, Linux",
          "offers":{"@type":"Offer","price":"0","priceCurrency":"EUR"},
          "aggregateRating":{"@type":"AggregateRating","ratingValue":str(s["score"]),"bestRating":"5","ratingCount":"1"}}
    extra = f'<script type="application/ld+json">{json.dumps(ld,ensure_ascii=False)}</script>'
    body = head(f"{s['name']} — Serveur MCP : usages, config et exemples | mcp-configs",
                s["resume"] + f" Type : {s['typ']}. Note : {s['score']}/5.",
                f"{BASE}/serveurs/{s['slug']}.html", extra)
    body += f"""<div class="wrap">
<p><a href="{BASE}/serveurs.html">← Tous les serveurs</a></p>
<h1>{s['name']} {'<span class="badge">officiel</span>' if s['official'] else '<span class="tag">community</span>'}</h1>
<p class="cat" style="color:var(--acc)">{s['cat']}</p>
<p style="font-size:1.1em">{s['resume']}</p>
<table>
<tr><th>Type</th><td><code>{s['typ']}</code></td></tr>
<tr><th>Endpoint / commande</th><td><code>{html.escape(s['url'])}</code></td></tr>
<tr><th>Authentification</th><td>{s['auth']}</td></tr>
<tr><th>Coût</th><td>{s['cout']}</td></tr>
<tr><th>Installation</th><td>{difftag(s)}</td></tr>
<tr><th>Note</th><td><span class="stars">{stars(s['score'])}</span> {s['score']}/5</td></tr>
</table>
<h2>Ce qu'il permet</h2><ul>{fait}</ul>
<h2>Exemples de demandes</h2>
<table><tr><th>Demande à l'agent</th><th>Résultat</th></tr>{ex}</table>
<h2>En quoi il change la vie</h2>
<p>{s['pourquoi']}</p>
<h2>Configuration</h2>
<p>Les fichiers prêts à l'emploi pour Devin, Cursor, Claude Desktop, VS Code et Codex sont dans le dépôt :
<a href="{REPO}/tree/main/{s['slug']}/"><code>{s['slug']}/</code> sur GitHub ↗</a></p>
</div>""" + FOOT
    write(f"serveurs/{s['slug']}.html", body)

for s in S: server_page(s)

# ---- index ---------------------------------------------------------------
cards = "".join(f"""<div class="card"><span class="cat">{s['cat']}</span>
<h3><a href="{BASE}/serveurs/{s['slug']}.html" style="color:var(--txt)">{s['name']}</a> {'<span class="badge">officiel</span>' if s['official'] else ''}</h3>
<p>{html.escape(s['resume'])}</p>
<p><span class="stars">{stars(s['score'])}</span> <b>{s['score']}/5</b> · <span class="tag">{s['typ']}</span></p></div>""" for s in S)
ld_idx = {"@context":"https://schema.org","@type":"TechArticle",
 "headline":"Catalogue de serveurs MCP (Model Context Protocol)",
 "description":"Un dossier par serveur MCP : configs prêtes pour Devin, Cursor, Claude, VS Code, Codex + explications et notes.",
 "author":{"@type":"Person","name":"fjjjuv"},
 "about":{"@type":"Thing","name":"Model Context Protocol"}}
idx = head("Catalogue MCP — 12 serveurs Model Context Protocol expliqués et configurés | mcp-configs",
           "Catalogue de serveurs MCP : ce qu'ils font, à quoi ils servent, exemples, notes, et fichiers de config prêts pour Devin, Cursor, Claude Desktop, VS Code et Codex.",
           BASE+"/", f'<script type="application/ld+json">{json.dumps(ld_idx,ensure_ascii=False)}</script>')
idx += f"""<div class="hero">
<h1>🧩 Model Context Protocol, en pratique</h1>
<p>Les MCP sont des <b>serveurs de capacités</b> qu'on branche à un agent IA. Une fois configuré, l'agent peut agir : lire vos boards Trello, pousser sur GitHub, piloter le navigateur, scanner la sécurité de votre code…</p>
<p style="margin-top:14px"><a class="badge" href="{BASE}/serveurs.html" style="font-size:1em;padding:8px 18px">Voir les {len(S)} serveurs →</a></p>
</div>
<div class="wrap">
<h2>C'est quoi un MCP ?</h2>
<p>Le <b>Model Context Protocol</b> est un standard ouvert (Anthropic, 2024) qui permet à un agent IA de
dialoguer avec des outils externes via une interface unifiée. Au lieu de coder une intégration par outil et par
IA, on configure un serveur MCP une fois — et il marche avec Devin, Cursor, Claude Desktop, VS Code, Codex…</p>
<p>Deux modes de transport : <b>remote</b> (URL HTTPS, souvent OAuth) ou <b>local stdio</b> (une commande comme
<code>npx</code> lancée par le client). Notre dépôt fournit un dossier par serveur avec la config adaptée à chaque plateforme.</p>
<h2>Les {len(S)} serveurs de notre setup</h2>
<div class="grid">{cards}</div>
<h2>Pourquoi ça change la vie</h2>
<ul>
<li><b>Zéro copier-coller</b> : l'agent lit/écrit directement dans vos outils (Trello, GitHub…)</li>
<li><b>Vérité terrain</b> : Context7 et DeepWiki injectent la vraie doc — fini les réponses sur des versions obsolètes</li>
<li><b>Sécurité continue</b> : Semgrep scanne pendant que l'agent écrit</li>
<li><b>Actions réelles</b> : Playwright navigue pour de vrai, Computer Use clique sur votre bureau</li>
<li><b>Mémoire</b> : le serveur Memory fait survivre vos préférences entre les sessions</li>
</ul>
</div>""" + FOOT
write("index.html", idx)

# ---- serveurs.html -------------------------------------------------------
rows = "".join(f"""<tr><td><a href="{BASE}/serveurs/{s['slug']}.html"><b>{s['name']}</b></a></td><td>{s['cat']}</td>
<td>{s['typ']}</td><td>{s['auth']}</td><td><span class="stars">{stars(s['score'])}</span> {s['score']}/5</td>
<td>{'<span class="badge">officiel</span>' if s['official'] else '<span class="tag">community</span>'}</td></tr>""" for s in S)
srv = head("Les 12 serveurs MCP — catalogue complet | mcp-configs",
           "Tableau complet des 12 serveurs MCP : Trello, Asana, GitHub, Playwright, Semgrep, Context7, DeepWiki, Memory… rôle, auth, note et config.",
           BASE+"/serveurs.html")
srv += f"""<div class="wrap"><h1>Catalogue — {len(S)} serveurs MCP</h1>
<p>Chaque serveur a sa page détaillée (usages, exemples de demandes, config). Les fichiers sont dans le
<a href="{REPO}">dépôt mcp-configs</a>, un dossier par serveur.</p>
<table><tr><th>Serveur</th><th>Catégorie</th><th>Type</th><th>Auth</th><th>Note</th><th></th></tr>{rows}</table>
<h2>Par catégorie</h2><ul>"""
for c in CATS:
    names = ", ".join(f'<a href="{BASE}/serveurs/{s["slug"]}.html">{s["name"]}</a>' for s in S if s["cat"]==c)
    srv += f"<li><b>{c}</b> : {names}</li>"
srv += "</ul></div>" + FOOT
write("serveurs.html", srv)

# ---- comparatif.html -----------------------------------------------------
cmp_rows = "".join(f"""<tr><td><a href="{BASE}/serveurs/{s['slug']}.html">{s['name']}</a></td>
<td><span class="stars">{stars(s['score'])}</span> {s['score']}/5</td>
<td>{difftag(s)}</td><td>{s['cout']}</td><td>{s['auth']}</td></tr>"""
 for s in sorted(S,key=lambda x:-x['score']))
cmp = head("Comparatif des serveurs MCP — notes, difficulté, coût | mcp-configs",
           "Comparatif noté des 12 serveurs MCP : utilité, facilité d'installation, coût, authentification. Quel serveur installer en premier ?",
           BASE+"/comparatif.html")
cmp += f"""<div class="wrap"><h1>Comparatif</h1>
<p>Notes subjectives fondées sur l'usage réel : utilité quotidienne, richesse des outils, fiabilité.
Difficulté d'installation : <span class="diff d1">très facile</span> = copier-coller suffisant ·
<span class="diff d2">facile</span> = une étape d'auth simple ·
<span class="diff d3">moyen</span> = quelques prérequis (clé API, scopes OAuth) ·
<span class="diff d4">difficile</span> = setup délicat ·
<span class="diff d5">très difficile</span> = bidouillage maison requis.</p>
<table><tr><th>Serveur</th><th>Note globale</th><th>Installation</th><th>Coût</th><th>Auth</th></tr>{cmp_rows}</table>
<h2>Par où commencer ?</h2>
<ul>
<li><b>Premier MCP</b> : <a href="{BASE}/serveurs/context7.html">Context7</a> ou <a href="{BASE}/serveurs/deepwiki.html">DeepWiki</a> — aucun auth, effet immédiat sur la qualité des réponses</li>
<li><b>Productivité</b> : <a href="{BASE}/serveurs/github.html">GitHub</a> puis <a href="{BASE}/serveurs/trello.html">Trello</a> — l'agent agit sur vos outils du quotidien</li>
<li><b>Sécurité</b> : <a href="{BASE}/serveurs/semgrep.html">Semgrep</a> — scan continu pendant que l'agent code</li>
<li><b>Navigateur</b> : <a href="{BASE}/serveurs/playwright.html">Playwright</a> — tests web réels sans écrire de script</li>
</ul></div>""" + FOOT
write("comparatif.html", cmp)

# ---- guide.html ----------------------------------------------------------
gd = head("Guide — c'est quoi le MCP et comment installer un serveur | mcp-configs",
           "Comprendre le Model Context Protocol : fonctionnement, remote vs stdio, et comment installer un serveur MCP sur Devin, Cursor, Claude Desktop, VS Code et Codex.",
           BASE+"/guide.html")
gd += f"""<div class="wrap"><h1>Guide : comprendre et installer un MCP</h1>
<h2>Le principe</h2>
<p>Un <b>serveur MCP</b> expose des <i>outils</i> (functions) que l'agent IA peut appeler : <code>list_boards</code>,
<code>create_file</code>, <code>browser_navigate</code>… Le client IA (Devin, Claude, Cursor…) lance le serveur au
démarrage et découvre ses outils automatiquement.</p>
<h2>Remote vs local</h2>
<table><tr><th></th><th>Remote (HTTPS)</th><th>Local (stdio)</th></tr>
<tr><td>Lancement</td><td>déjà hébergé, juste une URL</td><td>commande <code>npx</code>/binaire exécutée par le client</td></tr>
<tr><td>Auth</td><td>souvent OAuth (navigateur) ou clé API</td><td>généralement aucune — tourne sur votre machine</td></tr>
<tr><td>Exemples</td><td>Trello, GitHub, DeepWiki, Exa</td><td>Playwright, Memory, Semgrep, Context7</td></tr></table>
<h2>Installer sur Devin</h2>
<p>Fusionner dans <code>%APPDATA%\\devin\\mcp_config.json</code> sous <code>mcpServers</code> :</p>
<pre>{{
  "mcpServers": {{
    "trello": {{ "url": "https://mcp.trello.com/v1", "transport": "http" }},
    "memory": {{ "command": "npx", "args": ["-y", "@modelcontextprotocol/server-memory"] }}
  }}
}}</pre>
<p>Redémarrer Devin → le serveur apparaît dans les MCP actifs. Sous Windows, préférer
<code>"command": "cmd.exe", "args": ["/c", "npx", "-y", "..."]</code> quand <code>npx</code> n'est pas trouvé.</p>
<h2>Les autres plateformes</h2>
<table><tr><th>Plateforme</th><th>Fichier</th><th>Clé racine</th></tr>
<tr><td>Cursor</td><td><code>.cursor/mcp.json</code></td><td><code>mcpServers</code></td></tr>
<tr><td>Claude Desktop</td><td><code>claude_desktop_config.json</code></td><td><code>mcpServers</code></td></tr>
<tr><td>VS Code</td><td><code>.vscode/mcp.json</code></td><td><code>servers</code> + <code>type</code></td></tr>
<tr><td>Codex</td><td><code>~/.codex/config.toml</code></td><td><code>[mcp_servers.*]</code></td></tr>
<tr><td>Claude Code</td><td>via CLI</td><td><code>claude mcp add</code></td></tr></table>
<h2>Pièges rencontrés (vrai vécu)</h2>
<ul>
<li><b>OAuth Trello</b> : le consentement générique échoue → il faut relancer avec les scopes explicites
(<code>read:board:trello write:board:trello</code>…)</li>
<li><b>Windows + npx</b> : l'app graphique ne trouve pas toujours <code>npx</code> dans le PATH →
utiliser <code>cmd.exe /c npx</code> ou le chemin absolu de l'exécutable</li>
<li><b>Serveur auto-désactivé</b> : un échec de démarrage ajoute <code>"disabled": true</code> à la config — vérifiez-la</li>
<li><b>Chemin absolu requis parfois</b> : ex. Semgrep — <code>semgrep.exe</code> complet plutôt que <code>semgrep</code></li>
</ul>
<h2>Sécurité</h2>
<ul>
<li>Ne jamais commiter de token/secret dans les configs — utiliser des variables d'environnement</li>
<li>Un MCP local tourne avec VOS droits : <code>computer-use</code> clique réellement, <code>semgrep</code> lit vos fichiers</li>
<li>OAuth = jeton révocable : préférez-le aux clés en dur</li>
</ul>
</div>""" + FOOT
write("guide.html", gd)

# ---- style.css, robots, sitemap -----------------------------------------
write("style.css", CSS)
write("robots.txt", f"User-agent: *\nAllow: /\nSitemap: {BASE}/sitemap.xml\n")
urls = ["/", "/serveurs.html", "/comparatif.html", "/guide.html"] + [f"/serveurs/{s['slug']}.html" for s in S]
sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sm += "".join(f"  <url><loc>{BASE}{u}</loc></url>\n" for u in urls) + "</urlset>\n"
write("sitemap.xml", sm)
print("pages générées:", sum(len(files) for _,_,files in os.walk(OUT)))
