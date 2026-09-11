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

| Plugin                           | Bereich                                                                 | Voraussetzung                         |
| -------------------------------- | ----------------------------------------------------------------------- | ------------------------------------- |
| `knowledgecenter-gutachten`      | Gutachten, Aktenvermerke, Protokolle, Stellungnahmen                    | Gutachten-Modul im Abo                |
| `knowledgecenter-energieausweis` | Energieausweis-Projekte: Bauteile, Fenster, Konstruktionen, Ecotech-XML | Energieausweis-Modul im Abo           |
| `knowledgecenter-buero-branding` | Büroprofil, Briefpapier und Kontaktdaten                                | Owner-Konto                           |
| `knowledgecenter-zeiterfassung`  | Ausschließlich eigene Arbeitszeiten starten, beenden und korrigieren    | Persönliches Owner-Konto in Version 1 |
| `knowledgecenter-eingangsrechnungen` | Eingangsrechnungen prüfen, Fälligkeiten, Auswertungen und Zahlungsvermerke | Owner-Konto mit Eingangsrechnungs-Modul |

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
claude plugin install knowledgecenter-energieausweis@entrich-technologies
claude plugin install knowledgecenter-zeiterfassung@entrich-technologies
claude plugin install knowledgecenter-eingangsrechnungen@entrich-technologies
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
codex plugin add knowledgecenter-energieausweis@entrich-technologies
codex plugin add knowledgecenter-zeiterfassung@entrich-technologies
codex plugin add knowledgecenter-eingangsrechnungen@entrich-technologies
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
Server-Adresse des gewünschten Bereichs eintragen:

- Gutachten: `https://www.knowledgecenter.at/api/mcp/gutachten`
- Energieausweis: `https://www.knowledgecenter.at/api/mcp/energieausweis`
- Zeiterfassung: `https://www.knowledgecenter.at/api/mcp/zeiterfassung`
- Eingangsrechnungen (nach Web-Bereitstellung): `https://www.knowledgecenter.at/api/mcp/eingangsrechnungen`

ChatGPT öffnet anschließend die Anmeldung bei Knowledge Center.

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

## Plugin „knowledgecenter-energieausweis"

Energieausweis-Projekte lesen und aktualisieren: Stammdaten, Konstruktionen
(Bauteilkatalog), Bauteilflächen, Fenster/Türen und ihre Zuordnung zu Wänden,
Prüfsummen gegen den Ausweis, Ecotech-XML. Der Skill bringt Lesehilfen für
Ausweise von ETU, GEQ, ArchiPHYSIK und Ecotech mit, damit Claude einen alten
Ausweis (PDF) direkt in ein Projekt übernehmen kann.

MCP-Verbindung zu `https://www.knowledgecenter.at/api/mcp/energieausweis`
(OAuth wie beim Gutachten-Plugin, eine Anmeldung gilt für alle Bereiche).

| Werkzeug                     | Zweck                                                                                                       |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `ea_projekte_suchen`         | Projekte finden (Name, Straße, Ort, Status)                                                                 |
| `ea_projekt_lesen`           | Kompletter Stand mit Adressen `[bauteil:id]`, `[fenster:id]`, `[konstruktion:id]`, Prüfsummen und Warnungen |
| `ea_pruefsummen`             | Hülle, Fensterfläche, Stückzahl, BGF, Richtungspaare, Lücken                                                |
| `ea_projekt_anlegen`         | Neues Projekt                                                                                               |
| `ea_projekt_aktualisieren`   | Stammdaten, Anlage-Grunddaten, Status, Notizen — nur übergebene Felder                                      |
| `ea_konstruktionen_setzen`   | Konstruktionen anlegen/ändern, löschen nur ausdrücklich                                                     |
| `ea_bauteile_setzen`         | Bauteilflächen anlegen/ändern (Typ, Fläche, Richtung, Neigung, Nachbar, U-Wert, Konstruktion)               |
| `ea_fenster_setzen`          | Fenster/Türen anlegen/ändern (Breite × Höhe, U, g, Glasanteil, Richtung)                                    |
| `ea_zuordnungen_setzen`      | Fenster an Wände mit Stückzahl; „ersetzen" nur nach Rückfrage                                               |
| `ea_konstruktionen_ableiten` | Zauberstab: Konstruktionen aus Flächen gruppieren, Vorschau oder anwenden                                   |
| `ea_export_xml`              | Ecotech-XML, Link 24 h gültig, mit Mengen-Meldungen                                                         |

## Sicherheit

- Zugriff nur auf den eigenen Account (Owner); Anmeldungen und Keys sind
  jederzeit in Knowledge Center widerrufbar.
