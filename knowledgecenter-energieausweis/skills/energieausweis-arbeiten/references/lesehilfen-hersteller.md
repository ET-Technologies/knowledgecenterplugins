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
  Nachbarhaus" → bei belegtem beheiztem Nachbargebäude und belegtem Ausschluss
  aus der thermischen Hülle INNENWAND mit Nachbar BEHEIZT (Feuermauer), siehe
  Konstruktionstypen. Die Bezeichnung allein belegt das nicht; unklare
  Nachbarbedingungen melden. Kellerdecke → BODEN mit
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
  Bruttofläche des Fensterträgers muss BEIDE Öffnungssummen echt übertreffen:
  S_exakt = Σ Anzahl × Breite × Höhe aus den UNGERUNDETEN Produkten;
  S_3 = Σ Anzahl × runden3(Breite × Höhe).
  Träger = aufrunden2(max(S_exakt, S_3)); ist das Ergebnis gleich dem Maximum,
  weitere 0,01 m² addieren. runden3 betrifft die Einzelfläche VOR der
  Multiplikation mit der Stückzahl; aufrunden2 rundet nach oben auf 2 Dezimalen.
  Dezimal rechnen, ohne Gleitkommaartefakte. Maße einschließlich Rahmen
  verwenden und gegen die tatsächlich exportierten Maße prüfen. Ag ist nur
  die Glasfläche. NIE abrunden, NIE gerundete PDF-Zeilen summieren.
  Hintergrund: Laut berichtetem Ecotech-Importtest prüft der Baukörper mit
  auf 3 Dezimalen gerundeten Einzelflächen, das Berechnungsmodul mit exakten
  Produkten; auch Restfläche 0 wurde dort abgelehnt. Das Verhalten nach dem
  Import in der verwendeten Ecotech-Version in BEIDEN Modulen prüfen.
  Beispiele Wienerstraße 28b:
  39 × 0,96 × 1,66 + 0,90 × 1,90 → S_exakt 63,8604, S_3 63,876;
  Träger 63,88 m² (63,87 ist kleiner als S_3).
  30 × 0,98 × 1,68 + 9 × 0,50 × 1,30 → S_exakt 55,242, S_3 55,230;
  Träger 55,25 m² (55,24 ist kleiner als S_exakt).
  Den Zuschlag Δ = Träger − S_exakt je Träger und insgesamt dokumentieren.
  Diese rechnerische Restfläche ist gewollt, aber keine reale Wandfläche.
  Sie ist NICHT allgemein auf 0,001–0,02 m² begrenzt: Die Rundungsdifferenz
  der Einzelflächen wächst mit der Stückzahl. Nicht pauschal als rechnerisch
  bedeutungslos behandeln; ihren Einfluss in der Gegenkontrolle prüfen.
  Ausschließlich diese Öffnungen zuordnen, jede genau einmal und mit ihrer
  Stückzahl. Die Fensterfläche NICHT nochmals von den erhaltenen Netto-Wänden
  abziehen.
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
  = Gebäudehüllfläche des Ausweises + dokumentierte Zuschläge der zur Hülle
  zählenden Fensterträger, sofern die ursprüngliche Flächenbilanz schließt.
  Fensterflächen NICHT nochmals dazuaddieren, sie stecken bereits in den
  Trägern. Innere Bauteile zählen nicht zur Hülle.
  Stückzahlen, Fensterflächen und Richtungspaare separat gegen den Ausweis prüfen.
  Original-Hüllfläche und Modell-Hüllfläche getrennt berichten; den Quellwert
  nicht überschreiben. Berichteter Vergleich Wienerstraße: 2.034,12 statt
  2.034,08 m² = +0,04 m². GEQ-Fensterliste 141,56 gegenüber Heizlasttabelle
  141,53 m² = +0,03 m²; das ist eine SEPARATE Rundungsdifferenz.
  Nur nachvollziehbar berechnete Zuschläge akzeptieren; keine anderen
  Bauteilflächen zum Ausgleich verändern. BGF und Volumen gegen den Ausweis
  prüfen; A_B, A/V und lc unter Berücksichtigung der dokumentierten Zuschläge
  abgleichen. Für Um/LEK auch OIB-Kategorien, Temperatur-Korrekturfaktoren,
  U-Werte und weitere Berechnungseinstellungen prüfen. Das Setzen der
  Kategorien allein garantiert keine Übereinstimmung.
- Referenz 2189: AW01 171,09 m² + AW02 1.137,06 m² bleiben ohne Öffnungen.
  111 Öffnungen ergeben aus Maßen 340,075 m² (gerundet 340,08 m²), die Summe
  gedruckter gerundeter Zeilen dagegen 340,13 m². Das sind Rundungen, keine
  zusätzliche Wandfläche. Diese Werte sind nur ein Beispiel, keine Standardwerte.
