# État actuel

## Fait

- Structure du projet créée (specs, epics, governance, roadmap)
- Spécifications candidates rédigées (SPEC, EPICs, US, Features, Tasks)
- Backlog canonique défini dans `backlog.json`
- Dataset d'exemples `data/exigences_sample.json` (10 exigences)
- Implémentation des 3 modules d'audit dans `src/audit_exigences/`
- CLI `python -m audit_exigences.cli`
- 13 tests unitaires passants (oracles indépendants des critères CA)

## Preuves exécutées

- `evidence/audit-report.json` — run complet : 10 exigences, 6 anomalies détectées
  - EPIC-01 grammaire : 3 fautes (REQ-002 : systéme, redemarrer, aprés)
  - EPIC-02 : 1 duplication REQ-001 ↔ REQ-003 (score 1.00)
  - EPIC-03 : 1 négation opposée REQ-004 ↔ REQ-005 ; 1 conflit numérique REQ-006 ↔ REQ-007 (60 vs 80 degrés)
- Statut du run : `ready-for-human-review`

## À faire

- Revue humaine des 6 anomalies
- Fournir le dataset réel d'exigences automobiles (AMB-AUD-005)
- Choisir le dictionnaire orthographique de référence (AMB-AUD-003)
- Figer le seuil de similarité (AMB-AUD-001)
