# Knowledge Center — Plugins für Claude, ChatGPT und Codex

Je Bereich von Knowledge Center ein Plugin, passend zum Abo. Jedes Plugin
spricht den Endpunkt seines Bereichs an (`/api/mcp/<bereich>`) und bringt das
Arbeitsablauf-Wissen des Bereichs als Skill mit. Eine Anmeldung gilt für alle
Bereiche.

Dieselbe Knowledge-Center-Funktion liegt in zwei getrennten Verpackungen im
selben Plugin-Ordner: Claude Code liest `.claude-plugin/`, ChatGPT und Codex
lesen `.codex-plugin/`. Eine registrierte ChatGPT-App wird, soweit vorhanden,
über `.app.json` verknüpft.
Lediglich die MCP-Verbindung (`.mcp.json`), der Skill (`skills/`) und die Assets
sind gemeinsam — der Server und der fachliche Arbeitsablauf sind dieselben.

| Plugin                               | Bereich                                                                          | Voraussetzung                                |
| ------------------------------------ | -------------------------------------------------------------------------------- | -------------------------------------------- |
| `knowledgecenter-gutachten`          | Gutachten, Aktenvermerke, Protokolle, Stellungnahmen                             | Gutachten-Modul im Abo                       |
| `knowledgecenter-energieausweis`     | Energieausweis-Projekte: Bauteile, Fenster, Konstruktionen, Ecotech-XML          | Energieausweis-Modul im Abo                  |
| `knowledgecenter-buero-branding`     | Büroprofil, Briefpapier und Kontaktdaten                                         | Owner-Konto                                  |
| `knowledgecenter-zeiterfassung`      | Ausschließlich eigene Arbeitszeiten starten, beenden und korrigieren             | Persönliches Owner-Konto in Version 1        |
| `knowledgecenter-eingangsrechnungen` | Eingangsrechnungen prüfen, Fälligkeiten, Auswertungen und Zahlungsvermerke       | Owner-Konto mit Eingangsrechnungs-Modul      |
| `knowledgecenter-baustellen`         | Baustellen zusammenfassen, Fotos, Chatnachrichten und neue Aufgaben              | Persönliches Owner-Konto mit Baustellenmodul |
| `knowledgecenter-angebote`           | Angebote berechnen, als Karte prüfen, bearbeiten, freigeben und als PDF erzeugen | Persönliches Owner-Konto mit Angebotsmodul   |

Weitere Bereiche folgen als eigene Plugins.

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
claude plugin install knowledgecenter-baustellen@entrich-technologies
claude plugin install knowledgecenter-angebote@entrich-technologies
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
codex plugin add knowledgecenter-baustellen@entrich-technologies
codex plugin add knowledgecenter-angebote@entrich-technologies
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
- Baustellen (nach Web-Bereitstellung): `https://www.knowledgecenter.at/api/mcp/baustellen`
- Angebote: `https://www.knowledgecenter.at/api/mcp/angebote`

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
| `ea_projekt_aktualisieren`   | Stammdaten, Auftraggeber/Aussteller, Anlage-Grunddaten, Status, Notizen — nur übergebene Felder             |
| `ea_konstruktionen_setzen`   | Konstruktionen anlegen/ändern, löschen nur ausdrücklich                                                     |
| `ea_bauteile_setzen`         | Bauteilflächen anlegen/ändern (Typ, Fläche, Richtung, Neigung, Nachbar, U-Wert, Konstruktion)               |
| `ea_fenster_setzen`          | Fenster/Türen anlegen/ändern (Breite × Höhe, U, g, Glasanteil, Richtung)                                    |
| `ea_zuordnungen_setzen`      | Fenster an Wände mit Stückzahl; „ersetzen" nur nach Rückfrage                                               |
| `ea_konstruktionen_ableiten` | Zauberstab: Konstruktionen aus Flächen gruppieren, Vorschau oder anwenden                                   |
| `ea_export_xml`              | Ecotech-XML, Link 24 h gültig, mit Mengen-Meldungen                                                         |
| `ea_fotos_uebersicht`        | Fotos nach Kategorie mit `[foto:id]`, auch von der Begehung am Handy                                        |
| `ea_foto_ansehen`            | Foto als Bild ansehen (verkleinert) — z. B. Typenschild ablesen, Rahmen/Verglasung erkennen                 |
| `ea_foto_beschriften`        | Beschreibung oder Kategorie eines Fotos ändern                                                              |
| `ea_fotos_hochladen`         | Im Chat angehängte Fotos (ChatGPT) mit Kategorie übernehmen, wiederholbar über `anfrage_id`                 |
| `ea_foto_link`               | Link zur Kamera-Seite der Handy-App (für Claude oder zum Fotografieren vor Ort)                             |
| `ea_anlage_setzen`           | Typenschild, Wärmeabgabe, Kesselart, Aufstellort, Warmwasser, Lüftung, PV/Solar — nur übergebene Felder     |

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

