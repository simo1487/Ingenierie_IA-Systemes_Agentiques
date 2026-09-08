# Rapport d'organisation des normes du logiciel embarqué automobile

**Périmètre :** véhicules routiers, logiciels embarqués, ECU, calculateurs haute performance, fonctions connectées et systèmes d'aide à la conduite.

**Date du relevé :** 2026-09-08. Les pages officielles doivent être reconsultées avant une décision contractuelle ou réglementaire.

## 1. Résumé exécutif

Il n'existe pas une norme unique couvrant tout le logiciel automobile. L'écosystème est une **pile de contraintes** :

```text
Réglementation / homologation
        ↓
Sécurité fonctionnelle et sécurité de la fonction
        ↓
Cybersécurité et mises à jour
        ↓
Processus d'ingénierie et qualité
        ↓
Architecture, OS, middleware et protocoles
        ↓
Implémentation, codage, tests et preuves
```

Un projet sérieux doit donc construire une matrice reliant : **fonction → danger/menace → exigence → architecture → logiciel → test → preuve → obligation applicable**.

## 2. Les familles de textes

### 2.1 Réglementation et homologation

Les règlements UNECE ne sont pas de simples recommandations techniques : ils peuvent devenir obligatoires selon le pays, le type de véhicule et la date d'homologation.

- **UNECE R155** : cybersécurité du véhicule et système de management de la cybersécurité (CSMS).
- **UNECE R156** : mises à jour logicielles et système de management des mises à jour (SUMS).
- **UNECE R157** : exigences spécifiques aux systèmes d'aide à la conduite automatisée dans son champ d'application.

Ces règlements imposent plutôt un résultat démontrable et une capacité de management/homologation. **ISO/SAE 21434** et **ISO 24089** donnent les cadres d'ingénierie utiles pour produire les preuves ; ils ne remplacent pas le texte réglementaire.

### 2.2 Sécurité du produit

- **ISO 26262** traite les risques dus au comportement défaillant de systèmes électriques/électroniques liés à la sécurité. Elle organise le cycle de vie, l'analyse des risques, les niveaux ASIL, le développement système/matériel/logiciel et la production.
- **ISO 21448 (SOTIF)** traite les risques dus aux insuffisances de la fonctionnalité prévue, de sa spécification ou de ses performances, notamment pour les capteurs, la perception et les ADAS. Elle ne remplace pas ISO 26262 et ne traite pas les menaces de cybersécurité.
- **ISO/TS 5083:2025** fournit un cadre de conception, vérification et validation pour les systèmes de conduite automatisée dans son périmètre ; il complète l'analyse, mais ne constitue pas une homologation universelle.
- **IEC 61508** est un référentiel générique de sécurité fonctionnelle. Il peut servir de référence ou de contexte de transfert, mais une application automobile doit analyser les écarts vers ISO 26262.

### 2.3 Cybersécurité et mises à jour

- **ISO/SAE 21434** organise la cybersécurité sur tout le cycle de vie : concept, développement, production, exploitation, maintenance et fin de vie.
- **ISO/PAS 5112** fournit un guide d'audit du CSMS ; il ne remplace pas une évaluation complète ni ISO 19011.
- **ISO 24089** traite l'ingénierie des mises à jour logicielles du véhicule.
- **ISO/IEC 27001 / 27002** concernent la gouvernance et les contrôles de sécurité de l'information de l'organisation ; elles complètent, mais ne remplacent pas, ISO/SAE 21434.
- **SAE J3061** est à conserver comme document historique et guide de contexte : ISO/SAE 21434 l'a remplacé comme référence principale d'ingénierie automobile.

### 2.4 Processus, qualité et évaluation

- **Automotive SPICE** évalue la capacité des processus d'acquisition, de développement système et logiciel, de gestion des exigences, de vérification, de validation, de configuration et de gestion des changements.
- **ISO/IEC 330xx** fournit la famille générique de modèles de référence et d'évaluation de processus sur laquelle s'appuient des modèles sectoriels.
- **IATF 16949** concerne le système de management de la qualité automobile au niveau organisationnel et de la chaîne fournisseur ; ce n'est pas une norme de conception logicielle seule.
- **ISO 9001** fournit le socle générique de management de la qualité.

Automotive SPICE, ISO 26262 et ISO/SAE 21434 sont complémentaires : l'un évalue la capacité et les preuves du processus, les deux autres définissent des objectifs et activités propres à la sûreté et à la cybersécurité.

### 2.5 Architecture et interopérabilité

