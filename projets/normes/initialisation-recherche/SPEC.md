# SPEC — Initialisation de la recherche de normes

## 1. Informations générales

- **Identifiant :** `PROJ-NORM-INIT-001`
- **Branche :** `feat/initSearchSystem`
- **Projet parent :** Normes
- **Mission associée :** préparer le système de récupération et d’organisation des normes
- **Statut initial :** Prototype

## 2. Objectif

Fournir à l’équipe Normes une structure reproductible pour recenser les références applicables au logiciel embarqué automobile, conserver leurs métadonnées et récupérer uniquement les ressources accessibles légalement.

## 3. Besoin utilisateur

> En tant que membre de l’équipe Normes, je veux disposer d’un catalogue sourcé et d’un mécanisme de récupération contrôlé afin de préparer le nettoyage et l’analyse des références sans perdre leur provenance.

## 4. Périmètre

### Inclus

- Catalogue des normes, règlements, référentiels de processus et règles de codage.
- Métadonnées : identifiant, titre, organisme, édition, URL officielle, accès et statut.
- Script de récupération des ressources publiquement accessibles.
- Manifeste des tentatives, succès et échecs de téléchargement.
- Documentation d’utilisation et limites du corpus.

### Exclus

- Contournement d’authentification, de paiement ou de protection technique.
- Copie intégrale d’un texte protégé sans autorisation.
- Extraction ou validation détaillée des exigences, réalisée dans `feat/GetNormes`.
- Déclaration de conformité d’un projet.

## 5. Livrables attendus

- Un catalogue machine-readable en YAML ou CSV.
- Une liste de sources officielles et datées.
- Un script de récupération relançable sans secret.
- Un manifeste indiquant le résultat de chaque tentative.
- Un rapport expliquant les catégories retenues et les limites.

## 6. Règles

- Privilégier les organismes officiels et les dépôts des éditeurs.
- Marquer une édition inconnue comme telle au lieu de la deviner.
- Un accès refusé est enregistré comme refusé, jamais contourné.
- Le script ne remplace pas un fichier existant sans comportement documenté.
- Les documents volumineux ou non redistribuables ne sont pas ajoutés automatiquement.

## 7. Critères d’acceptation

- [ ] `CA-NORM-INIT-01` : chaque entrée possède un identifiant stable, un titre et une source.
- [ ] `CA-NORM-INIT-02` : l’édition et la date de consultation sont enregistrées ou marquées inconnues.
- [ ] `CA-NORM-INIT-03` : le script distingue succès, redirection, accès refusé et erreur réseau.
- [ ] `CA-NORM-INIT-04` : aucune restriction d’accès n’est contournée.
- [ ] `CA-NORM-INIT-05` : une autre personne peut relancer le script à partir de la documentation.
- [ ] `CA-NORM-INIT-06` : le catalogue reste exploitable même lorsqu’une source n’est pas téléchargeable.

## 8. Scénarios de vérification

```gherkin
Fonctionnalité: Initialiser le corpus de normes

  Scénario: Ressource publique disponible
    Étant donné une entrée contenant une URL officielle accessible
    Quand le script de récupération est exécuté
    Alors la ressource est enregistrée dans l’emplacement prévu
    Et le manifeste conserve sa source et le statut de succès

  Scénario: Ressource protégée
    Étant donné une ressource nécessitant un achat ou une authentification
    Quand le script reçoit un refus d’accès
    Alors aucun contournement n’est tenté
    Et le manifeste indique que la ressource n’a pas été récupérée
```

## 9. Passage à l’équipe Normes

Le prototype est transmissible lorsque le catalogue est lisible, que les téléchargements sont traçables et que l’équipe `feat/GetNormes` peut commencer l’extraction sans rechercher de nouveau la provenance des documents.
