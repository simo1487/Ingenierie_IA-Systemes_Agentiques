# Exemple de spécification : vérifications statique et dynamique

> **Note d'architecture :** Ce fichier constitue un exemple instancié (`FEAT-QUAL-001`). Le modèle générique réutilisable est disponible dans [`specs/templates/template-feature-spec.md`](specs/templates/template-feature-spec.md). L'architecture globale des spécifications et les règles documentaires sont définies dans [`specs/README.md`](specs/README.md).

Cette fiche décrit la feature proposée. Les choix d'outillage qui ne sont pas encore arrêtés restent explicitement ouverts.

## 1. Informations générales

- **Identifiant :** `FEAT-QUAL-001`
- **Nom de la feature :** Vérification qualité statique et dynamique avant validation d'un commit
- **Epic parente :** `EPIC-QUAL-001`
- **User Story parente :** `US-QUAL-003`
- **Responsable(s) :** Équipe Qualité du code : Eric, Céline et Damien
- **Priorité :** `P1`
- **Statut :** Proposée
- **Date :** `2026-09-08`

## 2. Objectif

Cette feature permet d'exécuter automatiquement une vérification statique et une vérification dynamique avant l'acceptation d'un commit, tout en permettant à un développeur ou à un relecteur de relancer les contrôles à la demande. Elle doit détecter tôt les défauts reproductibles et conserver un résultat exploitable pour la revue.

## 3. Besoin utilisateur

> En tant que développeur ou relecteur, je veux lancer les contrôles qualité automatiquement lors d'un commit ou manuellement, afin de détecter les défauts avant intégration et de disposer d'une preuve reproductible pour la revue.

## 4. Contexte et problème

- **Situation actuelle :** la cible, ses commandes de build et de test ainsi que les contrôles applicables restent à identifier et à figer avant le prototype.
- **Problème rencontré :** un commit peut être créé sans analyse statique ni exécution de tests ; les résultats ne sont donc ni systématiques ni facilement comparables.
- **Décision qui reste humaine :** décider si une anomalie est acceptable, corriger ou justifier une exception, et autoriser l'intégration lorsque le contrôle est inconclusif ou incomplet.
- **Question ouverte :** quels sont le langage, la commande de compilation et le framework de tests de la cible à contrôler ?

## 5. Périmètre

### Inclus

- Un contrôle statique déclenchable automatiquement avant la création du commit.
- Un contrôle dynamique déclenchable dans le même parcours, selon un profil rapide adapté au commit.
- Une commande explicite pour relancer les contrôles manuellement, avec un profil complet possible.
- Un code retour permettant d'accepter ou de bloquer le commit.
- La production d'un rapport horodaté et associé au commit ou à l'exécution.
- Une documentation d'installation, d'utilisation et de dépannage.

### Exclus

- La correction automatique du code ou la suppression automatique d'une anomalie.
- La décision humaine d'accepter un risque ou de déclarer une conformité réglementaire.
- La certification du logiciel ou la preuve que les contrôles couvrent tous les défauts possibles.
- Les tests matériels nécessitant une carte ou un banc non disponible localement, sauf décision ultérieure.

## 6. Entrées

| Entrée | Source | Version / date | Statut | Accès autorisé |
|---|---|---|---|---|
| Code source et fichiers de configuration | Dépôt Git | Version du commit contrôlé | À vérifier | Lecture |
| Configuration du contrôle statique | Dépôt Git | À définir et versionner | Candidat | Lecture |
| Commande de compilation et tests | Projet cible | À définir | À vérifier | Exécution |
| Rapport d’analyse existant | Projet cible à sélectionner | Version à relever | Observation à analyser | Lecture |
| Environnement d'exécution | Machine locale ou CI | Versions à figer | À vérifier | Lecture |

## 7. Sorties attendues

- Statut du contrôle : succès, échec, inconclusif ou non exécuté.
- Rapport statique listant les anomalies, leur gravité, leur fichier et leur ligne.
- Résultat dynamique : compilation, tests exécutés, tests réussis et tests échoués.
- Journal de commande, versions des outils et identifiant du commit contrôlé.
- Message lisible dans le terminal indiquant l'action à effectuer en cas d'échec.

