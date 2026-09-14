# TASK-FIL-204-01 — Recenser les copies/cache et définir la portée du reçu ainsi que l'autorité de révocation

`Référence — tâche candidate`

- **Epic parente :** [`EPIC-FIL-02`](../../../EPIC.md)
- **User Story parente :** [`US-FIL-204`](../../../user-stories/US-FIL-204.md)
- **Feature parente :** [`FEAT-FIL-204`](../FEATURE.md)
- **Jour :** `J06`
- **Phase :** Spécifier et figer l'oracle
- **Sources héritées :** [`C04-RETOUR`](../../../../../baseline/sources.md#c04-retour) — `J04` / Requête directe avant modèle, questions attendues, empreintes, doublons et retrait des sources / `retour_rapporte`<br>[`C06`](../../../../../baseline/sources.md#c06) — `J06` / Comparaison d'organisations, rôles, reprise, idempotence, mémoire et trace / `programme_prevu`
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable des données — personne à désigner

## Objectif

Recenser les copies/cache et définir la portée du reçu ainsi que l'autorité de révocation.

## Prérequis

- **Capacités préalables :** [`US-FIL-203`](../../../user-stories/US-FIL-203.md)
- **Estimation :** non attribuée
- **Date :** non attribuée

Un artefact existant peut satisfaire une capacité préalable après revue ; la tâche ne force pas à refaire un acquis démontré.

## Travail et livrable attendus

**Recenser les copies/cache et définir la portée du reçu ainsi que l'autorité de révocation**

Produire un artefact relu couvrant les cas et l'oracle de [`US-FIL-204`](../../../user-stories/US-FIL-204.md) dans le mode autorisé.

Un replay ou une fixture prépare la vérification ; il ne suffit pas à prouver l’intégration réelle de l’extension.

- **Entrée héritée :** Demande autorisée visant une entrée et une politique de rétention approuvée ; copies de test uniquement.
- **Sortie héritée :** Observation de révocation et reçu minimal sans contenu effacé ; limites sur sauvegardes explicitement déclarées.
- **Périmètre hérité :** Révocation locale sur données fictives ; suppression réelle et rétention légale exclues sans confirmation dédiée.
- **Critères de la US parente (références, pas preuve de couverture de cette tâche) :** [`CA-FIL-204-01`](../../../user-stories/US-FIL-204.md#ca-fil-204-01), [`CA-FIL-204-02`](../../../user-stories/US-FIL-204.md#ca-fil-204-02), [`CA-FIL-204-03`](../../../user-stories/US-FIL-204.md#ca-fil-204-03)

Les clauses et oracles de la spécification parente s'appliquent ; toute modification nécessite une nouvelle revue, pas une adaptation implicite au résultat observé.

## Vérification / sortie

- [ ] Artefact complet correspondant à la phase `Spécifier et figer l'oracle`
- [ ] Source, version, mode et statut déclarés
- [ ] Preuve ou disposition de revue jointe ; la tâche ne devient pas automatiquement `Terminé`

## Questions

Voir [`AMB-07`](../../../../../governance/ambiguities.md#amb-07).
