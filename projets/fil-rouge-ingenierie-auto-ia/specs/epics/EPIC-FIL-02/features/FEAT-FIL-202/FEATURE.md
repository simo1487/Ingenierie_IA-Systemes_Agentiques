# FEAT-FIL-202 — Borner les reprises et les appels IA

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-02`](../../EPIC.md)
- **User Story parente :** [`US-FIL-202`](../../user-stories/US-FIL-202.md)
- **Jour :** `J06`
- **Sources de formation :** [`N05`](../../../../baseline/sources.md#n05) — `J05` / Approches simples, types, budgets, contrôle humain et structuration ; propos à confirmer / `synthese_automatique`<br>[`C06`](../../../../baseline/sources.md#c06) — `J06` / Comparaison d'organisations, rôles, reprise, idempotence, mémoire et trace / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** opérateur — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Politique datée avec nombre maximal d'essais, délai et plafond d'usage ; configuration fictive explicitement étiquetée pour les tests.
- **Sortie :** Observation d'arrêt avec raison et budget consommé ; reprise proposée uniquement avec entrée observable modifiée.
- **Périmètre :** Budgets d'essais et de temps ; tarifs et seuils de production restent des décisions humaines.
- **Règle canonique :** [`RM-FIL-202`](../../user-stories/US-FIL-202.md#rm-fil-202)
- **Critères canoniques :** [`CA-FIL-202-01`](../../user-stories/US-FIL-202.md#ca-fil-202-01), [`CA-FIL-202-02`](../../user-stories/US-FIL-202.md#ca-fil-202-02), [`CA-FIL-202-03`](../../user-stories/US-FIL-202.md#ca-fil-202-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-202-01`](tasks/TASK-FIL-202-01.md) | Définir la politique de budget et les attendus aux limites, en séparant essai initial et reprises. | Spécifier et figer l'oracle | [`US-FIL-102`](../../../EPIC-FIL-01/user-stories/US-FIL-102.md) |
| [`TASK-FIL-202-02`](tasks/TASK-FIL-202-02.md) | Prévoir les gardes de reprise et l'arrêt sur timeout autour des appels, avec événements de budget. | Réaliser dans le périmètre autorisé | [`TASK-FIL-202-01`](tasks/TASK-FIL-202-01.md) |
| [`TASK-FIL-202-03`](tasks/TASK-FIL-202-03.md) | Tester limites exactes, entrée inchangée et fournisseur lent avec horloge factice ; faire approuver les paramètres réels séparément. | Vérifier et soumettre à revue | [`TASK-FIL-202-02`](tasks/TASK-FIL-202-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-202.md#oracle-indépendant) : Horloge factice et compteur externe d'appels, limites choisies comme données de test et non valeurs de production ; cas d'expiration en cours d'appel et d'annulation à spécifier avant implémentation.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-202-01`](../../user-stories/US-FIL-202.md#ca-fil-202-01)
- [ ] [`CA-FIL-202-02`](../../user-stories/US-FIL-202.md#ca-fil-202-02)
- [ ] [`CA-FIL-202-03`](../../user-stories/US-FIL-202.md#ca-fil-202-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-06`](../../../../governance/ambiguities.md#amb-06) reste ouverte.
