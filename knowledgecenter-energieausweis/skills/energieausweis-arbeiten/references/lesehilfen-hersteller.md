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

- GEQ-ÜBERNAHME ALS BERECHNUNGSMODELL: Netto-Wandflächen und Fensterträger.
  Voraussetzung: Die AW/IW-Flächen aus Heizlast-/Leitwert-Tabelle sind nachweislich
  NETTO, also bereits ohne Fenster/Türen. Mit der Gebäudehüllfläche gegenprüfen.
  Ist die Flächenbasis unklar, die Unklarheit melden und keine Träger erzeugen.
- Diese Netto-Wandflächen je ursprünglichem Bauteil und Nachbar erhalten; U-Wert
  und Konstruktion übernehmen. Keine Fenster zuordnen. Im Zielfeld für die
  Bruttofläche steht hier die Nettofläche, weil von dieser Wand nichts mehr
  abgezogen wird. Unbekannte Wandorientierungen bleiben null; nicht raten.
  GEOMETRIEAUSDRUCK und Fassadenstreifen dienen dabei nur zur Gegenkontrolle:
  dieselben Wandsegmente/Fassadenstreifen NICHT zusätzlich als Bauteile anlegen.
- Fenster/Türen nach belegter Orientierung UND ursprünglichem Trägerbauteil
  (z.B. AW01/AW02) gruppieren; unterschiedliche Nachbarn/Zonen und Neigungen
  getrennt halten. Geschoßzuordnung erhalten, soweit belegt. Nicht aus einem
  Bauteilkürzel eine Richtung für sämtliche realen Wände ableiten.
- Je belegter Gruppe mit Öffnungen einen Fensterträger anlegen, z.B.
  "Fensterträger S AW01"; bei Aufteilung je Geschoß dieses im Namen ergänzen.
  Typ, Nachbar und Konstruktion vom ursprünglichen Träger übernehmen.
  Bruttofläche = Summe Breite × Höhe × Anzahl der zugeordneten Öffnungen,
  einschließlich Rahmen. Mit UNGERUNDETEN Produkten rechnen, nicht mit der
  Summe gerundeter PDF-Zeilen. Ag ist nur die Glasfläche.
  Ausschließlich diese Öffnungen zuordnen, jede genau einmal und mit ihrer
  Stückzahl. Verbleibende massive Trägerfläche = 0 m². Die Fensterfläche
  NICHT nochmals von den erhaltenen Netto-Wänden abziehen.
  Dachfenster nicht künstlich einer senkrechten Wand zuordnen: ursprünglichen
  Dachtyp und belegte Neigung verwenden; fehlende Angaben melden.
- Nur benötigte Richtungen erzeugen. Keine leeren Träger für alle acht
  Himmelsrichtungen anlegen. Fehlende Richtungen nicht durch Ausschluss raten.
- Fensterträger sind rechnerische Hilfsflächen, KEINE realen Fassadenabmessungen.
  Nicht daraus Plan-/3D-Wände, Geschoßkonturen, BGF oder Volumen ableiten.
- Fensterwerte getrennt erhalten: Uw, g, Glasanteil, Neigung und Verschattung fs.
  fs ist NICHT g: g nicht um fs vermindern. Falls das Zielfeld für fs fehlt,
  den Originalwert im vorhandenen Fenster-Infofeld dokumentieren und die
  fehlende berechnungswirksame Übertragung ausdrücklich melden. Ein Textvermerk
  ersetzt keine Verschattungsberechnung; gleiche solare Gewinne nicht behaupten.
- Kontrolle: erhaltene Netto-Wände + Fensterträger + übrige äußere Bauteile
  = Gebäudehüllfläche. Fensterflächen NICHT nochmals dazuaddieren, sie stecken
  bereits in den Trägern. Innere Bauteile zählen nicht zur Hülle.
  Stückzahlen, Fensterflächen und Richtungspaare separat gegen den Ausweis prüfen.
- Referenz 2189: AW01 171,09 m² + AW02 1.137,06 m² bleiben ohne Öffnungen.
  111 Öffnungen ergeben aus Maßen 340,075 m² (gerundet 340,08 m²), die Summe
  gedruckter gerundeter Zeilen dagegen 340,13 m². Das sind Rundungen, keine
  zusätzliche Wandfläche. Diese Werte sind nur ein Beispiel, keine Standardwerte.
- Fenstertabelle: Ag ist die GLASfläche, Uw der U-Wert. Anz. ist die Stückzahl;
  Gruppenüberschriften tragen die Richtung. Prüfnormmaß-Zeilen nicht übernehmen.
  Beim MCP-Werkzeug gilt netto_flaeche = Breite × Höhe EINES Fensters;
  die Stückzahl steht in der Zuordnung, nicht nochmals in den Abmessungen.
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
2. **Fenster:** Fläche aller zugeordneten Exemplare = anzahl × B × H;
   Gesamtsumme = Fensterfläche des Ausweises. Im MCP-Feld netto_flaeche
   steht dagegen die Fläche EINES Fensters (B × H).
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
