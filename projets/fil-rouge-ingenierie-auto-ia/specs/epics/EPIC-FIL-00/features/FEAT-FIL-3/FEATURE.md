# FEAT-FIL-3 — Établir la preuve d'un correctif borné

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-00`](../../EPIC.md)
- **User Story parente :** [`US-FIL-3`](../../user-stories/US-FIL-3.md)
- **Jour :** `J01–J05`
- **Sources de formation :** [`C03`](../../../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation / `support_actuel`<br>[`C03-RETOUR`](../../../../baseline/sources.md#c03-retour) — `J03` / Plan préalable, bornes et comparaisons des tests générés, concurrence, doubles, contrôles dans la chaîne / `retour_rapporte`<br>[`N03`](../../../../baseline/sources.md#n03) — `J03` / Plan préalable, tests générés, scripts, qualité et organisation des spécifications ; propos à confirmer / `synthese_automatique`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** mainteneur — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Cas autorisé avec version, entrée, conditions, attendu indépendant, observation et procédure de reproduction ; copie isolée pour la mutation.
- **Sortie :** Observations de reproduction, expérience discriminante, rouge/vert, non-régression et mutation ; proposition de correctif avec revue humaine.
- **Périmètre :** Chaîne de preuve générale J03, distincte de la régression hostile J07 ; aucune correction métier appliquée par la rédaction de cette US.
- **Règle canonique :** [`RM-FIL-3`](../../user-stories/US-FIL-3.md#rm-fil-3)
- **Critères canoniques :** [`CA-FIL-3-01`](../../user-stories/US-FIL-3.md#ca-fil-3-01), [`CA-FIL-3-02`](../../user-stories/US-FIL-3.md#ca-fil-3-02), [`CA-FIL-3-03`](../../user-stories/US-FIL-3.md#ca-fil-3-03), [`CA-FIL-3-04`](../../user-stories/US-FIL-3.md#ca-fil-3-04)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-3-01`](tasks/TASK-FIL-3-01.md) | Décrire attendu/observé et au moins deux hypothèses plausibles ; choisir l'expérience qui les départage. | Reproduire et départager les hypothèses | [`US-FIL-2`](../../user-stories/US-FIL-2.md) |
| [`TASK-FIL-3-02`](tasks/TASK-FIL-3-02.md) | Conserver le rouge pertinent et le plan de correction limité au périmètre autorisé. | Figer le rouge et proposer le patch | [`TASK-FIL-3-01`](tasks/TASK-FIL-3-01.md) |
| [`TASK-FIL-3-03`](tasks/TASK-FIL-3-03.md) | Exécuter le même test après le patch et les tests voisins sans affaiblir leurs assertions. | Vérifier le vert et les cas voisins | [`TASK-FIL-3-02`](tasks/TASK-FIL-3-02.md) |
| [`TASK-FIL-3-04`](tasks/TASK-FIL-3-04.md) | Éprouver le test par mutation, restaurer la copie puis confronter code, documentation et décision de revue. | Éprouver et documenter la correction | [`TASK-FIL-3-03`](tasks/TASK-FIL-3-03.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-3.md#oracle-indépendant) : Contrat et observation initiale indépendants du patch ; comparaison des assertions et versions avant/après ; mutation dans une copie autorisée. Une erreur de compilation seule ne reproduit pas un défaut fonctionnel.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-3-01`](../../user-stories/US-FIL-3.md#ca-fil-3-01)
- [ ] [`CA-FIL-3-02`](../../user-stories/US-FIL-3.md#ca-fil-3-02)
- [ ] [`CA-FIL-3-03`](../../user-stories/US-FIL-3.md#ca-fil-3-03)
- [ ] [`CA-FIL-3-04`](../../user-stories/US-FIL-3.md#ca-fil-3-04)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-21`](../../../../governance/ambiguities.md#amb-21) reste ouverte.
