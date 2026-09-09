# SPEC — Chaîne de contrôles qualité reproductibles

## 1. Informations générales

- **Identifiant projet :** `PROJ-QUAL-001`
- **Équipe :** Qualité du code
- **Responsables :** Eric, Céline et Damien
- **Branche :** `feat_Cppcheck`
- **Statut :** `Draft`
- **Mission source :** « Recherche de contrôles qualité statiques et dynamiques » dans `travail.md`
- **Dernière mise à jour :** `2026-09-09`

## 2. Vision et Epic

### `EPIC-QUAL-001` — Détecter les défauts avant intégration

- **Vision :** proposer une chaîne minimale de contrôles statiques et dynamiques utilisable localement et en intégration.
- **Bénéficiaire principal :** développeur et relecteur.
- **Valeur attendue :** obtenir les mêmes diagnostics reproductibles avant qu’un changement soit intégré.
- **Indicateur de succès :** un tiers exécute les profils documentés et observe un échec sur un défaut contrôlé.

> En tant que développeur ou relecteur, je veux lancer les mêmes contrôles localement et en intégration afin de détecter les défauts reproductibles et de disposer d’un rapport exploitable.

## 3. Périmètre

### Inclus

- Cadrage explicite de la cible, des langages et de la chaîne de build.
- Comparaison d’outils statiques et d’approches dynamiques compatibles.
- Sélection justifiée d’un ensemble minimal versionné.
- Profils rapide et complet, cas de succès, défaut connu et outil absent.
- Rapport exploitable et proposition d’intégration dans un hook partagé ou une CI.

### Exclus

- Déclaration d’absence totale de défauts ou certification automatique.
- Correction silencieuse du code analysé.
- Blocage global du dépôt avant validation humaine du prototype.
- Exécution d’un outil non approuvé avec des secrets ou privilèges étendus.

## 4. Parties prenantes et décisions humaines réservées

| Partie prenante | Responsabilité | Décision réservée |
|---|---|---|
| Développeur | Exécuter et corriger les contrôles | Accepter ou corriger une anomalie confirmée |
| Relecteur qualité | Examiner les rapports | Classer faux positifs et déviations |
| Responsable d’intégration | Définir les contrôles bloquants | Activer un blocage local ou CI |

## 5. Entrées et baselines

| Entrée | Source canonique | Révision / date | Accès | Statut |
|---|---|---|---|---|
| Code cible | À sélectionner dans le portefeuille | Commit à figer | Lecture durant l’analyse | `Bloqué` |
| Système de build et tests existants | README du projet cible | Version à relever | Exécution contrôlée | `Non vérifié` |
| Outils candidats | Documentation et paquets officiels | Versions à sélectionner | Installation locale | `Candidat` |

## 6. Sorties et preuves attendues

| Sortie | Type d’information | Oracle indépendant |
|---|---|---|
| Matrice de comparaison | `Proposition` | Documentation officielle, licences et essai contrôlé |
| Configuration versionnée | `Observation` | Lecture de la configuration et version de l’outil |
| Rapport d’exécution | `Preuve vérifiée` | Code retour, sortie de l’outil et défaut injecté connu |
| Décision sur les alertes | `Proposition` puis décision humaine | Revue contradictoire documentée |

## 7. User Stories

### `US-QUAL-001` — Cadrer la cible

> En tant que responsable qualité, je veux connaître la cible, ses langages et ses commandes de build et de test afin de choisir des contrôles applicables.

- `RM-QUAL-001` — Aucun outil n’est déclaré compatible sans cible et version identifiées.
- **Nominal :** le projet cible fournit une commande de build reproductible.
- **Frontière :** un projet sans tests dynamiques reste analysable statiquement mais la lacune est visible.
- **Contre-exemple :** une cible inconnue interdit de déclarer la sélection terminée.
- **Critères associés :** `CA-QUAL-01`, `CA-QUAL-08`.

### `US-QUAL-002` — Comparer et sélectionner les contrôles

> En tant que relecteur, je veux comparer plusieurs outils selon une grille commune afin de retenir une chaîne compatible et justifiée.

- `RM-QUAL-002` — Version, licence, commande, couverture et limites sont consignées pour chaque candidat.
- **Nominal :** les candidats sont évalués avec les mêmes critères.
- **Frontière :** un outil pertinent mais indisponible est conservé comme alternative bloquée.
- **Contre-exemple :** un outil choisi sans exécution contrôlée reste `Candidat`.
- **Critères associés :** `CA-QUAL-02`, `CA-QUAL-03`.

### `US-QUAL-003` — Exécuter un profil rapide

> En tant que développeur, je veux une commande rapide qui retourne un statut fiable afin de détecter un défaut bloquant avant revue.

- `RM-QUAL-003` — Un contrôle non exécuté ne peut jamais être déclaré réussi.
- **Nominal :** tous les outils requis s’exécutent et le résumé indique versions et statuts.
- **Frontière :** aucun fichier applicable produit un état explicite, pas un succès trompeur.
- **Contre-exemple :** un défaut connu ou un outil requis absent empêche le succès global.
- **Critères associés :** `CA-QUAL-04`, `CA-QUAL-05`, `CA-QUAL-06`.

