# Knowledge Center — Plugins für Claude, ChatGPT und Codex

Je Bereich von Knowledge Center ein Plugin, passend zum Abo. Jedes Plugin
spricht den Endpunkt seines Bereichs an (`/api/mcp/<bereich>`) und bringt das
Arbeitsablauf-Wissen des Bereichs als Skill mit. Eine Anmeldung gilt für alle
Bereiche.

Dieselbe Knowledge-Center-Funktion liegt in zwei getrennten Verpackungen im
selben Plugin-Ordner: Claude Code liest `.claude-plugin/`, ChatGPT und Codex
lesen `.codex-plugin/`. Die registrierte ChatGPT-App steht in `.app.json`.
Lediglich die MCP-Verbindung (`.mcp.json`), der Skill (`skills/`) und die Assets
sind gemeinsam — der Server und der fachliche Arbeitsablauf sind dieselben.

| Plugin                      | Bereich                                              | Voraussetzung          |
| --------------------------- | ---------------------------------------------------- | ---------------------- |
| `knowledgecenter-gutachten` | Gutachten, Aktenvermerke, Protokolle, Stellungnahmen | Gutachten-Modul im Abo |

Weitere Bereiche (z. B. Angebote, Baustellen) folgen als eigene Plugins.

## Plugin „knowledgecenter-gutachten"

Gutachten, Aktenvermerke, Protokolle und Stellungnahmen suchen, lesen und
aus einem Diktat befüllen — nach den Regeln, die im jeweiligen Template
hinterlegt sind.

### Plattform-Verpackungen

- **Claude Code:** `.claude-plugin/plugin.json` beschreibt ausschließlich das
  Claude-Code-Plugin. Claude Code entdeckt die gemeinsame MCP-Konfiguration und
  den Skill im Plugin-Ordner.
- **ChatGPT und Codex:** `.codex-plugin/plugin.json` enthält die Oberfläche und
  verweist ausdrücklich auf Skill, MCP-Konfiguration und `.app.json`.
  `.app.json` ordnet das Plugin der registrierten ChatGPT-App zu.

Beide Verpackungen bleiben bewusst im selben Ordner, damit es nur eine
MCP-Konfiguration und eine fachliche Arbeitsanleitung zu pflegen gibt.

## Installation in Claude Code

```bash
# 1. Marketplace hinzufügen (dieses Repository)
claude plugin marketplace add ET-Technologies/knowledgecenterplugins

# 2. Plugin des Bereichs installieren
claude plugin install knowledgecenter-gutachten@entrich-technologies
```

Dann einfach eine Frage stellen, z. B. _„Welche Gutachten-Typen gibt es?"_.
Beim ersten Aufruf öffnet sich der Browser: bei Knowledge Center anmelden,
„Zulassen" klicken — fertig. Kein Key, keine Umgebungsvariable. Die
Anmeldung gilt für alle Bereiche und ist in Knowledge Center jederzeit
widerrufbar (Einstellungen → Claude-Zugänge (MCP)).

Falls die Anmeldung nicht von selbst erscheint: in Claude Code `/mcp`
eingeben und `knowledgecenter-gutachten` authentifizieren.

### Ohne Browser (Automatisierung, CI)

Statt der Anmeldung einen API-Key verwenden (Knowledge Center →
Einstellungen → Claude-Zugänge (MCP), nur Owner):

```bash
claude mcp add --transport http knowledgecenter-gutachten \
  https://www.knowledgecenter.at/api/mcp/gutachten \
  --header "Authorization: Bearer kc_…"
```

## Installation in Codex

```bash
# 1. Marketplace hinzufügen (dieses Repository)
codex plugin marketplace add https://github.com/ET-Technologies/knowledgecenterplugins.git

# 2. Plugin des Bereichs installieren
codex plugin add knowledgecenter-gutachten@entrich-technologies
```

Beim ersten Aufruf meldet sich Codex bei Knowledge Center an (OAuth im
Browser) — dieselbe Anmeldung wie bei Claude, jederzeit widerrufbar.

## Installation in ChatGPT

**Business / Enterprise (Workspace):** Der Workspace-Admin importiert dieses
Repository unter _Workspace-Einstellungen → Plugins → Add → Import marketplace_.
Der Workspace übernimmt Änderungen täglich (oder sofort mit _Sync now_).
Mitglieder aktivieren das Plugin und melden sich beim ersten Aufruf bei
Knowledge Center an.

**Einzelkonto:** In ChatGPT unter _Einstellungen → Security and login_ den
_Developer mode_ einschalten, dann unter _Plugins_ mit dem Plus die
Server-Adresse `https://www.knowledgecenter.at/api/mcp/gutachten` eintragen.
ChatGPT öffnet die Anmeldung bei Knowledge Center.

Hinweis: ChatGPT zeigt Bilder aus Werkzeug-Antworten nicht an; `foto_ansehen`
und `fotos_uebersicht` sind dort ohne Bild. Fotos kommen über den
Upload-Link (`foto_upload_link`) ins Gutachten, Bildunterschriften setzt der
Benutzer dort per Antippen.

## Alternative: claude.ai (Browser, Handy)

Ohne Plugin, über einen Konnektor: In claude.ai unter **Einstellungen →
Konnektoren → Benutzerdefinierten Konnektor hinzufügen** die URL
`https://www.knowledgecenter.at/api/mcp` eintragen — dieser Endpunkt
liefert alle Bereiche, die der Account im Abo hat. Die Anmeldung läuft
über Knowledge Center (OAuth), ein Key ist nicht nötig. Der Skill aus diesem
Plugin steht dort nicht zur Verfügung; die Regeln des Templates liefert der
Server trotzdem mit.

