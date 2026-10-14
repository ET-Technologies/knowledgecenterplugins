# Begehung in den Energieausweis übernehmen

Lies das, wenn der Benutzer Werte aus einer **Begehung der Begehung-App** in
einen Energieausweis bringen will („Übernimm die Begehung in EA-2026-0023",
„Was hat der Kollege vor Ort aufgenommen?", „Mach den Ausweis aus der
Begehung fertig").

## Warum es diesen Ablauf gibt

Begehung und Ausweis macht oft nicht dieselbe Person: Jemand nimmt vor Ort
auf (Diktat, Fotos, Kopf), jemand anderer rechnet im Büro. Die Begehung ist
deshalb ein **eigenes Dokument** und bleibt unverändert erhalten — so geht
nichts verloren, was vor Ort festgestellt wurde. Das Büro entscheidet, was in
den Ausweis kommt. Der Ausweis kann bereits geprüfte Angaben enthalten (aus
einem alten Ausweis, aus Plänen, vom Kunden); eine Begehung ist ein
Beleg unter mehreren, kein automatisches Update.

Daraus folgt alles Weitere: Werte zeigen statt schreiben, Herkunft nennen,
Überschreiben eigens ansprechen.

## Nicht verwechseln

- **Erfassung in der Energieausweis-App** (alter Weg): schreibt direkt in die
  Felder des Ausweises. Dafür gilt der Abschnitt „Begehung vom Handy und
  Fotos" im Skill.
- **Begehung-App** (dieser Ablauf): eigenes Dokument, in `ea_projekt_lesen`
  unter „Begehungen" mit `[begehung:id]`.

## Ablauf

1. **Lesen.** `ea_projekt_lesen` (Stand und Liste der Begehungen), dann
   `ea_begehung_lesen` (Kopf, Abschnitte, Fotonotizen, Diktat, Verknüpfung,
   frühere Übernahmen).
   - Mehrere Begehungen: fragen, welche gilt. Eine Nach- oder
     Ergänzungsbegehung kann ältere Angaben ersetzen — oder nur ergänzen.
   - „Bereits übernommen": sagen, was schon drin ist, statt es erneut
     anzubieten.
   - Nicht oder mit einem anderen Ausweis verknüpft: ansprechen;
     `begehung_verknuepfen` nur auf Auftrag.
2. **Werte herausziehen.** Nur was die Begehung belegt, je Wert mit kurzer
   Quelle („Kopf", „Diktat", „Fotonotiz Heizung"). Nicht umrechnen, nicht
   schätzen. Widerspricht sich die Begehung selbst (Diktat sagt 1972, Kopf
   1974), nicht auflösen, sondern als offene Frage nennen.
   - Fotos zählen nur, wenn du sie wirklich angesehen hast (`foto_ansehen`).
     In Clients ohne Bildanzeige (ChatGPT) nur Diktat und Notizen verwenden
     und das dazusagen — sonst entstehen Werte, die niemand gesehen hat.
3. **Vorschau.** `ea_begehung_uebernahme_vorschau` mit allen Werten. Die
   Tabelle zeigen (jetzt im Ausweis · aus der Begehung · Quelle), darunter
   die offenen Fragen. Werte mit „ÜBERSCHREIBT" eigens nennen: Hier steht
   schon etwas anderes, und nur der Benutzer weiß, was stimmt.
4. **Speichern nach Auswahl.** `ea_begehung_uebernahme_speichern` mit
   denselben Werten, dem `pruefcode` und `nur=[gewählte Felder]`.
   `ueberschreiben_bestaetigt=true` nur, wenn der Benutzer dem Überschreiben
   ausdrücklich zugestimmt hat. Meldet der Server eine Änderung seit der
   Vorschau: neue Vorschau zeigen, nicht blind wiederholen.
5. **Der Rest.** Fenster, Bauteile, Dach und Hausakte haben eigene Werkzeuge
   mit eigener Vorschau (`ea_fenster_setzen`, `ea_bauteile_setzen`,
   `ea_plan_dach_vorschau`, `ea_hausakte_eintragen`). Auch dort: erst zeigen,
   dann auf Auftrag schreiben.

## Felder

Schlüssel wie in `ea_projekt_aktualisieren` (z. B. `baujahr`,
`anzahl_geschosse`, `dachtyp`, `daemmung_fassade`, `brennstofftyp`,
`heizungs_baujahr`, `heizungsregelung`, `auftraggeber_name`), die Anlage mit
Gruppe davor: `typenschild.hersteller`, `typenschild.leistung_kw`,
`anlage.kesselart`, `anlage.aufstellort`, `anlage.warmwasser`,
`anlage.lueftung`, `pv_solar.pv`, `pv_solar.pv_kwp`. Die vollständige Liste
steht im Werkzeug. Leere Werte gibt es nicht — aus einer Begehung wird nichts
gelöscht.

## Beispiel

Benutzer: „Übernimm die Begehung von gestern in den Ausweis Landstraße."

1. `ea_projekte_suchen` „Landstraße" → `ea_projekt_lesen`: eine Begehung
   BG-2026-0007 („Erstbegehung", gestern).
2. `ea_begehung_lesen`: Kopf Baujahr 1974; Diktat „Gastherme im Keller,
   Brennwert, Baujahr 2009"; Fotonotiz „Typenschild Vaillant ecoTEC".
3. Vorschau mit `baujahr` 1974 (Kopf), `brennstofftyp` Erdgas (Diktat),
   `heizungs_baujahr` 2009 (Diktat), `anlage.kesselart` Gas-Brennwertkessel
   (Diktat), `anlage.aufstellort` Keller (Diktat), `typenschild.hersteller`
   Vaillant (Fotonotiz).
4. Antwort an den Benutzer, sinngemäß:

   > Aus der Begehung BG-2026-0007 kann ich 6 Werte übernehmen. **Baujahr
   > überschreibt** den eingetragenen Wert 1972 mit 1974 (Kopf der
   > Begehung) — welcher stimmt? Offen: Leistung am Typenschild steht nicht
   > in der Begehung. Soll ich die übrigen 5 übernehmen?

5. Nach „ja, Baujahr auch" → Speichern mit `ueberschreiben_bestaetigt=true`.