Version 0.1.8 ergänzt weitere Geschosse:

| Werkzeug                                                                     | Zweck                                                                                              |
| ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `ea_plan_geschoss_kopieren_vorschau` / `ea_plan_geschoss_kopieren_speichern` | Vorhandenes Geschoss mit Lage, Nachbarn und wahlweise Fenstern/Türen oben anhängen (z. B. EG → OG) |
| `ea_plan_geschoss_anlegen_vorschau` / `ea_plan_geschoss_anlegen_speichern`   | Geschoss mit eigenem Umriss in Metern oben anhängen (z. B. kleineres Dachgeschoss)                 |

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

## Plugin „knowledgecenter-angebote"

Das Paket enthält die Manifeste für Claude Code sowie ChatGPT/Codex, die
gemeinsame MCP-Verbindung, den Skill `angebote-erstellen` und das Angebotsicon
(256 × 256 Pixel, 6.942 Bytes), das als Icon und Logo eingebunden ist.

| Werkzeug                       | Zweck                                                          |
| ------------------------------ | -------------------------------------------------------------- |
| `kunden_suchen`                | Bestehende Kunden finden und eindeutig auswählen               |
| `kunden_lesen`                 | Kundenadresse, Ansprechpartner und Vertragsrabatt lesen        |
| `kunde_anlegen`                | Neuen Kunden auf Auftrag anlegen                               |
| `kunde_aendern`                | Adresse, Kontakt oder Vertragsrabatt eines Kunden ändern       |
| `produkte_suchen`              | Katalogartikel nach Name oder Artikelnummer finden             |
| `produkt_lesen`                | Katalogpreis, Einheit, Steuer und Preismodus lesen             |
| `produkt_anlegen`              | Neuen Artikel auf Auftrag in den Katalog aufnehmen             |
| `belegarten_auflisten`         | Aktive Belegarten und Standardvorlage anzeigen                 |
| `belegart_lesen`               | Struktur, Textbausteine, Spalten und Darstellung lesen         |
| `angebot_vorschau`             | Angaben prüfen und mit der Web-Logik berechnen, ohne Speichern |
| `angebot_anlegen`              | Geprüftes Angebot auf Auftrag als Entwurf speichern            |
| `angebote_suchen`              | Angebote suchen, nach Status, Kunde, Datum filtern             |
| `angebot_lesen`                | Gespeichertes Angebot mit laufenden Positionsnummern lesen     |
| `angebot_kopie_vorschau`       | Gespeichertes Angebot als Vorlage für ein neues vorbereiten    |
| `angebot_aendern`              | Titel, Datum, Gültigkeit, Notiz oder Kunde ändern              |
| `angebot_position_anlegen`     | Position hinzufügen, optional an einer bestimmten Stelle       |
| `angebot_position_aendern`     | Menge, Preis, Text, Einheit oder Steuer einer Position ändern  |
| `angebot_position_loeschen`    | Position auf ausdrücklichen Auftrag entfernen                  |
| `angebot_position_verschieben` | Reihenfolge ändern, ohne Mengen, Preise oder Summen            |
| `angebot_status_setzen`        | Freigeben und Versand dokumentieren; Nummer kommt vom Server   |
| `angebot_pdf`                  | PDF des gespeicherten Stands als Download-Link erzeugen        |
| `render_angebot_vorschau`      | Vorschau als Karte im Chat, Anlegen direkt aus der Karte       |
| `render_angebot`               | Gespeichertes Angebot als Karte, mit Bearbeiten und Freigeben  |
| `render_angebote_treffer`      | Angebotstreffer als antippbare Liste im Chat                   |
| `render_kunden_treffer`        | Kundentreffer als antippbare Liste im Chat                     |
| `render_kunde`                 | Kundenkarte mit Konditionen und den jüngsten Angeboten         |

