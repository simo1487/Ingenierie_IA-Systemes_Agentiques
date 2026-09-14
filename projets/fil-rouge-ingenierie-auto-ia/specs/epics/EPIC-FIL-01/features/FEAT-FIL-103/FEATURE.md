# FEAT-FIL-103 — Comparer deux organisations à cas figés

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-01`](../../EPIC.md)
- **User Story parente :** [`US-FIL-103`](../../user-stories/US-FIL-103.md)
- **Jour :** `J06`
- **Sources de formation :** [`C05`](../../../../baseline/sources.md#c05) — `J05` / Besoin avant framework, règle/recherche/workflow/agent et valeur observable / `support_actuel`<br>[`C06-G5`](../../../../baseline/sources.md#c06-g5) — `J06` / Comparaison, journal complet, interruption et mémoire ; revue G5 / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** architecte — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Cas, références et attendus figés avant essai ; deux organisations A/B ; vérificateur avec sources indépendantes ; mode d'exécution déclaré.
- **Sortie :** Observations par cas et proposition de choix avec erreurs, durées, limites et décision humaine ; aucun gain présumé.
- **Périmètre :** Comparaison séquence/producteur-vérificateur avec replay possible ; ni parallélisme imposé ni benchmark de fournisseurs.
- **Règle canonique :** [`RM-FIL-103`](../../user-stories/US-FIL-103.md#rm-fil-103)
- **Critères canoniques :** [`CA-FIL-103-01`](../../user-stories/US-FIL-103.md#ca-fil-103-01), [`CA-FIL-103-02`](../../user-stories/US-FIL-103.md#ca-fil-103-02), [`CA-FIL-103-03`](../../user-stories/US-FIL-103.md#ca-fil-103-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-103-01`](tasks/TASK-FIL-103-01.md) | Figer les cas, les références et les entrées distinctes des rôles conformément à MES-01. | Spécifier et figer l'oracle | [`US-FIL-6`](../../../EPIC-FIL-00/user-stories/US-FIL-6.md), [`US-FIL-102`](../../user-stories/US-FIL-102.md) |
| [`TASK-FIL-103-02`](tasks/TASK-FIL-103-02.md) | Préparer deux exécutions ou deux replays déclarés, en conservant leurs journaux et décisions sans mélanger les modes. | Réaliser dans le périmètre autorisé | [`TASK-FIL-103-01`](tasks/TASK-FIL-103-01.md) |
| [`TASK-FIL-103-03`](tasks/TASK-FIL-103-03.md) | Confronter chaque résultat à l'attendu figé puis faire consigner le choix humain et les limites de comparaison. | Vérifier et soumettre à revue | [`TASK-FIL-103-02`](tasks/TASK-FIL-103-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-103.md#oracle-indépendant) : Contrat MES-01 dans governance/measurement-contracts.md ; attendus indépendants du texte produit par A/B. Un second juge LLM n'est pas l'arbitre final.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-103-01`](../../user-stories/US-FIL-103.md#ca-fil-103-01)
- [ ] [`CA-FIL-103-02`](../../user-stories/US-FIL-103.md#ca-fil-103-02)
- [ ] [`CA-FIL-103-03`](../../user-stories/US-FIL-103.md#ca-fil-103-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-03`](../../../../governance/ambiguities.md#amb-03) reste ouverte.
