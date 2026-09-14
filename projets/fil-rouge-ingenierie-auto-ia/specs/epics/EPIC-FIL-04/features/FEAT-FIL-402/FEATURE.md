# FEAT-FIL-402 — Éprouver une protection par sa régression

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-04`](../../EPIC.md)
- **User Story parente :** [`US-FIL-402`](../../user-stories/US-FIL-402.md)
- **Jour :** `J07`
- **Sources de formation :** [`C03`](../../../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation / `support_actuel`<br>[`C07-G6`](../../../../baseline/sources.md#c07-g6) — `J07` / Outil préparé ou replay, refus avant accès, régression et première divergence ; G6 / `programme_prevu`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** relecteur sécurité — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Cas hostile versionné, copie isolée de test et garde d'autorisation identifié ; mutation défensive contrôlée.
- **Sortie :** Observations rouge/vert et mutation avec versions, code retour et décision de revue.
- **Périmètre :** Mutation ciblée défensive en environnement isolé ; aucune désactivation de politique de dépôt.
- **Règle canonique :** [`RM-FIL-402`](../../user-stories/US-FIL-402.md#rm-fil-402)
- **Critères canoniques :** [`CA-FIL-402-01`](../../user-stories/US-FIL-402.md#ca-fil-402-01), [`CA-FIL-402-02`](../../user-stories/US-FIL-402.md#ca-fil-402-02), [`CA-FIL-402-03`](../../user-stories/US-FIL-402.md#ca-fil-402-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-402-01`](tasks/TASK-FIL-402-01.md) | Choisir le contrôle local à muter et figer le cas qui observe réellement l'accès. | Spécifier et figer l'oracle | [`US-FIL-3`](../../../EPIC-FIL-00/user-stories/US-FIL-3.md), [`US-FIL-401`](../../user-stories/US-FIL-401.md) |
| [`TASK-FIL-402-02`](tasks/TASK-FIL-402-02.md) | Réaliser rouge/vert et mutation sur une copie isolée, conserver les résultats sans exposer de données réelles. | Réaliser dans le périmètre autorisé | [`TASK-FIL-402-01`](tasks/TASK-FIL-402-01.md) |
| [`TASK-FIL-402-03`](tasks/TASK-FIL-402-03.md) | Faire revoir la première cause de l'échec et démontrer que la protection et l'environnement d'origine sont préservés. | Vérifier et soumettre à revue | [`TASK-FIL-402-02`](tasks/TASK-FIL-402-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-402.md#oracle-indépendant) : MES-02 ; attendu fixe zéro accès hors portée ; échec du test fondé sur compteur d'accès, pas sur sa propre chaîne de log.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-402-01`](../../user-stories/US-FIL-402.md#ca-fil-402-01)
- [ ] [`CA-FIL-402-02`](../../user-stories/US-FIL-402.md#ca-fil-402-02)
- [ ] [`CA-FIL-402-03`](../../user-stories/US-FIL-402.md#ca-fil-402-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-11`](../../../../governance/ambiguities.md#amb-11) reste ouverte.
