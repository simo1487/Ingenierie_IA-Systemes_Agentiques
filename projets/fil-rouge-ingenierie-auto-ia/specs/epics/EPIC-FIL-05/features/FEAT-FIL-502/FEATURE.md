# FEAT-FIL-502 — Bloquer une intégration dépourvue de preuves

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-05`](../../EPIC.md)
- **User Story parente :** [`US-FIL-502`](../../user-stories/US-FIL-502.md)
- **Jour :** `J08`
- **Sources de formation :** [`C03-RETOUR`](../../../../baseline/sources.md#c03-retour) — `J03` / Plan préalable, bornes et comparaisons des tests générés, concurrence, doubles, contrôles dans la chaîne / `retour_rapporte`<br>[`C08`](../../../../baseline/sources.md#c08) — `J08` / Quatre verdicts, risques gouvernés, preuves bornées et coût complet / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Extension production`
- **Priorité :** `P2`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** relecteur intégration — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Lot de fichiers, tests hors ligne, liens de specs, résultats de non-régression et politique de revue existante.
- **Sortie :** Observations de contrôles ciblés et globaux séparées, défauts attribués au périmètre ; décision humaine d'intégration.
- **Périmètre :** Préparation des contrôles ; aucune modification de protection de branche ni fusion automatique.
- **Règle canonique :** [`RM-FIL-502`](../../user-stories/US-FIL-502.md#rm-fil-502)
- **Critères canoniques :** [`CA-FIL-502-01`](../../user-stories/US-FIL-502.md#ca-fil-502-01), [`CA-FIL-502-02`](../../user-stories/US-FIL-502.md#ca-fil-502-02), [`CA-FIL-502-03`](../../user-stories/US-FIL-502.md#ca-fil-502-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-502-01`](tasks/TASK-FIL-502-01.md) | Lister les contrôles et leurs périmètres, avec traitement explicite de l'héritage en échec du monorepo. | Spécifier et figer l'oracle | [`US-FIL-401`](../../../EPIC-FIL-04/user-stories/US-FIL-401.md), [`US-FIL-402`](../../../EPIC-FIL-04/user-stories/US-FIL-402.md), [`US-FIL-501`](../../user-stories/US-FIL-501.md) |
| [`TASK-FIL-502-02`](tasks/TASK-FIL-502-02.md) | Prévoir l'automatisation des tests et de l'intégrité des specs dans la chaîne existante sans modifier les politiques de sécurité. | Réaliser dans le périmètre autorisé | [`TASK-FIL-502-01`](tasks/TASK-FIL-502-01.md) |
| [`TASK-FIL-502-03`](tasks/TASK-FIL-502-03.md) | Éprouver un lien cassé et un test critique en échec puis faire relire les preuves avant toute intégration autorisée. | Vérifier et soumettre à revue | [`TASK-FIL-502-02`](tasks/TASK-FIL-502-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-502.md#oracle-indépendant) : Codes retour réels et journaux de contrôle ; jeu de liens cassés/IDs orphelins pour les specs ; absence de résultat interprétée non exécuté.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-502-01`](../../user-stories/US-FIL-502.md#ca-fil-502-01)
- [ ] [`CA-FIL-502-02`](../../user-stories/US-FIL-502.md#ca-fil-502-02)
- [ ] [`CA-FIL-502-03`](../../user-stories/US-FIL-502.md#ca-fil-502-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-14`](../../../../governance/ambiguities.md#amb-14) reste ouverte.
