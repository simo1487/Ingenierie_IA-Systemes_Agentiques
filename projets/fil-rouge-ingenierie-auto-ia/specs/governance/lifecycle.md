# Référence — Cycle de vie documentaire, travail et preuve

## Statuts indépendants

| Dimension | Valeurs autorisées | Sens |
|---|---|---|
| Documentaire | `Draft`, `Candidate`, `In Review`, `Validated` | Maturité du document, sans présumer le travail ni la preuve |
| Travail | `À faire`, `Prêt`, `En cours`, `En revue`, `Terminé`, `Bloqué` | État de réalisation |
| Trace | `Observé`, `Candidat`, `Vérifié`, `Non vérifié`, `Bloqué` | Force de la relation ou de la preuve |
| Information | `Proposition`, `Observation`, `Preuve vérifiée`, `Question ouverte` | Nature de l’énoncé ou de l’artefact |

Une case de critère cochée ne constitue ni une auto-approbation ni une décision de Gate.

## Definition of Ready

Une spécification `Candidate` peut être prête à discuter lorsque ses identifiants, sources, inconnues, exemples et oracle proposé sont explicites. Cela ne signifie pas qu’elle est prête à implémenter.

Une Story ou tâche ne passe à `Prêt` pour implémentation que si :

- les identifiants parent et enfant sont présents ;
- l’oracle indépendant est approuvé ;
- les dépendances de capacité sont explicites et un artefact existant peut les satisfaire après revue ;
- les décisions bloquantes sont résolues ou font l’objet d’une disposition humaine explicite ;
- le rôle et la personne responsable sont nommés avant exécution.

Le nombre de cas et de tâches dépend du besoin. Les familles nominal, frontière et refus restent le minimum de revue ; Gherkin est conservé par convention du dépôt, sans être présenté comme obligation universelle du cours J02.

## Definition of Done

Le statut `Terminé` exige un artefact réalisé et une preuve indiquant le mode, les versions, le résultat et ses limites, puis une revue attribuée. Une violation critique n’est pas compensée par un score agrégé. Un chemin prévu, une commande non exécutée ou un champ non vide ne vaut pas preuve.

## Gates distinctes

- `G0` valide le cadrage ; `G1` examine spécifications, tests et traçabilité v0 ; `G2` examine la chaîne de preuves qualité, mutation et documentation. La revue d’intégration sur `develop` suit ces Gates dans un workflow distinct.
- Le [workflow racine](../../../../workflows/README.md) décrit l’enchaînement de ces Gates et de la revue d’intégration.
- `G0` à `G4` représentent les acquis J01–J05 à examiner comme prérequis ; ils ne sont pas présumés franchis et ne créent pas automatiquement de nouveaux devoirs.
- `G5/J06`, `G6/J07` et `G7/J08` sont les Gates pédagogiques futures des journées correspondantes.
- Une Gate pédagogique ne remplace pas une Gate de revue du dépôt, et inversement.
- Le backlog n’enregistre aucune Gate comme déjà franchie.

## Transfert vers un outil de suivi

Aucune création d’issue Jira ou GitHub n’est autorisée par ce lot. Les identifiants `EPIC`, `US`, `FEAT` et `TASK` sont transférables ultérieurement sans prétendre que des tickets existent déjà.