- Finalisierte Gutachten sind schreibgeschützt. Überschreibende Aktionen
  verlangen eine ausdrückliche Bestätigung.
- Bei Verlust eines Geräts oder Keys: auf der Claude-Zugänge-Seite widerrufen.

## Plan aus Grundrissen (Energieausweis)

Mit `ea_plan_lesen`, `ea_plan_vorschau` und `ea_plan_speichern` lässt sich
der erste Geschossplan aus im Chat gelesenen Grundrissen anlegen. Geschosse,
Außenkonturen, Höhen, Nordrichtung und Quellen werden gespeichert. Die
Webplattform zeigt daraus die bearbeitbare Planzeichnung und Plan-3D.
Der Erstimport überschreibt keine vorhandenen Planstände. Fenster und Außentüren
werden anschließend mit `ea_plan_oeffnungen_vorschau/speichern` ergänzt.

Ab Version 0.1.6 öffnet `ea_plan_3d_anzeigen` das gespeicherte Gebäude direkt
im Chat als interaktive Ansicht: drehen, zoomen, Ansichten wechseln und Ebenen
ausblenden. Fenster und Außentüren stammen aus denselben Plandaten wie im Web.
Die Ansicht ist lesend; nach Planänderungen erneut aufrufen. Benötigt einen
Client mit MCP-UI-Unterstützung. Für die 3D-Anzeige ist keine neue SQL-Migration
nötig; der aktualisierte Webserver muss einschließlich UI-Datei veröffentlicht sein.

Version 0.1.5 ergänzt folgende Aktionen:

| Werkzeug                                                       | Zweck                                                                                                                                      |
| -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `ea_plan_bearbeiten_vorschau` / `ea_plan_bearbeiten_speichern` | Fenster/Türen verschieben, ändern, löschen; Wandpunkte, Höhe, Maßstab, Norden und Nachbarn ändern; Dokument mit geprüfter Passung zuordnen |
| `ea_plan_bild`                                                 | Beschriftetes 2D-Planbild mit Wand-, Punkt- und Öffnungsreferenzen; auch für einen ungespeicherten Entwurf                                 |
| `ea_plan_datei_hochladen`                                      | PDF/PNG/JPEG/WebP aus ChatGPT als Projektdokument hochladen, maximal 20 MB                                                                 |
| `ea_plan_dokumente_lesen`                                      | Dokumente und Ebenenzuordnungen lesen; Originaldatei, Seite und Rendermaße abrufen                                                         |
| `ea_plan_baukoerper_vorschau` / `ea_plan_baukoerper_speichern` | Geometrie ohne Duplikate in einen leeren Baukörper übernehmen oder einen reinen Plugin-Planbestand ausdrücklich ersetzen                   |

