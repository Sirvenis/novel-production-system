# Freshness and Provenance

This package is a separately identified final Showrunner compliance gate. It does not modify or replace:
- `fiction-role-benchmark-v1.1`;
- Wave 1A or Wave 1B evidence;
- `fiction-role-benchmark-v1.2-wave1c-holdout` or its evidence.

Fresh scenario controls:
- new location: Blackglass Estuary Laboratory inside an offshore storm barrier;
- new incident: quarantine-bay load state and deactivated access token during king tide evacuation;
- new characters: Tamsin Roe, Cal Roe, Niko Pell, Esme Venn, Rian Sable;
- new exact literal: `LOT 6 / RETURN UNOPENED`;
- new evidence structures: floor-load threshold and credential acceptance;
- new future-story options: malfunction, staged interference, ecological anomaly.

Automated pre-run freshness validation compares candidate-visible hashes and scans prohibited prior scenario markers, names, locations, incidents, evidence structures, `three short beeps`, and `amber twice, pause, amber once`. The resulting record must be committed before candidate execution.
