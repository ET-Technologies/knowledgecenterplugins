---
name: gutachten-arbeiten
description: Gutachten, Aktenvermerke, Protokolle und Stellungnahmen in Knowledge Center — suchen, lesen, aus Diktat befüllen, Fotos hochladen lassen und beschriften, PDF. Nutzen, sobald der Benutzer nach solchen Dokumenten oder deren Inhalten fragt oder eines anlegen, nachtragen, korrigieren oder als PDF haben will.
---

# Gutachten in Knowledge Center

Der Zugriff läuft über den MCP-Server `knowledgecenter-gutachten`. Die
vollständige Arbeitsanleitung (Werkzeuge, Ablauf „Diktat rein → PDF raus",
Interpretation, Regeln) liefert der Server selbst beim Verbinden — sie ist
für alle Clients gleich und immer aktuell. Halte dich daran.

Kurzfassung:

1. Typ klären, Gutachten lesen oder anlegen, Regeln des Templates beachten.
2. Diktat selbst verstehen und mit `gutachten_befuellen` schreiben —
   Namen und Adressen vorher mit `adressbuch_suchen` klären, bei
   Unklarheit den Benutzer fragen statt raten.
3. Neue Fotos: Bietet der Client ein Werkzeug für direkt angehängte Dateien an,
   dieses verwenden. Andernfalls `foto_upload_link` erzeugen und dem Benutzer
   zeigen. Bei vielen Fotos danach `fotos_uebersicht` (Kontaktabzug) und
   `fotos_zuordnen` (alles in einem Aufruf) statt Foto für Foto.
4. Vor jeder Schreibaktion: der Benutzer muss sie gewollt haben.

## Einrichtung in Claude Code (falls der Server nicht verbunden ist)

Beim ersten Aufruf öffnet Claude Code die Anmeldung bei Knowledge Center im
Browser (OAuth, nur für Owner-Konten). Danach ist die Verbindung aktiv.
Falls die Anmeldung nicht angeboten wird: `/mcp` in Claude Code eingeben und
`knowledgecenter-gutachten` authentifizieren.

Für Automatisierungen ohne Browser: API-Key aus Knowledge Center
(Einstellungen → Claude-Zugänge (MCP), nur Owner) und den Server manuell mit
Header eintragen:

```bash
claude mcp add --transport http knowledgecenter-gutachten \
  https://www.knowledgecenter.at/api/mcp/gutachten \
  --header "Authorization: Bearer kc_…"
```

## Einrichtung in ChatGPT und Codex

Die jeweilige Plattform-Verpackung stellt dieselbe MCP-Verbindung bereit. Beim
ersten Aufruf die Anmeldung bei Knowledge Center durchführen. In ChatGPT kann
außerdem das clienteigene Werkzeug für angehängte Fotos verfügbar sein; nur
dort ist der direkte Datei-Upload dem Upload-Link vorzuziehen.