- Fenstertabelle: Ag ist die GLASfläche, Uw der U-Wert. Anz. ist die Stückzahl;
  Gruppenüberschriften tragen die Richtung. Prüfnormmaß-Zeilen nicht übernehmen.
  Beim MCP-Werkzeug gilt netto_flaeche = Breite × Höhe EINES Fensters;
  die Stückzahl steht in der Zuordnung, nicht nochmals in den Abmessungen.
- Wand gegen andere Bauwerke ZW..: Ist sie im Ausweis als thermisch nicht
  wirksame Trennwand zu einem beheizten Nachbarbereich nachgewiesen und
  nicht in A_B enthalten, als INNENWAND, Nachbar BEHEIZT, Konstruktion
  INTERNAL_WALL übernehmen; in_huelle = false, in_bgf = false, Richtung null.
  Heizlasttabelle ohne Korrekturfaktor UND ohne Summenbeitrag als Gegenkontrolle
  verwenden. Das Kürzel ZW.. oder ein fehlender Faktor allein genügt nicht.
- Warme Zwischendecke ZD.. = inneres Bauteil (DECKE mit Nachbar BEHEIZT),
  in_huelle = false, aber in_bgf = true, wenn sie den Geschossboden abbildet.
  Jeden Geschossboden nur einmal zählen, nicht zusätzlich eine identische
  Bodenfläche anlegen.

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
   Bei GEQ die berechneten Trägerzuschläge separat ausweisen und gegenrechnen.
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
  Für eine belegte Wand zum beheizten Nachbargebäude / Feuermauer, die im
  Ausweis nicht zur thermischen Hülle zählt: Typ INNENWAND, Nachbar BEHEIZT,
  in_huelle = false. Im Ecotech-Import die Zuordnung als Innenwand zum
  beheizten Nachbarbereich und den Ausschluss aus A_B prüfen.
  Für diesen Fall NICHT Nachbar NACHBAR und NICHT AUSSENWAND warm/warm
  verwenden: In den berichteten Importtests kam es zu ungültigen Zuordnungen
  bzw. zusätzlicher Hüllfläche. Diese Regel nicht auf unbeheizte oder
  unbekannte Nachbarbereiche übertragen; deren Bedingungen aus dem Ausweis
  übernehmen bzw. klären, statt sie zur Anpassung von A_B als beheizt zu setzen.
- DECKE/BODEN gegen AUSSEN = SLAB_OVER_THOROUGHFARE (die Durchfahrt IST
  Außenluft); gegen Garagen-Einheit = …\_DOWNWARDS. NIE SLAB mit einer
  Raum-Einheit kombinieren.
- Decke gegen getrennte Einheit (Gewerbe) = Nachbar ANDERE_WOHNEINHEIT +
  …\_DOWNWARDS; liegt die Einheit oberhalb: …\_UPWARDS. Nachbar BEHEIZT
  (Zwischendecke) = …\_NO_HEATFLOW, zählt NICHT zur Hülle, aber ZUR BGF
  (in_bgf = true), wenn sie den Geschossboden abbildet. Nicht doppelt zählen.
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
5. `ea_zuordnungen_setzen`: Öffnungen dem belegten Träger gleicher Richtung,
   Bauteilzugehörigkeit und Neigung mit Stückzahl zuordnen; Dachfenster dem Dach.
6. `ea_pruefsummen` — Ergebnis dem Benutzer als Tabelle berichten, bei GEQ
   einschließlich der Trägerzuschläge. „Außenwand ohne Richtung“ ist nur bei
   bewusst erhaltenen GEQ-Nettowänden ohne belegte Richtung erwartbar;
   nicht pauschal für Fensterträger oder belegte Fassaden ignorieren.
7. `ea_export_xml` und Import in Ecotech. Danach im BERECHNUNGSMODUL und
   im Baukörper die Meldungsliste prüfen. Bei „Nettofläche kleiner Null“
   zunächst Stückzahlen, Maße, Doppelzuordnungen und beide Öffnungssummen
   prüfen. Nur bei bestätigtem Rundungsproblem den rechnerischen GEQ-Fensterträger um
   0,01 m² erhöhen, Zuschlag dokumentieren, neu exportieren und erneut prüfen.
   Nicht unbegrenzt erhöhen oder echte Zuordnungsfehler damit verdecken.
   Gebäudekenndaten gegen den Ausweis abgleichen (BGF, Volumen, A_B, A/V, lc),
   dabei dokumentierte Rundungszuschläge berücksichtigen. Wenn Ecotech nicht
   verfügbar ist, XML bereitstellen und den Importtest als offen melden;
   keine erfolgreiche Prüfung behaupten.
