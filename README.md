# Knowledge Center — Claude-Plugins

Je Bereich von Knowledge Center ein Plugin, passend zum Abo. Jedes Plugin
spricht den Endpunkt seines Bereichs an (`/api/mcp/<bereich>`) und bringt das
Arbeitsablauf-Wissen des Bereichs als Skill mit. Ein Key gilt für alle Bereiche.

| Plugin | Bereich | Voraussetzung |
|---|---|---|
| `knowledgecenter-gutachten` | Gutachten, Aktenvermerke, Protokolle, Stellungnahmen | Gutachten-Modul im Abo |

Weitere Bereiche (z. B. Angebote, Baustellen) folgen als eigene Plugins.

## Plugin „knowledgecenter-gutachten"

Gutachten, Aktenvermerke, Protokolle und Stellungnahmen suchen, lesen und
aus einem Diktat befüllen — nach den Regeln, die im jeweiligen Template
hinterlegt sind.

## Installation in Claude Code

```bash
# 1. Marketplace hinzufügen (dieses Repository)
claude plugin marketplace add ET-Technologies/knowledgecenter-plugin

# 2. Plugin installieren
claude plugin install knowledgecenter-gutachten@entrich-technologies
```

Windows (PowerShell): dieselben Befehle; die Umgebungsvariable unten mit
`setx KNOWLEDGECENTER_MCP_KEY "kc_…"` setzen und das Terminal neu öffnen.

## API-Key einrichten

1. In Knowledge Center: **Einstellungen → Claude-Zugänge (MCP)** (nur Owner)
2. **Key erzeugen** — „Nur Lesen" für reine Auswertung, sonst „Lesen und Schreiben" — und kopieren
3. Als Umgebungsvariable setzen, z. B. in `~/.zshrc` / `~/.bashrc`:

```bash
export KNOWLEDGECENTER_MCP_KEY=kc_…
```

4. Claude Code neu starten. Test: *„Welche Gutachten-Typen gibt es?"*

## Alternative: claude.ai (Browser, Handy)

Ohne Plugin, über einen Konnektor: In claude.ai unter **Einstellungen →
Konnektoren → Benutzerdefinierten Konnektor hinzufügen** die URL
`https://applications.builddesk.at/api/mcp` eintragen — dieser Endpunkt
liefert alle Bereiche, die der Account im Abo hat. Die Anmeldung läuft
über Knowledge Center (OAuth), ein Key ist nicht nötig. Der Skill aus diesem
Plugin steht dort nicht zur Verfügung; die Regeln des Templates liefert der
Server trotzdem mit.

## Was das Plugin enthält

- **MCP-Verbindung** zu `https://applications.builddesk.at/api/mcp/gutachten`.
  Der Key steckt nicht im Plugin — jeder Benutzer verwendet seinen eigenen.
- **Skill „gutachten-arbeiten"**: Tool-Reihenfolge, Umgang mit Instanzen,
  Fotos und Finalisierung, Regeln für Schreibaktionen.

## Werkzeuge

| Werkzeug | Zweck |
|---|---|
| `gutachten_typen_auflisten` | Templates mit Abschnitten, Feldern und Regeln |
| `gutachten_suchen` | Gutachten finden (Titel, Nummer, Typ, Status) |
| `gutachten_lesen` | Vollständiger Inhalt mit Feldadressen und Regeln |
| `adressbuch_suchen` | Kunden, Lieferanten, Ansprechpartner, Mitarbeiter |
| `foto_ansehen` | Foto als Bild (verkleinert) — zum Ansehen und Beschriften |
| `gutachten_anlegen` | Neues Gutachten zu einem Template |
| `gutachten_befuellen` | Mehrere Felder in einem Aufruf — der Standardweg aus dem Diktat |
| `feld_setzen` | Einzelne Korrektur |
| `foto_beschriften` | Bildunterschrift setzen, Foto einem Abschnitt/Eintrag zuordnen |
| `gutachten_auswerten` | Server-KI wie der Knopf „Transkript auswerten" (nur auf Wunsch) |
| `pdf_erzeugen` | Fertiges PDF, Link 24 h gültig |

Welche Templates und Abschnitte über MCP erreichbar sind, legt der
Administrator im Template fest (MCP-Zugriff: kein / nur lesen / lesen und
schreiben; einzelne Abschnitte „nicht über MCP").

## Sicherheit

- Zugriff nur auf den Account des Key-Besitzers; Keys sind jederzeit in
  Knowledge Center widerrufbar.
- Finalisierte Gutachten sind schreibgeschützt. Überschreibende Aktionen
  verlangen eine ausdrückliche Bestätigung.
- Bei Verlust eines Keys: auf der Claude-Zugänge-Seite widerrufen.

## Versionen

- **0.3.0** — Ein Plugin je Bereich (`knowledgecenter-gutachten`), eigener
  Endpunkt `/api/mcp/gutachten`, Abo-Prüfung durch den Server

- **0.2.0** — Befüllen durch Claude (`gutachten_befuellen`), Adressbuch,
  Fotos ansehen und beschriften, Regeln des Templates in den
  Werkzeug-Antworten, MCP-Zugriff pro Template
- **0.1.0** — Lesen, Diktat über Server-KI, Felder setzen, PDF

© Entrich Technologies GmbH. Nutzung für Kunden von Knowledge Center.
