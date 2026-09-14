# FEAT-FIL-1 — Choisir une assistance proportionnée au besoin

`Référence — feature candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-00`](../../EPIC.md)
- **User Story parente :** [`US-FIL-1`](../../user-stories/US-FIL-1.md)
- **Jour :** `J01–J05`
- **Sources de formation :** [`C01`](../../../../baseline/sources.md#c01) — `J01` / Mécanisme proportionné, données, hébergement et souveraineté distincts / `support_actuel`<br>[`C05`](../../../../baseline/sources.md#c05) — `J05` / Besoin avant framework, règle/recherche/workflow/agent et valeur observable / `support_actuel`<br>[`N05`](../../../../baseline/sources.md#n05) — `J05` / Approches simples, types, budgets, contrôle humain et structuration ; propos à confirmer / `synthese_automatique`
- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** responsable produit — personne à désigner

Cette Feature détaille la User Story parente ; elle ne crée pas une exigence indépendante.

## Contrat candidat

- **Entrée :** Fiche de besoin révisée : résultat utile, utilisateurs, données admises, destinations de traitement, actions permises et décideur ; modèle et hébergement envisagés séparément.
- **Sortie :** Proposition de mécanisme minimal avec justification, alternative et questions ouvertes ; aucune autorisation d'accès déduite du modèle choisi.
- **Périmètre :** Cadrage et lecture des acquis J01/J05 ; aucun framework, runtime ou fournisseur nouveau imposé, aucune clé manipulée.
- **Règle canonique :** [`RM-FIL-1`](../../user-stories/US-FIL-1.md#rm-fil-1)
- **Critères canoniques :** [`CA-FIL-1-01`](../../user-stories/US-FIL-1.md#ca-fil-1-01), [`CA-FIL-1-02`](../../user-stories/US-FIL-1.md#ca-fil-1-02), [`CA-FIL-1-03`](../../user-stories/US-FIL-1.md#ca-fil-1-03)

Aucune surface future n'est affirmée comme présente ; son emplacement reste à décider avant réalisation. La baseline actuelle est décrite dans [`current-state.md`](../../../../baseline/current-state.md). Les noms de modules futurs ne sont pas présentés comme existants.

## Découpage exécutable

| Tâche | Objectif | Phase | Dépendances |
|---|---|---|---|
| [`TASK-FIL-1-01`](tasks/TASK-FIL-1-01.md) | Rassembler le besoin, les actions permises et la classification des données, en séparant faits et hypothèses. | Spécifier et figer l'oracle | Aucune |
| [`TASK-FIL-1-02`](tasks/TASK-FIL-1-02.md) | Comparer les mécanismes nécessaires à ce besoin et décrire les flux de données, y compris repli et télémétrie envisagés. | Réaliser dans le périmètre autorisé | [`TASK-FIL-1-01`](tasks/TASK-FIL-1-01.md) |
| [`TASK-FIL-1-03`](tasks/TASK-FIL-1-03.md) | Faire examiner la justification et les droits de traitement ; conserver les décisions non prises sans revendiquer une architecture approuvée. | Vérifier et soumettre à revue | [`TASK-FIL-1-02`](tasks/TASK-FIL-1-02.md) |

La livraison et les tests sont planifiés ; aucune tâche n'est exécutée par cette spécification.

## Vérification prévue

L'oracle à appliquer est celui de la [`User Story parente`](../../user-stories/US-FIL-1.md#oracle-indépendant) : Revue de la fiche de besoin par le responsable et confrontation au tableau des mécanismes de J05 ; la présence d'un framework ou l'exécution locale ne prouvent ni nécessité ni sûreté.

Les limites d'interruption, de concurrence ou de documentation applicables restent celles des cas de la User Story. Aucun retour de code supplémentaire n'est inventé ici.

## Acceptation

- [ ] [`CA-FIL-1-01`](../../user-stories/US-FIL-1.md#ca-fil-1-01)
- [ ] [`CA-FIL-1-02`](../../user-stories/US-FIL-1.md#ca-fil-1-02)
- [ ] [`CA-FIL-1-03`](../../user-stories/US-FIL-1.md#ca-fil-1-03)

Le responsable nominatif et la décision d'acceptation restent à décider. Les décisions demeurent humaines et [`AMB-19`](../../../../governance/ambiguities.md#amb-19) reste ouverte.