Benötigt einen persönlichen Owner-Zugang, das Angebotsmodul (`proposal`) und
Leserecht; zum Anlegen zusätzlich Schreibrecht. Kunden und Produkte werden aus
dem bestehenden Stammdatenbestand gelesen. Das Plugin enthält keine eigene
Datenbank- oder Preislogik. Neue Angebote unterstützen Katalog- und freie
Positionen in EUR, maximal 100 Positionen. Ein positiver Kundenvertragsrabatt
ersetzt Positionsrabatte. Wiederholungen desselben Speicherauftrags verwenden
dieselbe Anfrage-ID und erzeugen keinen zweiten Entwurf.

Gespeicherte Angebote lassen sich im Chat suchen, anzeigen, ändern, freigeben und
als PDF erzeugen. Die Karte kennt vier Ansichten — Vorschau, gespeichertes
Angebot, Trefferliste und Kundenkarte — und tauscht beim Antippen eines Treffers
ihren Inhalt selbst aus, ohne weiteren Werkzeugaufruf. `render_angebote_treffer`
und `render_kunden_treffer` suchen dafür selbst auf dem Server, damit keine vom
Modell erfundenen Treffer in einer Karte landen.

E-Mail-Versand, Löschen, Vorlagenwechsel, zusätzliche Vorlagenfelder, Anhänge und
die Baustellenzuordnung erfolgen weiterhin in der Web-App. Das Plugin verlinkt
den gespeicherten Beleg.

**Stand und Bereitstellung:** Der Webstand mit dem Angebotsbereich ist in
Produktion. Eine Installation ist weiterhin kein Nachweis für einen
erfolgreichen Praxistest: Der Ablauf Kundensuche → Vorschau → Entwurf →
Bearbeiten → Freigabe → PDF und das Antippen in den Trefferlisten gehören vor
der Veröffentlichung einmal durchgespielt. Die obigen
Repository-Installationsbefehle setzen voraus, dass die Paketversion im
verwendeten Marketplace veröffentlicht wurde.

Für Preview die URL in `knowledgecenter-angebote/.mcp.json` auf den tatsächlichen
Preview-Server mit Pfad `/api/mcp/angebote` setzen. Die mitgelieferte URL
`https://www.knowledgecenter.at/api/mcp/angebote` ist die vorgesehene
Produktionsadresse. Preview benötigt eine getrennte Supabase-Testumgebung mit
passenden Umgebungsvariablen und OAuth-Konfiguration. Auch der vom Backend
zurückgegebene Web-Link muss zur Testumgebung gehören; im aktuellen Backend
verwendet er noch die feste Produktionsadresse.

Vor dem passenden Web-Deployment in der gewählten Datenbank zuerst
`20260912_smart_document_atomic_save.sql`, danach
`20260912_smart_document_mcp_create.sql` aus `web/sql/` ausführen. Die SQL-Dateien
unter `web/sql/tests/` sind ausschließlich für eine wegwerfbare Testdatenbank.
Die Prüfung und Ausführung dieser Migrationen ist nicht Teil der
Plugin-Installation.

Die registrierte ChatGPT-App `asdk_app_6aa6e09cd21081918b858eab450d83c9` ist über
`knowledgecenter-angebote/.app.json` und den `apps`-Verweis im Codex-Manifest
verknüpft. Diese Verknüpfung stellt den MCP-Server nicht bereit und ersetzt
nicht die Anmeldung am verbundenen Knowledge-Center-Account.