Pour chaque sortie, préciser si elle constitue :

- une **proposition** ;
- une **observation** ;
- une **preuve vérifiée** ;
- une **question ouverte**.

## 8. Règles métier et contraintes

- Le contrôle doit être déterministe à environnement et commit identiques, ou signaler explicitement les facteurs non déterministes.
- Une anomalie statique de gravité bloquante ou un test dynamique échoué bloque le commit par défaut.
- Un outil absent, une compilation impossible ou un test non exécuté ne doit pas être présenté comme un succès.
- Le développeur peut relancer le contrôle complet manuellement, mais ne peut pas masquer un échec sans justification et revue humaine.
- Les outils et leurs versions doivent être documentés et, autant que possible, verrouillés.
- Aucun secret, fichier personnel ou artefact volumineux ne doit être ajouté au dépôt par le mécanisme de contrôle.

## 9. Critères d'acceptation

- [ ] `CA-01` : un commit déclenche automatiquement le profil rapide statique et dynamique configuré.
- [ ] `CA-02` : une anomalie bloquante ou un test échoué renvoie un code non nul et empêche le commit.
- [ ] `CA-03` : une commande manuelle permet de lancer le profil rapide et le profil complet sans modifier le code.
- [ ] `CA-04` : le résultat indique clairement les contrôles exécutés, ignorés ou en échec.
- [ ] `CA-05` : le rapport conserve le commit, les versions des outils, les commandes et les résultats.
- [ ] `CA-06` : un contrôle interrompu ou incomplet n'est jamais classé comme réussi.
- [ ] `CA-07` : un relecteur peut reproduire le contrôle en suivant la documentation.
- [ ] Les sources, versions et statuts sont conservés.
- [ ] Les informations inconnues restent explicitement ouvertes.
- [ ] Aucune preuve de conformité n'est revendiquée sans vérification.

## 10. Scénarios Gherkin

```gherkin
Fonctionnalité: Vérification qualité avant validation d'un commit

  Contexte:
    Étant donné un dépôt contenant le code et la configuration du projet
    Et les outils requis installés dans les versions documentées

  Scénario: Contrôles réussis avant un commit
    Étant donné un changement qui ne produit aucune anomalie bloquante
    Quand le développeur lance la création du commit
    Alors le contrôle statique et le profil dynamique configuré sont exécutés
    Et le commit est accepté avec un rapport associé au commit contrôlé

  Scénario: Contrôle manuel complet
    Étant donné un dépôt dans un état compilable
    Quand un relecteur lance explicitement le profil complet
    Alors les résultats détaillés sont affichés et enregistrés

  Scénario: Échec bloquant
    Étant donné une anomalie statique bloquante ou un test dynamique échoué
    Quand le développeur lance la création du commit
    Alors le contrôle renvoie un code non nul
    Et le commit est refusé avec la cause et le chemin du rapport

  Scénario: Outil ou test indisponible
    Étant donné qu'un outil requis est absent ou qu'un test ne peut pas être exécuté
    Quand le contrôle est lancé
    Alors le résultat est inconclusif ou en échec
    Et aucune réussite globale n'est annoncée
```

### Couverture des scénarios

| Scénario | Critère couvert | Source de l'attendu | Oracle / observation | Statut |
|---|---|---|---|---|
| Contrôles réussis avant un commit | CA-01, CA-05 | Cette spécification | Code retour nul, rapport et identifiant du commit | Candidat |
| Contrôle manuel complet | CA-03, CA-04 | Cette spécification | Rapport complet et commandes rejouables | Candidat |
| Échec bloquant | CA-02, CA-06 | Cette spécification | Code retour non nul et commit non créé | Candidat |
| Outil ou test indisponible | CA-04, CA-06 | Cette spécification | Statut inconclusif ou échec visible | Candidat |

## 11. Traçabilité

