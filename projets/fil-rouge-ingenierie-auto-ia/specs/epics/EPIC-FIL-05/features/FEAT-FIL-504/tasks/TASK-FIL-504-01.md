# TASK-FIL-504-01 — Définir champs permis, rétention et sources des mesures, sans choisir des seuils de production arbitraires

`Référence — tâche candidate`

- **Epic parente :** [`EPIC-FIL-05`](../../../EPIC.md)
- **User Story parente :** [`US-FIL-504`](../../../user-stories/US-FIL-504.md)
- **Feature parente :** [`FEAT-FIL-504`](../FEATURE.md)
- **Jour :** `J08`
- **Phase :** Spécifier et figer l'oracle
- **Sources héritées :** [`C06`](../../../../../baseline/sources.md#c06) — `J06` / Comparaison d'organisations, rôles, reprise, idempotence, mémoire et trace / `programme_prevu`<br>[`C07`](../../../../../baseline/sources.md#c07) — `J07` / Politique avant accès, révision pédagogique MCP 2026-07-28, contenu non fiable et cas indépendants / `programme_prevu`<br>[`C08`](../../../../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet / `programme_prevu`
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** opérateur — personne à désigner

## Objectif

Définir champs permis, rétention et sources des mesures, sans choisir des seuils de production arbitraires.

## Prérequis

- **Capacités préalables :** [`US-FIL-102`](../../../../EPIC-FIL-01/user-stories/US-FIL-102.md), [`US-FIL-202`](../../../../EPIC-FIL-02/user-stories/US-FIL-202.md), [`US-FIL-503`](../../../user-stories/US-FIL-503.md)
- **Estimation :** non attribuée
- **Date :** non attribuée

Un artefact existant peut satisfaire une capacité préalable après revue ; la tâche ne force pas à refaire un acquis démontré.

## Travail et livrable attendus

**Définir champs permis, rétention et sources des mesures, sans choisir des seuils de production arbitraires**

Produire un artefact relu couvrant les cas et l'oracle de [`US-FIL-504`](../../../user-stories/US-FIL-504.md) dans le mode autorisé.

Un replay ou une fixture prépare la vérification ; il ne suffit pas à prouver l’intégration réelle de l’extension.

- **Entrée héritée :** Événements assainis, politique d'observation versionnée, sources de durée/usage et conditions d'arrêt approuvées.
- **Sortie héritée :** Observations corrélées au run et alertes vers un rôle désigné ; données absentes explicitement non mesurées.
- **Périmètre hérité :** Observabilité minimale locale ; plateforme cloud et seuils de service non choisis implicitement.
- **Critères de la US parente (références, pas preuve de couverture de cette tâche) :** [`CA-FIL-504-01`](../../../user-stories/US-FIL-504.md#ca-fil-504-01), [`CA-FIL-504-02`](../../../user-stories/US-FIL-504.md#ca-fil-504-02), [`CA-FIL-504-03`](../../../user-stories/US-FIL-504.md#ca-fil-504-03)

Les clauses et oracles de la spécification parente s'appliquent ; toute modification nécessite une nouvelle revue, pas une adaptation implicite au résultat observé.

## Vérification / sortie

- [ ] Artefact complet correspondant à la phase `Spécifier et figer l'oracle`
- [ ] Source, version, mode et statut déclarés
- [ ] Preuve ou disposition de revue jointe ; la tâche ne devient pas automatiquement `Terminé`

## Questions

Voir [`AMB-02`](../../../../../governance/ambiguities.md#amb-02).