Bei der Prüfung am 19.09.2026 antwortete der Produktionsendpunkt
`/api/mcp/angebote` ohne Anmeldung mit HTTP 401 und seine
OAuth-Ressourcenmetadaten mit HTTP 200; der Endpunkt ist also erreichbar und
verlangt die Anmeldung. Danach sollte `tools/list` bei freigeschaltetem
Angebotsmodul und Lese-/Schreibrecht die 25 oben genannten Werkzeuge liefern;
mit reinem Leserecht entfallen die schreibenden, darunter `angebot_anlegen`.

Das Plugin arbeitet über Werkzeugaufrufe im Chat; die Karte ersetzt keine
Angebotsübersicht in der Web-App. Als erster Lesetest eignet sich:
„Welche Angebotsvorlagen stehen mir zur Verfügung?“ Für die Karte:
„Zeig mir meine Angebote mit Fenster“ und einen Treffer antippen.

## Versionen

- **Angebote 0.9.2** — Bezeichnung nur bei freien Positionen änderbar
  (`katalog: true` bei Katalogartikeln); Löschen und Stornieren fragen vorher nach.

- **Angebote 0.9.1** — Schnellerer Kartenaufbau: `render_angebot` und
  `render_angebot_vorschau` liefern die Daten selbst; der Skill ruft sie direkt
  auf statt vorher `angebot_lesen` bzw. `angebot_vorschau`.

- **Angebote 0.9.0** — Angebotssuche mit Filtern: `angebote_suchen` und
  `render_angebote_treffer` filtern nach Status, Kunde, Angebotsdatum und
  Gültigkeit und sortieren nach Datum oder Betrag; Anzahl (`gesamt`) und
  Bruttosumme (`summe_brutto`) aller Treffer rechnet der Server. Neuer
  Skill-Ablauf „Überblick und Nachfassen“; die Kundenkarte zeigt alle Angebote
  des Kunden.

- **Angebote 0.8.0** — Bearbeitungen tragen den gezeigten Stand
  (`erwartet_stand` aus `stand` von `angebot_lesen` oder der letzten Antwort).
  Wurde das Angebot inzwischen geändert, etwa in der Web-App umsortiert,
  speichert der Server nichts, statt eine Positionsnummer auf eine andere
  Position anzuwenden; der Skill beschreibt, wie dann neu gelesen wird.

- **Angebote 0.7.0** — Die Angebotskarte zeigt je Position den Steuersatz, dazu
  Gültigkeit und Notiz, und ändert Kopfdaten (Titel, Datum, Gültigkeit, Notiz)
  selbst. Neu: `angebot_kopie_vorschau` und der Knopf „Als Vorlage kopieren“
  machen aus einem gespeicherten Angebot eine neue Vorschau (schreibt nichts,
  aktuelle Katalogpreise, kein Vertragsrabatt des alten Kunden); angelegt wird
  wie bei jeder Vorschau. Einzelne Bearbeitungen in der Karte gehen still als Kartenstand in den
  Kontext statt als Chatnachricht; Anlegen, Freigabe und PDF meldet sie weiter
  per Nachricht. Der Skill löst bei Formulierungen wie „Angebot schreiben“ oder
  „Kostenvoranschlag“ aus und beschreibt Statuswechsel und PDF ohne
  Widersprüche.

- **Angebote 0.6.0** — Die Belegnummer vergibt der Server. Sie entsteht beim
  Speichern in der Datenbank, je Belegart schon beim Anlegen (Angebot, Aufmaß)
  oder erst bei der Freigabe (Rechnung, Lieferschein, Auftragsbestätigung).
  `angebot_status_setzen` setzt nur noch den Status und meldet die Nummer;
  setzen lässt sie sich über MCP nicht mehr, auch nicht aus einem Diktat.

- **Angebote 0.5.0** — Werkzeugnamen folgen dem Web: `belegarten_auflisten`
  und `belegart_lesen` statt `angebotsvorlagen_auflisten` und
  `angebotsvorlage_lesen`. Die Liste heißt jetzt überall Belegarten, weil sie
  Angebot, Auftragsbestätigung, Lieferschein, Rechnung und Aufmaß enthält.
  `belegart_lesen` liefert zusätzlich die Darstellung (Briefkopf-Schalter,
  Schrift, Folgeseiten), die im Web vom Angebotsdesign in die Belegart gezogen
  ist; Logo, Firma, Adresse und Akzentfarbe kommen aus dem Büro-Branding.

