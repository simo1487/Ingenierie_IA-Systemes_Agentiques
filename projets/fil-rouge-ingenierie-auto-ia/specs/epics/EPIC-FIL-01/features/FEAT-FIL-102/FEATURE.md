# FEAT-FIL-102 — Lire un journal complet de run

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-01`](../../EPIC.md)
- **User Story parente :** [`US-FIL-102`](../../user-stories/US-FIL-102.md)
- **Jour :** `J06`
- **Sources de formation :** [`C03-RETOUR`](../../../../baseline/sources.md#c03-retour) — `J03` / Plan préalable, bornes et comparaisons des tests générés, concurrence, doubles, contrôles dans la chaîne / `retour_rapporte`<br>[`C06-G5`](../../../../baseline/sources.md#c06-g5) — `J06` / Comparaison, journal complet, interruption et mémoire ; revue G5 / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** opérateur — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Run autorisé, versions de code/configuration, mode réel ou fixture ou replay, horloge contrôlée pour les tests.
- **Sortie :** Observation : événements ordonnés avec run_id, event_id, séquence, étape, transition, auteur, décision, références d'entrée/sortie, durée, erreur et versions ; pas de contenu brut sensible.
- **Périmètre :** Journal d'un run séquentiel ; le stockage distribué est exclu.
- **Règle canonique :** [`RM-FIL-102`](../../user-stories/US-FIL-102.md#rm-fil-102)
- **Critères canoniques :** [`CA-FIL-102-01`](../../user-stories/US-FIL-102.md#ca-fil-102-01), [`CA-FIL-102-02`](../../user-stories/US-FIL-102.md#ca-fil-102-02), [`CA-FIL-102-03`](../../user-stories/US-FIL-102.md#ca-fil-102-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-102-01`](tasks/TASK-FIL-102-01.md) | Définir les champs du journal et une séquence R1 succès/interruption/erreur avec durées factices. | Spécifier et figer l'oracle | [`US-FIL-101`](../../user-stories/US-FIL-101.md) |
| [`TASK-FIL-102-02`](tasks/TASK-FIL-102-02.md) | Instrumenter les transitions de l'orchestrateur et la sérialisation des événements sans changer les décisions métier. | Réaliser dans le périmètre autorisé | [`TASK-FIL-102-01`](tasks/TASK-FIL-102-01.md) |
| [`TASK-FIL-102-03`](tasks/TASK-FIL-102-03.md) | Faire expliquer le journal par un pair, tester l'événement manquant et vérifier l'absence de contenu sensible. | Vérifier et soumettre à revue | [`TASK-FIL-102-02`](tasks/TASK-FIL-102-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-102.md#oracle-indépendant) : Séquence d'événements attendue écrite avant exécution ; horloge et fournisseur factices ; comparaison champ par champ avec la séquence observée, pas avec un second export du même journal.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-102-01`](../../user-stories/US-FIL-102.md#ca-fil-102-01)
- [ ] [`CA-FIL-102-02`](../../user-stories/US-FIL-102.md#ca-fil-102-02)
- [ ] [`CA-FIL-102-03`](../../user-stories/US-FIL-102.md#ca-fil-102-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-02`](../../../../governance/ambiguities.md#amb-02) reste ouverte.
