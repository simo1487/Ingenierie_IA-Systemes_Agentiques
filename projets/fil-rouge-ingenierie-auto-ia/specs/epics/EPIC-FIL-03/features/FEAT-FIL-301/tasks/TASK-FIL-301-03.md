# TASK-FIL-301-03 — Produire un appel autorisé et un refus hors portée avec compteur d'accès, puis retirer le garde en environnement de test pour éprouver l'oracle

`Référence — tâche candidate`

- **Epic parente :** [`EPIC-FIL-03`](../../../EPIC.md)
- **User Story parente :** [`US-FIL-301`](../../../user-stories/US-FIL-301.md)
- **Feature parente :** [`FEAT-FIL-301`](../FEATURE.md)
- **Jour :** `J07`
- **Phase :** Vérifier et soumettre à revue
- **Sources héritées :** [`C05-SKILL`](../../../../../baseline/sources.md#c05-skill) — `J05` / Méthode capitalisée, outils/événements versionnés, limites des démonstrations LlamaIndex / `support_actuel`<br>[`C07-G6`](../../../../../baseline/sources.md#c07-g6) — `J07` / Outil préparé ou replay, refus avant accès, régression et première divergence ; G6 / `programme_prevu`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable sécurité — personne à désigner

## Objectif

Produire un appel autorisé et un refus hors portée avec compteur d'accès, puis retirer le garde en environnement de test pour éprouver l'oracle.

## Prérequis

- **Capacités préalables :** [`TASK-FIL-301-02`](TASK-FIL-301-02.md)
- **Estimation :** non attribuée
- **Date :** non attribuée

Un artefact existant peut satisfaire une capacité préalable après revue ; la tâche ne force pas à refaire un acquis démontré.

## Travail et livrable attendus

**Produire un appel autorisé et un refus hors portée avec compteur d'accès, puis retirer le garde en environnement de test pour éprouver l'oracle**

Réaliser la phase décrite par [`FEAT-FIL-301`](../FEATURE.md) sans revendiquer une disponibilité ou une preuve non observée.

Une fixture ou un replay n’est recevable que si le périmètre de la US l’autorise, avec mode et limites déclarés.

- **Entrée héritée :** Identité issue du contexte de confiance, outil read-only nommé, arguments typés par identifiants et périmètre autorisé versionné.
- **Sortie héritée :** Observation autorisé/refusé avec règle, raison et ordre des événements ; résultat uniquement après autorisation.
- **Périmètre hérité :** Consultation d'une ressource fictive ; pas de SQL libre, shell, URL libre ni écriture sur sources.
- **Critères de la US parente (références, pas preuve de couverture de cette tâche) :** [`CA-FIL-301-01`](../../../user-stories/US-FIL-301.md#ca-fil-301-01), [`CA-FIL-301-02`](../../../user-stories/US-FIL-301.md#ca-fil-301-02), [`CA-FIL-301-03`](../../../user-stories/US-FIL-301.md#ca-fil-301-03)

Les clauses et oracles de la spécification parente s'appliquent ; toute modification nécessite une nouvelle revue, pas une adaptation implicite au résultat observé.

## Vérification / sortie

- [ ] Artefact complet correspondant à la phase `Vérifier et soumettre à revue`
- [ ] Source, version, mode et statut déclarés
- [ ] Preuve ou disposition de revue jointe ; la tâche ne devient pas automatiquement `Terminé`

## Questions

Voir [`AMB-08`](../../../../../governance/ambiguities.md#amb-08).
