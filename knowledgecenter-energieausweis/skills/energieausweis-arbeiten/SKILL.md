---
name: energieausweis-arbeiten
description: Energieausweis-Projekte in Knowledge Center — suchen, lesen, Stammdaten, Bauteile, Fenster, Konstruktionen und Zuordnungen aktualisieren, Prüfsummen gegen den Ausweis rechnen, Ecotech-XML erzeugen, einen alten Ausweis (PDF) in ein Projekt übernehmen. Nutzen, sobald der Benutzer nach Energieausweisen, Gebäudehülle, Bauteilen, Fenstern, U-Werten oder Ecotech fragt oder einen Ausweis anlegen, nachtragen oder korrigieren will.
---

# Energieausweis in Knowledge Center

Der Zugriff läuft über den MCP-Server `knowledgecenter-energieausweis`. Die
vollständige Arbeitsanleitung (Werkzeuge, Ablauf, Vokabular, Regeln) liefert
der Server beim Verbinden — für alle Clients gleich. Halte dich daran.

Kurzfassung:

1. `ea_projekte_suchen` → `ea_projekt_lesen`. Stand und Warnungen kurz
   zusammenfassen; die Adressen `[bauteil:id]`, `[fenster:id]`,
   `[konstruktion:id]` sind die Referenzen für alle Änderungen.
2. Änderungen vor dem Schreiben kurz zeigen, dann die `*_setzen`-Werkzeuge:
   mit id ändern (nur übergebene Felder), ohne id neu anlegen. Gelöscht wird
   nur, was ausdrücklich in `loeschen` steht — nach Rückfrage.
3. Konstruktionen fehlen: `ea_konstruktionen_ableiten` als Vorschau, dann
   nach Rückfrage mit `anwenden=true`.
4. Nach jedem Schreiben `ea_pruefsummen`; Lücken benennen (Nachbar bei
   Decken, fehlende Zuordnung, fehlende Konstruktion, Richtungspaar), nicht
   selbst füllen. Nichts erfinden, Richtungen nie raten.
5. `ea_export_xml` nur auf Wunsch; die Meldungen des Exports wiedergeben.

## Alten Ausweis (PDF) übernehmen

Wenn der Benutzer ein EA-PDF schickt, liest du es selbst und schreibst die
Daten mit den Werkzeugen (Reihenfolge: Projekt → Konstruktionen → Bauteile →
Fenster → Zuordnungen → Prüfsummen). Wo im Ausweis welche Werte stehen und
welche Fallen es je Hersteller gibt, steht in
`references/lesehilfen-hersteller.md` — vor dem Lesen eines Ausweises öffnen.
Prüfsummen vor dem Schreiben: Hülle, Fensterfläche, Richtungspaare, BGF.

## Einrichtung in Claude Code (falls der Server nicht verbunden ist)

Beim ersten Aufruf öffnet Claude Code die Anmeldung bei Knowledge Center im
Browser (OAuth, nur für Owner-Konten mit Energieausweis-Modul). Falls die
Anmeldung nicht angeboten wird: `/mcp` eingeben und
`knowledgecenter-energieausweis` authentifizieren.

Für Automatisierungen ohne Browser: API-Key aus Knowledge Center
(Einstellungen → MCP-Zugänge (Claude), nur Owner) und den Server manuell mit
Header eintragen:

```bash
claude mcp add --transport http knowledgecenter-energieausweis \
  https://www.knowledgecenter.at/api/mcp/energieausweis \
  --header "Authorization: Bearer kc_…"
```