Je Ebene können eine Datei und eine PDF-Seite hinterlegt werden. Nach dem Upload
die Passung aus Maßstab und Bezugspunkt prüfen und separat zuordnen; bestehende
Gebäudeabmessungen und Geschosslage bleiben dabei erhalten. Dateiübergabe nutzt
[OpenAI-Dateiparameter](https://developers.openai.com/plugins/reference#define-file-inputs).
Alternativ im Web unter Dokumente hochladen und die Dokument-ID verwenden.
Geneigte Dächer, Innenhöfe, Innentüren und Dachfenster sind nicht enthalten.

Voraussetzung im Web-Repository: zuerst `sql/20260909_energy_plan_mcp.sql`
(sofern noch nicht vorhanden), dann `sql/20260909_energy_plan_edit.sql` und
`sql/20260909_energy_plan_transfer.sql` anwenden und den zugehörigen Webserver
bereitstellen. Beide neuen RPCs sind nur für den Service-Account ausführbar.
Ein Plugin-Update allein aktiviert die Server-Werkzeuge nicht. Danach Aktionen
in ChatGPT aktualisieren und in einem neuen Chat testen. Der MCP-Endpunkt bleibt
`https://www.knowledgecenter.at/api/mcp/energieausweis`.

## Plugin „knowledgecenter-buero-branding"

Version 0.1.0 ergänzt die vorhandene Seite **Büro-Branding** um einen MCP-Zugang.
Das Plugin liest und ändert dieselben zentralen Einstellungen: Firmenname,
Untertitel, Adresse, Telefon, E-Mail, Website, Logo-URL und Alternativtext,
Fußzeile, geschäftliche Pflichtangaben, Standard-Unterzeichner und Akzentfarbe.

| Werkzeug                   | Zweck                                                  |
| -------------------------- | ------------------------------------------------------ |
| `buero_branding_lesen`     | Büroprofil und fehlende Angaben lesen                  |
| `buero_branding_vorschau`  | Änderungen ohne Speichern prüfen und Prüfcode erhalten |
| `buero_branding_speichern` | Geprüfte Änderungen auf Nutzerauftrag speichern        |

MCP-Endpunkt: `https://www.knowledgecenter.at/api/mcp/buero-branding`.
Benötigt ein Owner-Konto; kein zusätzliches Fachmodul-Abo. Die Verbindung
arbeitet ausschließlich im angemeldeten Account. Nicht genannte Branding-Felder
und andere Account-Einstellungen bleiben erhalten. Zwischenzeitliche Änderungen
werden beim Speichern erkannt. Eine Datenbankmigration ist nicht erforderlich.

**Bereitstellung:** Zuerst den zugehörigen Webserver-Code veröffentlichen.
Die eigene ChatGPT-App `asdk_app_6aa19df282948191a5e5269bf20a5745` ist in
`knowledgecenter-buero-branding/.app.json` hinterlegt und über
`"apps": "./.app.json"` im Codex-Manifest verknüpft. Nach Veröffentlichung des
Plugin-Pakets in ChatGPT importieren beziehungsweise aktualisieren und mit dem
richtigen Kundenaccount anmelden. Die App muss den obigen MCP-Endpunkt verwenden.

Diese erste Version übernimmt Logo-URLs, keine Bilddateien. Die Vorschau ist
ein Vergleich der Angaben; die visuelle Briefkopf-Vorschau bleibt auf der
Büro-Branding-Seite. Ein Vorschau-PDF, Vorlagenänderungen und ein automatischer
Transfer zwischen Kundenaccounts sind nicht enthalten.

## Versionen

- **Eingangsrechnungen 0.2.0** — zwölf Werkzeuge: Belegupload mit automatischer
  Erfassung und Statusabfrage, Originalbeleg ansehen sowie Suche, Lesen, Prüfung,
  Fälligkeiten/Skonto und vollständige Auswertungen; Rechnungskorrekturen und
  Zahlungsvermerke jeweils mit Vorschau und Konfliktschutz. Owner-Zugang,
  Feature-Flag `invoice_incoming`, nur der eigene Rechnungsbestand.
  Uploads nutzen den vorhandenen Eingangskorb mit `document_processing` und
  Monatskontingent. PDF-/Bildanhänge bis 10 MB; Wiederholungen mit derselben
  Auftrags-ID legen keinen zweiten Beleg an. Bezahlt-Status mit Zahlungsdatum,
  Zahlungsart optional. Icon: 256 × 256 Pixel, unter 10 KB.
  Keine neue SQL-Migration. Zuerst Webserver bereitstellen, dann Plugin-Paket.
  Die registrierte ChatGPT-App ist über `.app.json` im Codex-Manifest verknüpft.

- **Zeiterfassung 0.1.0** — sechs Werkzeuge für eigene `time_sessions`:
  `zeit_status`, `zeit_lesen`, `zeit_starten`, `zeit_beenden`, `zeit_nachtragen`,
  `zeit_korrigieren`. Auch Owner können keine fremden Zeiten bearbeiten.
  Vor Bereitstellung die Web-Migration `20260910_mcp_time_sessions.sql` ausführen.
  Die eigene ChatGPT-App `asdk_app_6aa33b8b80588191841b79ce9e327d14` ist über
  `.app.json` im Codex-Manifest verknüpft. Das Icon hat
  256 × 256 Pixel und ist kleiner als 10 KB. Keine Änderungen an `time_entries`
  oder den Verwaltungsrechten der Web-Oberfläche.

- **Energieausweis 0.1.7** — vermeidet doppelte Prüfsummenaufrufe: nach einer
  Änderung entweder den vollständigen Projektstand inklusive Prüfsummen oder
  nur die Prüfsummen lesen. Web bündelt Katalogänderungen und Zugangsprüfung;
  geprüfte Plandateimetadaten werden je Storage-Version wiederverwendet.
- **Energieausweis 0.1.6** — interaktive 3D-Ansicht im Chat mit Drehen,
  Maus-/Touch-Zoom, Ansichtswechsel und ein-/ausblendbaren Ebenen.

- **Energieausweis 0.1.5** — bestehende Zeichnungen bearbeiten, beschriftete
  Planbilder, Originalpläne je Ebene und kontrollierte Baukörper-Übernahme.

- **Energieausweis 0.1.4** — erster Geschossplan über MCP: lesen, Vorschau,
  initial speichern; Quellenbelege und gleiche Geometrie für Plan/3D.

- **Energieausweis 0.1.0** — lesen, aktualisieren, Prüfsummen, Konstruktionen
  ableiten und Ecotech-XML; jetzt auch mit ChatGPT- und Codex-Verpackung;
  Skill mit Hersteller-Lesehilfen

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
