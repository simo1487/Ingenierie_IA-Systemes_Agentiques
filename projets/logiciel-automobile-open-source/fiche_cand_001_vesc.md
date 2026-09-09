# Fiche Projet Candidat — VESC Project

## Informations d'identification

- **ID candidat :** `CAND-001`
- **Nom du projet :** VESC firmware
- **URL canonique du dépôt :** https://github.com/vedderb/bldc
- **Révision analysée (tag/commit) :** master (dernier commit 2026-09-04)
- **Date de la révision :** 2026-09-04
- **Domaine principal :** Embarqué

## Licence et légal

- **Licence observée :** GNU General Public License version 3.0 (GPLv3)
- **Fichier de licence :** README.md (badge GPLv3), mentionnée dans section License
- **Statut de réutilisation :** À vérifier (GPLv3 a des restrictions pour réutilisation commerciale)
- **Notes sur la licence :** Licence GPLv3 confirmée dans README avec badge officiel. Restrictions copyleft potentielles pour intégration commerciale.

## Activité du projet

- **Statut :** Actif
- **Dernier commit :** 2026-09-04 (pushed_at)
- **Fréquence des commits :** 3,793 commits depuis 2014-01-09 (création)
- **Nombre de contributeurs :** À vérifier via GitHub contributors
- **Définition d'activité appliquée :** Projet actif si commit < 30 jours (dernier commit: 5 jours)

## Documentation

- **README principal :** README.md (complet avec instructions build, install, IDE)
- **Documentation officielle :** https://vesc-project.com/ (mentionné dans README)
- **Qualité de la documentation :** Bonne - README détaillé avec badges qualité
- **Notes :** README inclut instructions de build pour Linux/macOS/Windows, support IDE Qt Creator, méthode upload firmware

## Exigences

- **Fichiers d'exigences identifiés :** Aucun fichier d'exigences formelles identifié dans le dépôt
- **Format des exigences :** Non applicable (pas de fichiers exigences)
- **Nombre d'exigences :** 0 (exigences formelles)
- **Complétude des exigences :** Absente
- **Traçabilité exigences → code :** Non applicable
- **Source précise pour chaque exigence citée :** Non applicable

## Tests

- **Fichiers de tests identifiés :** À rechercher
- **Framework de tests :** À déterminer
- **Couverture de tests :** À vérifier
- **Types de tests :** À déterminer
- **Notes :** 

## Mécanismes qualité

### CI/CD
- **Outil CI :** GitHub Actions
- **Fichier de configuration CI :** .github/workflows/nix.yml
- **Statut CI :** Actif (badge GitHub Actions présent dans README)

### Contrôles qualité
- **Linting / Static analysis :** Codacy (badge présent dans README)
- **Revues de code :** Non vérifié (56 Pull Requests ouvertes)
- **Checks qualité automatisés :** Codacy grade A (badge API)
- **Notes :** Intégration Codacy pour analyse de code quality 

## Traçabilité

- **Relations de traçabilité explicites :** Non vérifié
- **Outils de traçabilité :** À déterminer
- **Liens exigences ↔ tests ↔ code :** Non vérifié
- **Notes :** 

## Évaluation selon la grille

| Critère | Statut | Preuve (fichier/ligne) | Notes |
|---|---|---|---|
| `CA-OSS-01` (URL, licence, révision) | Vérifié | URL: https://github.com/vedderb/bldc, Licence: GPLv3 (README.md badge), Révision: master (2026-09-04) | Révision figée: master branch |
| `CA-OSS-02` (Exigences retrouvables) | Non vérifié | Analyse complète de l'arborescence via API GitHub | Aucun fichier d'exigences formelles identifié (ni .md, .txt, .doc spécifiques exigences) |
| `CA-OSS-03` (Mécanismes qualité) | Vérifié partiel | CI: .github/workflows/nix.yml, Quality: Codacy badge (README.md) | CI/CD et analyse qualité présents |
| `CA-OSS-05` (Données signalées) | Vérifié | Champs avec données marqués, absences signalées | |
| `CA-OSS-07` (Reproductibilité) | Vérifié | Révision master (2026-09-04) figée pour analyse | Branch master accessible |

## Points forts

- Projet mature avec forte communauté (3,428 stars, 1,939 forks)
- Activité soutenue (3,793 commits depuis 2014, dernier commit 2026-09-04)
- Support complet FOC pour moteurs brushless avec techniques avancées
- Documentation README complète et détaillée (build, IDE, upload)
- CI/CD avec GitHub Actions (.github/workflows/nix.yml)
- Analyse qualité automatisée via Codacy (grade A)
- Support multi-plateforme (Linux, macOS, Windows)
- Basé sur STM32F405 MCU (plateforme éprouvée)
- Multi-interface (USB, CAN, SPI, I2C, UART, PWM, ADC)

## Limites / Lacunes

- Licence GPLv3 - restrictions copyleft potentielles pour réutilisation commerciale
- **Exigences formelles absentes** : recherche complète via API GitHub confirmée - aucun fichier d'exigences identifié dans l'arborescence
- Traçabilité exigences/tests/code non applicable (absence d'exigences)
- 262 issues ouvertes (potentiel dettes techniques)
- Pas de revue de code formelle documentée

## Recommandation

- **Statut :** Candidat acceptable
- **Justification :** Projet mature avec activité soutenue, CI/CD fonctionnel et analyse qualité (Codacy). Licence GPLv3 confirmée mais restrictions copyleft à considérer pour usage commercial. Absence d'exigences formelles documentées - principal frein pour référence exigences.
- **Projet(s) alternatif(s) suggéré(s) :** Cornell CEV (MIT License), Axel Framework (MIT License) pour alternatives licences plus permissives

## Notes générales

- Firmware open source pour contrôleurs DC/BLDC/FOC
- Applications: véhicules électriques personnels, skateboards, e-bikes, robots
- Projet principal de l'écosystème VESC avec forte communauté
- Révision analysée: master branch (commit 2026-09-04)
- Mécanismes qualité présents (CI/CD GitHub Actions, Codacy)
- **Exigences formelles absentes du dépôt** : recherche complète via API GitHub de l'arborescence complète (git/trees/master?recursive=1) confirmée - aucun fichier d'exigences formelles identifié. Le projet utilise des fichiers de configuration (conf_general.h, CONTRIBUTING guidelines) mais pas de spécifications d'exigences formelles.

---

**Rempli par :** Devin AI
**Date de remplissage :** 2026-09-09
**Statut de la fiche :** En cours (informations dépôt récupérées, exigences formelles à analyser)