- **Angebote 0.4.0** — Trefferlisten, Kundenkarte und Umsortieren in derselben
  Karte: `render_angebote_treffer` und `render_kunden_treffer` zeigen Treffer als
  antippbare Liste und suchen dafür selbst auf dem Server; `render_kunde` zeigt
  Anschrift, Kontakt, Vertragsrabatt, Ansprechpartner und die fünf jüngsten
  Angebote des Kunden; `angebot_position_verschieben` ändert ausschließlich die
  Reihenfolge. Ein angetippter Treffer ersetzt den Inhalt der Karte an Ort und
  Stelle, ohne weiteren Werkzeugaufruf. Der Skill `angebote-erstellen` nennt die
  neuen Werkzeuge in den Grundregeln sowie in Ablauf 1 und 2. Keine neue
  SQL-Migration, keine Änderung an Endpunkt oder Anmeldung.

- **Angebote 0.1.0** — acht Werkzeuge für Kunden, Produktkatalog, Vorlagen,
  Angebotsvorschau und das Anlegen eines Entwurfs. Gemeinsamer Skill, MCP-Anbindung,
  Claude-/Codex-Manifeste und Marketplace-Einträge. Icon und Logo: 256 × 256 Pixel,
  unter 10 KB. Vorschau mit Prüfcode; Speichern mit wiederverwendbarer Anfrage-ID.
  Preview-Praxistest und Web-Bereitstellung stehen noch aus.

- **Baustellen 0.1.0** — elf Werkzeuge für Baustellensuche und Zusammenfassung,
  Fotos hochladen/lesen/beschriften, Chatnachrichten senden und Aufgaben erstellen.
  Aufgaben unterstützen Beschreibung, aktiven Verantwortlichen, Priorität,
  Beginn, Fälligkeit und Aufwand. Nachrichten, Aufgaben und Änderungen bestehender
  Beschriftungen verwenden eine Vorschau. Wiederholungen mit derselben Anfrage-ID
  erzeugen keine zweite Nachricht, Aufgabe oder Fotodatei-Zuordnung.
  Persönlicher Owner-Zugang mit Baustellenmodul; Web-Berechtigungen und freigegebene
  Baustellentabs gelten zusätzlich. Die vorhandene Galerie, der Baustellenchat und
  die Web-Aufgabenliste werden verwendet. Chat-Fotos: JPEG/PNG/WebP bis 10 MB und
  30 Megapixel, abhängig von der Dateiübergabe des Clients; alternativ Web-Upload.
  Keine neue SQL-Migration; Webserver zuerst bereitstellen. Die eigene ChatGPT-App
  `asdk_app_6aa409ed837081918f0bff4fe668b0df` ist über `.app.json` im Codex-Manifest
  verknüpft. Icon: 256 × 256 Pixel, 6.430 Bytes.

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

- **Energieausweis 0.1.8** — Fotos und Begehung vom Handy: `ea_fotos_uebersicht`,
  `ea_foto_ansehen` (Foto als Bild, z. B. Typenschild ablesen),
  `ea_foto_beschriften`, `ea_fotos_hochladen` (Fotos aus dem Chat),
  `ea_foto_link` (Kamera-Seite der Handy-App) und `ea_anlage_setzen`
  (Typenschild, Wärmeabgabe, Kesselart, Warmwasser, Lüftung, PV/Solar
  eintragen); `ea_projekt_aktualisieren` schreibt auch Auftraggeber und
  Aussteller; `ea_projekt_lesen` zeigt zusätzlich Warmwasser,
  Aufstellort, PV/Solar, Bereiche und den Abschluss der Begehung sowie die
  Anzahl der Fotos. Der Skill beschreibt den Ablauf „mit der Begehung
  weitermachen". Neu sind auch weitere Geschosse:
  `ea_plan_geschoss_kopieren_*` und `ea_plan_geschoss_anlegen_*`;
  `ea_plan_lesen` liefert dafür `umriss_m`. Benötigt den Web-Stand mit den
  neuen Werkzeugen.
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
