# Plan — Génération des fiches projets candidats

## Objectif
Créer des fiches projets détaillées pour les 11 projets restants listés dans `projets_controle_moteur_electrique.md` en utilisant le template `template_candidat.json`, en récupérant les informations depuis les dépôts GitHub respectifs.

## Projets à traiter
La fiche CAND-001 (VESC Project) a déjà été créée. Les 11 projets restants sont :

1. **CAND-002** - Tesla Model 3/Y Inverter Firmware (c2000-inverter-M3-Y)
2. **CAND-003** - Cornell Electric Vehicles Motor Controller (CEV_MCont_V1.0)
3. **CAND-004** - Axel BLDC Motor Controller Framework (axel)
4. **CAND-005** - FOC King (FOC_KING)
5. **CAND-006** - Vehicle Management Unit (VMU)
6. **CAND-007** - Infineon IMR Motor Control (IMR_IMD701_MC)
7. **CAND-008** - NXP PMSM FOC Motor Control (an-mc-pmsm-foc-2sh-s32k344)
8. **CAND-009** - OpenVVVF RTE (RTE)
9. **CAND-010** - SF-Motion (sf-motion)
10. **CAND-011** - MiniBLDC TMC6200 (MiniBLDC_TMC6200_v2)
11. **CAND-012** - PCBasPRO Cheap FOC2VESC (PCBasPRO_0002_Cheap_FOC2VESC)

## Méthodologie par projet

Pour chaque projet, suivre ce processus :

### Étape 1 : Récupération informations de base
Depuis `projets_controle_moteur_electrique.md` :
- Nom du projet
- URL GitHub
- Description technique
- Application ciblée
- Informations de licence (si disponibles)

### Étape 2 : Analyse du dépôt GitHub
Via API GitHub et webfetch :
- **Informations dépôt** : API GitHub pour stars, forks, commits, activité
- **README** : Contenu du README.md pour documentation et instructions
- **Licence** : Vérification fichier LICENSE ou badge dans README
- **Structure du dépôt** : Exploration arborescence pour identifier :
  - Fichiers d'exigences (requirements, spec, etc.)
  - Fichiers de tests
  - Configuration CI/CD (.github/workflows, .gitlab-ci.yml, etc.)
  - Documentation technique

### Étape 3 : Recherche exigences formelles
- Exploration complète de l'arborescence via API GitHub (`git/trees/master?recursive=1`)
- Recherche de fichiers contenant des termes : "requirements", "spec", "specification", "exigences"
- Vérification des dossiers documentation/, docs/, requirements/, spec/
- Analyse des fichiers PDF ou documents externes mentionnés

### Étape 4 : Remplissage du template
Créer fichier `fiche_cand_XXX_nom.json` avec les sections :

**Informations d'identification**
- ID candidat (CAND-002 à CAND-012)
- Nom, URL, révision, domaine principal

**Licence et légal**
- Licence observée (avec fichier source)
- Statut de réutilisation
- Notes sur la licence

**Activité du projet**
- Statut, dernier commit, fréquence, contributeurs
- Définition d'activité appliquée (commit < 30 jours = actif)

**Documentation**
- README principal, documentation externe
- Qualité de la documentation

**Exigences**
- Fichiers d'exigences identifiés (ou "Aucun")
- Format, nombre, complétude
- Traçabilité exigences → code

**Tests**
- Fichiers de tests, framework, couverture, types

**Mécanismes qualité**
- CI/CD (outil, fichier, statut)
- Contrôles qualité (linting, revues, checks automatisés)

**Traçabilité**
- Relations explicites, outils, liens

**Évaluation selon la grille**
- CA-OSS-01 à CA-OSS-07 avec statuts et preuves

**Points forts / Limites**
- Basés sur l'analyse du dépôt

**Recommandation**
- Statut, justification, alternatives

### Étape 5 : Création du fichier
- Nom du fichier : `fiche_cand_XXX_nom_projet.json`
- Format : JSON selon template_candidat.json
- Emplacement : même dossier que template_candidat.json

## Ordre de traitement
Traitement séquentiel des projets CAND-002 à CAND-012 dans l'ordre de la liste.

## Critères de qualité
- Chaque affirmation technique doit être sourcée (fichier/commit/tag précis)
- Les données absentes doivent être explicitement marquées "Non vérifié"
- Respect strict du format du template
- Reproductibilité : révision figée pour chaque analyse

## Livrables attendus
- 11 fichiers de fiches projets (fiche_cand_002_*.json à fiche_cand_012_*.json)
- Chaque fiche complète avec informations disponibles depuis GitHub
- Évaluation selon les critères CA-OSS-01 à CA-OSS-07 du SPEC.md

## Risques et mitigations
- **Dépôt inaccessible** : Marquer comme "Non vérifié" et continuer
- **Licence non trouvée** : Marquer comme "À vérifier" et signaler dans limites
- **Exigences absentes** : Confirmer par exploration complète et marquer explicitement
- **API rate limiting** : Espacer les requêtes et utiliser webfetch alternatif

---

**Créé le :** 2026-09-09
**Statut du plan :** Prêt pour approbation et exécution
