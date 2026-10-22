---
name: plan-zeichnen
description: Geschosspläne der Energieausweis-Projekte in Knowledge Center zeichnen und korrigieren - Umriss, Ecken, Sollmaße, Wand-Nachbarn, Fenster und Außentüren, Geschosse (anlegen, kopieren, löschen, umsortieren, Keller darunter), Dach (Sattel, Pult, Walm), Boden-/Deckenbereiche, Originalpläne je Geschoss mit Einrasten auf Vektor-PDFs und Lupe mit Meterraster für Scans, Aufmaß als Maßkette; Prüfung mit Kennzahlen vorher/nachher, Kontrolle als Bild oder in 3D und anschließend die Übernahme in den Baukörper.
---

# Plan zeichnen in Knowledge Center

Der Zugriff läuft über den MCP-Server `knowledgecenter-energie-plan`. Die
vollständige Arbeitsanleitung liefert der Server beim Verbinden - für alle
Clients gleich. Halte dich daran.

Kurzfassung:

1. `ea_projekte_suchen` → `plan_lesen`: Plan in Metern mit **festen IDs**
   für Geschosse, Ecken, Wände und Öffnungen, Himmelsrichtung je Wand,
   Unterlage (Originalplan, Maßstab). Originalplan: `ea_plan_dokumente_lesen`;
   bei Vektor-PDF liefert `plan_linien_lesen` die Wandlinien in denselben
   Metern.
   Bei Scans und großen Blättern sind die Maßzahlen im Gesamtbild
   unlesbar: dann die Lupe `plan_ausschnitt`. Erst die ganze Seite mit
   `dokument_id` (Blattpixel) - Seite wählen, Maßstab an einer Bemaßung
   messen, `geschoss_anlegen` mit `unterlage`. Danach mit `geschoss` und
   `wand` oder `bereich` Wand für Wand hineinzoomen: Raster in Plan-Metern,
   Maßketten lesen, Ecken am Raster ablesen. Bemaßung geht vor Raster.
2. Alle gewünschten Änderungen als `befehle` in **einem** Aufruf von
   `plan_befehle_vorschau`. Befehle nennen IDs, keine Nummern: Ecke einfügen
   teilt eine Wand, alle übrigen IDs bleiben. Neue Geschosse, Ecken und
   Öffnungen bekommen eine neue UUID von dir. Das Web nutzt dieselben Befehle.
   Ohne Plan: `geschoss_anlegen`, dann `masskette` (Aufmaß „10 m, dann links
   8 m …“) oder `umriss_setzen`; Originalplan mit `unterlage_setzen`.
3. Vorschau lesen: `pruefung.offen` (was noch fehlt, z. B. offener Umriss,
   Norden, U-Werte), `pruefung.kennzahlen_aenderung` (Fläche, Volumen, Hülle
   vorher/nachher) und `eingerastet`. Dem Nutzer kurz zeigen. Speichern nur
   auf Auftrag mit `plan_befehle_speichern`, identischen `befehle`,
   `einrasten` und `pruefcode`; Löschen zusätzlich `loeschen_bestaetigt=true`.
4. Kontrolle mit `plan_bild` je Geschoss: Kurzzeichen E/W/F/B mit Zuordnung
   zu den IDs, mit `befehle` auch als Entwurf vor dem Speichern; mit
   `mit_original=true` liegt der Originalplan darunter und die Kontur ist
   rot - liegt sie auf den Außenwänden? Im Detail `plan_ausschnitt` mit
   `mit_umriss=true` je Wand. Oder `ea_plan_3d_anzeigen`.
   Danach die Übernahme in den Baukörper vorschlagen
   (`ea_plan_baukoerper_vorschau`, bei vorhandenem Baukörper
   `modus: abgleichen` – U-Werte und Konstruktionen bleiben; speichern nur
   auf Auftrag).

Begriffe:

- Plan-Bezug: Meter, x nach rechts, y nach oben, für alle Geschosse gleich.
  Wand-ID = ID ihrer Anfangsecke; die Wand läuft zur nächsten Ecke.
- `mitteM` bei Öffnungen: Wandanfang bis Mitte der Öffnung.
- `hoehe_m` eines Geschosses: Fußboden bis Fußboden mit Decke - nicht die
  lichte Raumhöhe.
- `masskette`: `schritte` mit `laengeM` und `drehung` (`links`, `rechts`,
  `gerade` oder Grad) ab `start`/`startRichtungGrad`; ein vorhandener Umriss nur mit
  `ersetzen: true`.
- Vektor-PDF (CAD-Export): `einrasten: true` zieht neu gesetzte oder
  verschobene Ecken bis 15 cm auf die nächste Linienecke; die Vorschau nennt
  unter `eingerastet`, was verschoben wurde. `ea_plan_dokumente_lesen`
  meldet unter `massstab_im_plan` gefundene Maßstäbe mit `pixel_pro_meter` -
  nur bei Originalgröße gültig, an einer Bemaßung gegenprüfen.
- Dach: `ea_plan_dach_vorschau`/`_speichern` – Satteldach, Pultdach oder
  Walmdach; bei L/T/U Grate und Kehlen je Flügel, beim Satteldach Giebel an
  den Flügelenden. Boden-/Deckenbereiche
  (unterkellerter Teil, Boden über Garage, Terrasse): `bereich_setzen` /
  `bereich_loeschen`.
- Web und KI am selben Plan: Ein offener Plan-Reiter übernimmt gespeicherte
  Änderungen von selbst, als rückgängig machbaren Schritt „KI: …“. Speichert
  das Web gleichzeitig, werden Änderungen an verschiedenen Ecken
  zusammengeführt.

Regeln: Maße, Höhen, Nordrichtung und Nachbarn nur aus Plan, Bemaßung oder
Nutzerangabe - nie raten, `quelle` immer angeben. Bei „Planstand geändert“
neu lesen und neu prüfen. Plan und Energie-Bauteile sind getrennt.
