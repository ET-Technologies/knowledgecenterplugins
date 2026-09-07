# Lesehilfen: Energieausweise je Hersteller

Wo welche Werte stehen und welche Fallen es gibt. Grundregel: **nichts
erfinden.** Was nicht im Dokument steht, bleibt leer und wird gemeldet.
Richtungen nie raten — nur dokumentierte Ketten übernehmen.

## Lesen

- Text-PDF: Rohtext extrahieren; layoutkritische Tabellen zusätzlich als
  Bild prüfen. Scan-PDF: nur Bilder.
- Seitenzahlen stehen meist in der Fußzeile; die Textextraktion hängt sie ans
  Seitenende.

## ETU (Gebäudeprofi, eausweis.at)

- Flächen: „5.1 Gebäudegeometrie – Flächen" (brutto UND netto) sowie
  „6.1 spezifische Transmissionswärmeverluste" (netto + U-Werte + Fx).
- Fensterformeln in der Berechnungsspalte: `21 * (1,1*2)` = anzahl 21,
  Breite 1,1, Höhe 2,0. Mischformeln (`12*(1,1*2) + 6*(0,4*0,6)`) in MEHRERE
  Fenstertypen aufsplitten.
- g-Wert und Glasanteil: „6.3 Daten transparenter Bauteile" (Faktor
  Rahmenanteil = Glasanteil, Gesamtenergiedurchlassgrad = g). NICHT den
  wirksamen Wert.
- 16er-Windrose exakt abschreiben (NNO 22,5 / NNW 337,5 — der letzte
  Buchstabe entscheidet die Seite). Fenster und ihre Wand sind ein
  Richtungspaar.
- Kennzahlen im 2011er-Layout: HWB = REFERENZKLIMA-Spalte (links), nicht SK.
- Kategorien der Anforderungsliste: „Flachdach" → DACH; „Decke über
  Außenluft (Durchfahrten, Parkdecks)" → DECKE mit Nachbar AUSSEN; „Wand zu
  Nachbarhaus" → Nachbar NACHBAR (Feuermauer); Kellerdecke → BODEN mit
  UNBEHEIZTER_KELLER. Liegende Flächen gegen Garagen-Einheiten sind Decken
  mit Wärmestrom nach unten.
- Richtungen: Ecotech kennt nur das 8er-Raster (N, NO, O, SO, S, SW, W, NW).
  Wände und Fenster deshalb gleich im 45-Grad-Raster schreiben
  (NNO→NO 45, OSO→SO 135, SSW→SW 225, WNW→NW 315) und die Namen ohne
  16er-Kürzel vergeben. Die Originalrichtungen in die Notizen.
- Anlagentechnik: Kapitel 7 (Wärmeerzeugung, Baujahr, Brennstoff, Regelung,
  Lüftung, Warmwasser).

## GEQ (Zehentmayer)

- Wände NUR als Einzelsegmente aus dem Geometrieausdruck (W1..W4 je
  Geschossblock, brutto) plus Fassadenstreifen-Zeilen. Die Heizlast-Zeilen
  AW/IW sind NETTO-Summen derselben Wände — nie zusätzlich.
- Fenstertabelle „Fenster und Türen": Ag ist die GLASfläche, Uw der U-Wert;
  Anz.-Spalte = Stückzahl; Gruppenüberschriften tragen die Richtung;
  Prüfnormmaß-Zeilen sind keine Fenster.
- Wand-Richtungen nur über die dokumentierte Kette (Öffnung eines
  Wand-Bauteils in einer Richtungsgruppe + Teilung im Geometrieausdruck;
  Gegenwand der Grundform = Gegenrichtung). Offene bleiben leer. Dieselbe
  Segmentnummer ist dieselbe Fassade — EG W3 und OG1 W3 zeigen nie in
  verschiedene Richtungen.
- Warme Zwischendecke ZD.. = inneres Bauteil (DECKE mit Nachbar BEHEIZT).

## ArchiPHYSIK (A-NULL)

- Zwei Tabellen zusammen lesen: „Leitwerte" (je Richtung Nord/Ost/Süd/
  West/Horizontal, NETTO-Flächen + U + Fx; Summe = Hüllfläche) und
  „Bauteilflächen" (BRUTTO, mit „n x Einzelfläche" und Richtungsbuchstabe
  N/O/S/W/H — dort stehen die Stückzahlen). Brutto-Wand minus
  Leitwerte-Netto = Fensterfläche der Wand; jede Richtung muss auf 0,00
  schließen.