- **AUTOSAR Classic** vise les systèmes embarqués fortement contraints, temps réel et prédictibles ; son architecture distingue application, RTE et BSW.
- **AUTOSAR Adaptive** vise des calculateurs haute performance, services et applications dynamiques, notamment pour des fonctions de conduite automatisée et de connectivité.
- **AUTOSAR Foundation** contient des éléments communs aux plateformes.
- **CAN (ISO 11898)**, **LIN (ISO 17987)**, **DoIP (ISO 13400)**, **UDS (ISO 14229)** et **diagnostic sur CAN (ISO 15765)** décrivent des mécanismes de communication ou de diagnostic, pas un cycle de développement complet.
- **ISO 15118** est important pour la communication véhicule-réseau et la recharge des véhicules électriques.
- Les spécifications AUTOSAR, contrairement aux normes ISO, sont publiées par un partenariat industriel et peuvent avoir des releases propres.

### 2.6 Implémentation et règles de codage

- **MISRA C** et **MISRA C++** proposent des règles de développement visant la sûreté, la robustesse et la maintenabilité ; elles sont des lignes directrices et leur statut contractuel dépend du projet.
- **CERT C/C++** apporte des règles de programmation sécurisée, particulièrement utiles en complément de la cybersécurité.
- Les règles doivent être configurées, justifiées et contrôlées par analyse statique, revue et tests. Une liste de règles seule ne constitue pas une preuve de conformité.

## 3. Articulation par cycle de vie

| Étape | Questions | Références principales | Preuves attendues |
|---|---|---|---|
| Cadrage | Quel marché, véhicule, fonction et niveau de criticité ? | UNECE applicable, ISO 26262-2, ISO/SAE 21434 | Applicability matrix, rôles, plan de sécurité |
| Concept | Quels dangers, menaces et objectifs ? | ISO 26262-3, ISO 21448, ISO/SAE 21434 | HARA, TARA, objectifs de sécurité et cyber-objectifs |
| Architecture | Comment allouer et isoler les fonctions ? | ISO 26262-4/5, AUTOSAR, protocoles ISO | Architecture, allocation, interfaces, analyses d'indépendance |
| Développement logiciel | Comment spécifier, coder et intégrer ? | ISO 26262-6, Automotive SPICE, MISRA, AUTOSAR | Exigences, conception, code, revues, analyse statique |
| Vérification/validation | Comment démontrer le comportement ? | ISO 26262, SOTIF, ISO/TS 5083, ISO/SAE 21434 | Tests, couverture, anomalies, validation, scénarios |
| Mise en production | Comment maîtriser les versions ? | ISO 26262-7, UNECE R155/R156, ISO 24089 | Configuration, libération, CSMS/SUMS, rapports |
| Exploitation | Comment surveiller et corriger ? | UNECE R155/R156, ISO/SAE 21434 | Incidents, vulnérabilités, campagne OTA, retour terrain |
| Fin de vie | Comment retirer et tracer ? | ISO/SAE 21434, ISO 24089, exigences client | Décommissionnement, révocation, archivage des preuves |

## 4. Hiérarchie de décision recommandée

1. **Identifier les obligations légales du marché cible.** Une norme volontaire ne peut pas être utilisée pour ignorer un règlement applicable.
2. **Délimiter la fonction et les interfaces.** Documenter ce qui est dans le véhicule, dans l'ECU, dans le cloud, dans l'outil de développement et chez le fournisseur.
3. **Séparer les analyses.** Faire apparaître distinctement HARA/safety, SOTIF, TARA/cyber et qualité/processus, puis relier les interfaces.
4. **Choisir la release technique.** Figer la version AUTOSAR, les protocoles et les outils ; enregistrer les éditions des normes achetées.
5. **Construire les preuves.** Chaque exigence doit avoir une source, un propriétaire, un statut, un lien vers l'implémentation et un résultat de vérification.
6. **Gérer les écarts.** Une déviation, une interprétation ou un tailoring doit être approuvé et justifié ; elle ne doit pas être masquée par une étiquette « conforme ».

## 5. Limites et règles d'utilisation

- Le catalogue n'est pas exhaustif : il couvre les références centrales du logiciel embarqué automobile, pas toutes les normes de composants, CEM, électriques, mécaniques, données personnelles, pays ou OEM.
- Les pages ISO/SAE et SAE peuvent vendre le texte intégral. Le dépôt conserve les métadonnées et les liens officiels, pas les textes protégés.
- « Applicable », « utilisé par l'industrie », « recommandé » et « conforme » sont quatre affirmations différentes.
- Les versions proposées dans `normes.yml` sont des repères de travail issus des pages consultées ; la version à appliquer doit être confirmée dans le catalogue de l'organisme et dans le contrat projet.

## 6. Résultat attendu pour FormationIaProject

Le dossier peut servir de point de départ à :

- une base RAG avec métadonnées et citations ;
- une matrice d'applicabilité par projet ;
- un registre des obligations et des preuves ;
- un tableau de suivi des versions et des écarts ;
- un support pédagogique distinguant réglementation, normes, architecture et bonnes pratiques.
