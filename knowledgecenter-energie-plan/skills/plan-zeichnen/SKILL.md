---
name: plan-zeichnen
description: Geschosspläne der Energieausweis-Projekte in Knowledge Center zeichnen und korrigieren - Umriss, Ecken, Sollmaße, Wand-Nachbarn, Fenster und Außentüren, Geschosse (anlegen, kopieren, löschen, umsortieren, Keller darunter), Satteldach, Originalpläne je Geschoss; Kontrolle als Bild oder in 3D und anschließend die Übernahme in den Baukörper.
---

# Plan zeichnen in Knowledge Center

Der Zugriff läuft über den MCP-Server `knowledgecenter-energie-plan`. Die
vollständige Arbeitsanleitung liefert der Server beim Verbinden - für alle
Clients gleich. Halte dich daran.

Kurzfassung:

1. `ea_projekte_suchen` → `ea_plan_lesen`. Geschosse heißen über ihre `id`
   oder ihren Namen (z. B. „EG“). Ohne Plan: erster Entwurf mit
   `ea_plan_vorschau`/`ea_plan_speichern`.
2. Alle gewünschten Änderungen als `schritte` in **einem** Aufruf von
   `ea_plan_aendern_vorschau` - alles in Metern, wie `umriss_m`. Die Schritte
   laufen der Reihe nach; Kanten- und Eckennummern gelten für den Stand nach
   den vorherigen Schritten. Ein im selben Aufruf angelegtes Geschoss lässt
   sich über seinen Namen gleich weiterbearbeiten.
3. Vorschau dem Nutzer kurz zeigen (Flächen, Kanten, Gelöschtes). Speichern
   nur auf Auftrag mit `ea_plan_aendern_speichern`, identischen `aenderungen`
   und `pruefcode`; Löschen zusätzlich `loeschen_bestaetigt=true`.
4. Kontrolle mit `ea_plan_bild` je Geschoss - mit `mit_original=true` liegt
   der Originalplan darunter und die Kontur ist rot: liegt sie auf den
   Außenwänden? - oder `ea_plan_3d_anzeigen`.
   Danach die Übernahme in den Baukörper vorschlagen
   (`ea_plan_baukoerper_vorschau`, speichern nur auf Auftrag).

Begriffe:

- Kante k läuft von Ecke k zu Ecke k+1, die letzte zurück zu Ecke 0.
- `abstand_m` bei Fenstern: Kantenanfang bis Öffnungskante, nicht Mitte.
- `hoehe_m` eines Geschosses: Fußboden bis Fußboden mit Decke - nicht die
  lichte Raumhöhe.
- Vektor-PDF (CAD-Export): `einrasten: true` zieht Punkte von
  `ecke_verschieben` und `geschoss_anlegen` bis 15 cm auf die nächste
  Wandecke; die Vorschau nennt unter `eingerastet`, was verschoben wurde.
  `ea_plan_dokumente_lesen` meldet unter `massstab_im_plan` gefundene
  Maßstäbe mit `pixel_pro_meter` - nur bei Originalgröße gültig, an einer
  Bemaßung gegenprüfen.
- Dach: `ea_plan_dach_vorschau`/`_speichern`. Boden-/Deckenbereiche und die
  Zuordnung eines Originalplans: `ea_plan_bearbeiten_vorschau`/`_speichern`.

Regeln: Maße, Höhen, Nordrichtung und Nachbarn nur aus Plan, Bemaßung oder
Nutzerangabe - nie raten, `quelle` immer angeben. Bei „Planstand geändert“
neu lesen und neu prüfen; auch Änderungen im Web zählen. Plan und
Energie-Bauteile sind getrennt.