- Fenster-Einzelflächen sind WIRKSAME Flächen (lichte Maße), nicht das
  Nennmaß im Namen („Fenster 100\*80" = 0,63 m² = 0,90 × 0,70): Nennmaß minus
  0,10 m je Seite. Bei Türen mit Breite = Nennbreite − 0,10 die eine glatte
  cm-Höhe suchen, deren Produkt auf die EA-Fläche rundet; nur wenn keine
  existiert, Höhe flächentreu mit Hinweis. NIE das Nennmaß als Breite/Höhe
  speichern — aber die Namen tragen die EA-Bezeichnung mit Nennmaß.
- „Gewinne"-Seite: Spalte g fix 0,75 = Fs (Verschattung, NICHT g!), Ag =
  Glasfläche, dritte Spalte = g je Bauteil. glasanteil = Ag/Fläche.
  Verglaste Eingangstüren zählen zur Fensterfläche.
- Mehrzonen-Gebäude: Trennflächen zwischen beheizten Zonen sind NICHT in der
  Hülle — nicht anlegen. Seite „Geschossfläche und Volumen" liefert die BGF
  je Geschoss für die Gegenrechnung.
- Terrassen (D..) sind Dächer gegen Außenluft (ROOF, flach); „Fußboden über
  Durchfahrt/Gang" = Decke gegen AUSSEN; „Fußboden über KG/TG" = BODEN gegen
  TIEFGARAGE.
- Kennzahlen vom Label (RK = Anforderungsspalte): HWB Ref RK; SK-Block
  darunter.

## Ecotech (BuildDesk)

- Wände brutto aus „Beheizte Hülle" (Spalte „Ausricht./Neigung", z. B.
  „135deg/90deg"); „zu Garage" → DURCHFAHRT. Die Gebäudedaten-Seite ist
  netto — nicht doppeln.
- Fenster „kompakt": Zeile „3 AF 1,46/1,34m U=0,73" → anzahl 3; AF/AT/IT =
  Fenster/Außentür/Innentür; Glasanteil-Spalte in %, g-Spalte (nicht gw).
- HWB aus dem Referenzklima-Block.

## Prüfsummen VOR dem Schreiben (alle müssen aufgehen)

1. **Hülle:** Summe der Bauteil-Bruttoflächen = Hüllfläche des Ausweises
   (brutto inkl. Fenster) bzw. netto + Fensterflächen. Toleranz < 0,5 %.
   Innere Bauteile (Nachbar beheizt) zählen NICHT zur Hülle.
2. **Fenster:** je Typ netto = anzahl × B × H; Gesamtsumme = Fensterfläche
   des Ausweises (steht meist explizit).
3. **Richtungspaare:** jede Fensterrichtung hat eine Wand gleicher Richtung.
4. **BGF:** Summe der Geschossböden (BODEN immer; DECKE gegen beheizt/
   Durchfahrt) muss zur BGF passen. Listet der Ausweis keine
   Zwischendecken, die Lücke als Notiz dokumentieren — nicht erfinden.
5. **U-Werte** gegen die Anforderungsliste des Ausweises quergelesen.

## Konstruktionstypen (Ecotech-Importregeln)

- Wand gegen JEDEN fremden Bereich (Garage, Keller, Stiegenhaus,
  Nachbargebäude, andere Wohneinheit) = INTERNAL_WALL.
- DECKE/BODEN gegen AUSSEN = SLAB_OVER_THOROUGHFARE (die Durchfahrt IST
  Außenluft); gegen Garagen-Einheit = …\_DOWNWARDS. NIE SLAB mit einer
  Raum-Einheit kombinieren.
- Decke gegen getrennte Einheit (Gewerbe) = Nachbar ANDERE_WOHNEINHEIT +
  …\_DOWNWARDS; liegt die Einheit oberhalb: …\_UPWARDS. Nachbar BEHEIZT
  (Zwischendecke) = …\_NO_HEATFLOW, zählt weder zur Hülle noch zur BGF.
- Decke → Dachraum = …\_UPWARDS; Flachdach = ROOF mit Flachdach-Haken.
- Neigung: Wand 90, Decke/Boden 0. Eine Decke mit 90 steht für Ecotech
  senkrecht.

## Schreiben (Reihenfolge ist Pflicht)

1. `ea_projekt_anlegen` (Status `test` für Probeläufe) und
   `ea_projekt_aktualisieren` mit Stammdaten, Anlage-Grunddaten und einer
   Notiz zur Herkunft (Software, Ausstellungsdatum, Besonderheiten).
2. `ea_konstruktionen_setzen`: je Aufbau des Ausweises eine Konstruktion.
3. `ea_bauteile_setzen`: Flächen mit Typ, Bruttofläche, Richtung (8er-Raster),
   Neigung, Nachbar, U-Wert und `konstruktion_id`.
4. `ea_fenster_setzen`: Breite × Höhe, Nettofläche = EIN Fenster, U, g,
   Glasanteil, Richtung; Namen mit der EA-Bezeichnung.
5. `ea_zuordnungen_setzen`: Fenster an die Außenwand gleicher Richtung mit
   Stückzahl.
6. `ea_pruefsummen` — Ergebnis dem Benutzer als Tabelle berichten.