### `US-QUAL-004` — Revoir et reproduire les résultats

> En tant que relecteur qualité, je veux retrouver les commandes, alertes, exclusions et limites afin de reproduire l’analyse et décider humainement de chaque signalement.

- `RM-QUAL-004` — Faux positifs et déviations nécessitent une justification humaine.
- **Nominal :** un tiers reproduit le rapport à partir de la documentation.
- **Frontière :** une alerte indécidable reste ouverte.
- **Contre-exemple :** une exclusion non documentée invalide la revue.
- **Critères associés :** `CA-QUAL-07`, `CA-QUAL-08`.

## 8. Critères d’acceptation de l’Epic

- [ ] `CA-QUAL-01` — La cible, sa révision, ses langages et ses commandes de build et de test sont définis.
- [ ] `CA-QUAL-02` — Au moins deux outils statiques et deux approches dynamiques sont comparés selon une même grille.
- [ ] `CA-QUAL-03` — Le choix des outils et versions est justifié par des observations reproductibles.
- [ ] `CA-QUAL-04` — Le profil rapide est exécutable avec une commande documentée.
- [ ] `CA-QUAL-05` — Un défaut contrôlé produit un code non nul et un diagnostic localisable.
- [ ] `CA-QUAL-06` — L’absence d’un outil requis produit un échec ou un état inconclusif visible.
- [ ] `CA-QUAL-07` — Une autre personne peut reproduire les contrôles dans l’environnement documenté.
- [ ] `CA-QUAL-08` — Les limites, exclusions, faux positifs et éléments non testés sont listés.

## 9. Scénarios Gherkin et oracles indépendants

```gherkin
Fonctionnalité: Exécuter des contrôles qualité reproductibles

  Scénario: Profil rapide réussi
    Étant donné une cible compilable et les outils requis installés
    Quand le profil rapide est lancé
    Alors les contrôles configurés sont exécutés
    Et le résultat indique leurs commandes, versions et statuts

  Scénario: Aucun fichier applicable
    Étant donné une cible ne contenant aucun fichier reconnu par un contrôle
    Quand le profil rapide est lancé
    Alors le contrôle indique qu’aucun fichier n’a été analysé
    Et le résultat n’est pas assimilé silencieusement à une preuve d’absence de défaut

  Scénario: Défaut bloquant connu
    Étant donné une fixture contenant un défaut attendu
    Quand le profil rapide est lancé
    Alors la commande retourne un code non nul
    Et le rapport localise la cause

  Scénario: Outil requis absent
    Étant donné qu’un outil requis n’est pas disponible
    Quand le contrôle est lancé
    Alors aucun succès global n’est annoncé
    Et l’installation manquante est indiquée
```

| Scénario | User Story | Critères | Oracle indépendant |
|---|---|---|---|
| Profil réussi | `US-QUAL-003` | `CA-QUAL-04` | Liste configurée des contrôles et traces d’exécution |
| Aucun fichier | `US-QUAL-003` | `CA-QUAL-08` | Fixture vide connue avant implémentation |
| Défaut connu | `US-QUAL-003` | `CA-QUAL-05` | Fixture fautive approuvée et code retour du processus |
| Outil absent | `US-QUAL-003` | `CA-QUAL-06` | Environnement contrôlé sans l’exécutable |

## 10. Traçabilité Epic → Stories → preuves

| Epic | User Story | Règle | Critères | Livrable / preuve | Statut |
|---|---|---|---|---|---|
| `EPIC-QUAL-001` | `US-QUAL-001` | `RM-QUAL-001` | `CA-QUAL-01/08` | Fiche de cible | `Bloqué` |
| `EPIC-QUAL-001` | `US-QUAL-002` | `RM-QUAL-002` | `CA-QUAL-02/03` | Matrice de comparaison | `Candidat` |
| `EPIC-QUAL-001` | `US-QUAL-003` | `RM-QUAL-003` | `CA-QUAL-04/05/06` | Scripts, fixtures et rapports | `Candidat` |
| `EPIC-QUAL-001` | `US-QUAL-004` | `RM-QUAL-004` | `CA-QUAL-07/08` | Rapport de revue | `Candidat` |

## 11. Risques, ambiguïtés et questions ouvertes

| ID | Description | Décision attendue | Statut |
|---|---|---|---|
| `AMB-QUAL-001` | Le code cible, les langages et le build ne sont pas sélectionnés. | Choisir et figer la cible avant la sélection finale des outils. | `Ouvert` |
| `AMB-QUAL-002` | Les budgets de durée local et CI ne sont pas fixés. | Définir les seuils des profils rapide et complet. | `Ouvert` |
| `AMB-QUAL-003` | Les catégories d’anomalies bloquantes ne sont pas approuvées. | Faire arbitrer la politique de Gate. | `Ouvert` |

## 12. Définition de terminé

L’Epic est terminée lorsqu’une cible figée dispose de profils rapide et complet reproductibles, qu’un défaut contrôlé est détecté, que l’absence d’outil reste visible et que les décisions sur alertes et blocages sont consignées par un humain.