## Was das Plugin enthält

```
knowledgecenter-gutachten/
  .claude-plugin/plugin.json   Manifest für Claude Code
  .codex-plugin/plugin.json    Manifest für ChatGPT und Codex
  .app.json                    ChatGPT: Verweis auf die registrierte App (asdk_app_…)
  .mcp.json                    MCP-Verbindung (gemeinsam)
  skills/gutachten-arbeiten/   Skill (gemeinsam, Agent-Skills-Standard)
  assets/                      Logo und Icon für das Plugin-Verzeichnis
```

Marketplace-Dateien: `.claude-plugin/marketplace.json` (Claude Code) und
`.agents/plugins/marketplace.json` (ChatGPT und Codex).

- **MCP-Verbindung** zu `https://www.knowledgecenter.at/api/mcp/gutachten`
  mit Anmeldung im Browser (OAuth). Es stecken keine Zugangsdaten im Plugin.
- **Skill „gutachten-arbeiten"**: clientneutrale Kurzfassung. Die vollständige
  Arbeitsanleitung liefert der Server beim Verbinden — für alle Clients gleich.
  Die wichtigsten Regeln stehen zusätzlich in den Werkzeugbeschreibungen,
  damit auch Clients ohne Server-Anleitung sie kennen.
- **Werkzeug-Annotations** (`readOnlyHint` u. a.) liefert der Server mit —
  ChatGPT fragt damit nur bei schreibenden Werkzeugen nach.

## Werkzeuge

| Werkzeug                    | Zweck                                                                                   |
| --------------------------- | --------------------------------------------------------------------------------------- |
| `gutachten_typen_auflisten` | Templates mit Abschnitten, Feldern und Regeln                                           |
| `gutachten_suchen`          | Gutachten finden (Titel, Nummer, Typ, Status)                                           |
| `gutachten_lesen`           | Vollständiger Inhalt mit Feldadressen und Regeln                                        |
| `adressbuch_suchen`         | Kunden, Lieferanten, Ansprechpartner, Mitarbeiter                                       |
| `foto_ansehen`              | Foto als Bild (verkleinert) — zum Ansehen und Beschriften                               |
| `gutachten_anlegen`         | Neues Gutachten zu einem Template                                                       |
| `gutachten_befuellen`       | Mehrere Felder in einem Aufruf — der Standardweg aus dem Diktat                         |
| `feld_setzen`               | Einzelne Korrektur                                                                      |
| `foto_beschriften`          | Bildunterschrift setzen, Foto einem Abschnitt/Eintrag zuordnen                          |
| `fotos_uebersicht`          | Kontaktabzug: bis zu 20 Fotos als nummeriertes Raster in einem Bild                     |
| `fotos_zuordnen`            | Viele Fotos in einem Aufruf zuordnen und beschriften                                    |
| `foto_upload_link`          | Kurzlebiger Link, über den der Benutzer neue Fotos hochlädt (Handy/Browser)             |
| `gutachten_fotos_hochladen` | Nur ChatGPT: im Chat angehängte Fotos direkt ins Gutachten übernehmen (Datei-Parameter) |
| `gutachten_auswerten`       | Server-KI wie der Knopf „Transkript auswerten" (nur auf Wunsch)                         |
| `pdf_erzeugen`              | Fertiges PDF, Link 24 h gültig                                                          |

Welche Templates und Abschnitte über MCP erreichbar sind, legt der
Administrator im Template fest (MCP-Zugriff: kein / nur lesen / lesen und
schreiben; einzelne Abschnitte „nicht über MCP").

## Sicherheit

- Zugriff nur auf den eigenen Account (Owner); Anmeldungen und Keys sind
  jederzeit in Knowledge Center widerrufbar.
- Finalisierte Gutachten sind schreibgeschützt. Überschreibende Aktionen
  verlangen eine ausdrückliche Bestätigung.
- Bei Verlust eines Geräts oder Keys: auf der Claude-Zugänge-Seite widerrufen.

## Versionen

- **0.7.1** — Plattform-Verpackungen klarer getrennt; Foto-Upload im gemeinsamen
  Skill clientneutral beschrieben; automatische Repository-Validierung

- **0.7.0** — Verpackung für ChatGPT und Codex (`.codex-plugin`,
  `.agents/plugins/marketplace.json`, Assets); Server liefert Titel und
  Annotations je Werkzeug

- **0.6.0** — Viele Fotos auf einmal: Kontaktabzug (`fotos_uebersicht`),
  Sammelaufruf (`fotos_zuordnen`), einheitliche Fotonamen bei Link-Uploads

- **0.5.0** — Neue Fotos über `foto_upload_link` (Upload-Seite ohne
  App-Login, Link 2 Stunden gültig)

- **0.4.0** — Anmeldung im Browser statt API-Key; Arbeitsanleitung kommt
  vom Server

- **0.3.0** — Ein Plugin je Bereich (`knowledgecenter-gutachten`), eigener
  Endpunkt `/api/mcp/gutachten`, Abo-Prüfung durch den Server

- **0.2.0** — Befüllen durch Claude (`gutachten_befuellen`), Adressbuch,
  Fotos ansehen und beschriften, Regeln des Templates in den
  Werkzeug-Antworten, MCP-Zugriff pro Template
- **0.1.0** — Lesen, Diktat über Server-KI, Felder setzen, PDF

© Entrich Technologies GmbH. Nutzung für Kunden von Knowledge Center.