| Élément | Source ou identifiant | Relation | Preuve / passage | Statut |
|---|---|---|---|---|
| Exécuter une analyse statique | FEAT-QUAL-001 | Configuration et commande statique | À définir avec l'outil retenu | Candidat |
| Exécuter une vérification dynamique | FEAT-QUAL-001 | Compilation et tests du projet | Commande de test à définir | Candidat |
| Bloquer un commit défectueux | FEAT-QUAL-001 | Hook de commit ou équivalent CI | Code retour non nul attendu | Candidat |
| Produire une preuve reproductible | FEAT-QUAL-001 | Rapport et documentation | Commit, versions, commandes, résultats | Candidat |
| État actuel du contrôle statique | Rapport du projet cible à sélectionner | Observation vers rapport statique | Présence et contenu du rapport à qualifier | Non vérifié |

> Une proximité de vocabulaire, un nom de fichier ou la présence d'un test ne suffit pas à prouver une relation.

## 12. Vérification

La procédure exacte dépend de l'outillage du projet, qui doit encore être arrêté. La procédure cible est la suivante.

1. Installer les versions documentées des outils et récupérer le dépôt.
2. Lancer le profil rapide avec la commande documentée, puis vérifier son code retour.
3. Modifier volontairement un cas de test ou introduire une anomalie contrôlée dans un environnement de démonstration.
4. Vérifier que le contrôle échoue, que le commit est refusé et que le rapport identifie la cause.
5. Annuler cette modification de démonstration et relancer le profil complet manuellement.

- **Environnement :** dépôt Git ; système local et éventuellement CI ; versions des outils à figer.
- **Données utilisées :** code du dépôt, configuration versionnée, tests et données de test non sensibles.
- **Résultat attendu :** contrôle terminé avec statut, code retour et rapport consultable.
- **Limites de la vérification :** elle ne démontre pas l'absence de tous les défauts, la conformité à une norme, ni le comportement sur matériel réel non testé.

## 13. Dépendances et risques

### Dépendances

- Définition du projet cible, de sa commande de compilation et de son framework de tests.
- Choix des outils statique et dynamique, de leurs versions et de leurs seuils de gravité.
- Accès à un environnement reproductible ; éventuellement installation d'un hook partagé et d'un runner CI.
- Décision sur le temps maximal acceptable pour un commit.

### Risques

| Risque | Impact | Probabilité | Mesure de maîtrise | Responsable |
|---|---|---|---|---|
| Contrôle trop lent pour un commit | Fort | Moyen | Profil rapide au commit, profil complet manuel ou CI | Équipe Qualité du code |
| Faux positifs ou règles mal configurées | Moyen | Moyen | Revue des règles, seuils versionnés et exceptions justifiées | Équipe Qualité du code |
| Environnement local différent de la CI | Fort | Moyen | Versions documentées et exécution reproductible | À désigner |
| Tests dynamiques incomplets | Fort | Moyen | Mesurer la couverture et documenter les limites | À désigner |
| Rapport Cppcheck non interprétable à cause d'inclusions manquantes | Moyen | Élevé | Corriger les chemins de compilation ou classer le résultat inconclusif | Équipe Qualité du code |

## 14. Décision de revue

- **Relecteur(s) :** Équipe Qualité du code et responsable du dépôt
- **Date de revue :** À planifier
- **Décision :** À revoir
- **Corrections demandées :** choisir les outils, les commandes, les seuils et le mode d'installation du hook.
- **Points restant ouverts :** langage et cible exacts ; commande de build ; framework de tests ; durée maximale du profil commit ; conservation des rapports ; politique d'exception.

## Checklist finale

- [ ] Le besoin utilisateur est compréhensible.
- [ ] Le périmètre et les exclusions sont explicites.
- [ ] Les entrées et leurs versions sont identifiées ou signalées comme à définir.
- [ ] Les sorties sont distinguées des preuves.
- [ ] Les critères d'acceptation sont observables.
- [ ] Il existe au moins un scénario nominal.
- [ ] Il existe au moins un scénario frontière, erreur ou refus.
- [ ] Chaque scénario possède un attendu et un oracle.
- [ ] Les relations de traçabilité sont sourcées.
- [ ] Les inconnues ne sont pas inventées.
- [ ] La vérification est reproductible par une autre personne une fois l'outillage arrêté.
- [ ] Les limites et risques sont documentés.
