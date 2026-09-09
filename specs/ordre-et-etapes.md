# Guide Méthodologique : Les Points et Étapes à Respecter dans l'Ordre Strict

Ce document constitue le référentiel d'ingénierie obligatoire du projet. Il synthétise les enseignements des trois premiers jours de formation (**J01**, **J02**, **J03**) et détaille la **séquence chronologique stricte** à suivre pour chaque exigence, feature, enquête de bogue ou intégration.

```text
┌──────────────┐     ┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│  ÉTAPES 1-2  │ ──> │  ÉTAPES 3-5  │ ──> │  ÉTAPES 6-9  │ ──> │   ÉTAPE 10   │
│   Cadrage    │     │  Spécif & G1 │     │ Preuves & G2 │     │ Intégration  │
│  & Baselines │     │  Example Map │     │  Red-Green   │     │  Fact-Check  │
└──────────────┘     └──────────────┘     └──────────────┘     └──────────────┘
```

---

## Vue synoptique de la séquence ordonnée

| Ordre | Étape | Démarche clé | Règle non négociable | Livrable / Sortie | Gate |
|:---:|---|---|---|---|:---:|
| **1** | **Cadrage & Frontières** | Définir utilisateur, besoin et permissions | `upstream/**` en lecture seule ; séparer proposition et preuve | Fiche de cadrage | **G0** |
| **2** | **Audit de l'Exigence** | Vérifier clarté, singularité, baseline | Ne jamais inventer une information absente | Registre d'ambiguïtés | — |
| **3** | **Example Mapping** | Éliciter règles, cas nominaux, limites | Explorer contre-exemples avant tout code | Fiche Example Map | — |
| **4** | **Gherkin & Oracles** | Formaliser scénarios et oracles | Proscrire tout test tautologique | Scénarios Gherkin | — |
| **5** | **Matrice Traçabilité v0** | Chaîner exigence ↔ doc ↔ code ↔ test | Similarité lexicale ≠ relation de preuve | Matrice v0 JSON | **G1** |
| **6** | **Enquête Scientifique** | Isoler observation brute vs hypothèses | Ne jamais corriger sans reproduire | Fiche de reproduction | — |
| **7** | **Cycle Red-Green** | Test discriminant rouge puis patch minimal | Respecter KISS, YAGNI, SRP | Preuve ROUGE + VERT | — |
| **8** | **Épreuve par Mutation** | Tester la sensibilité aux faux correctifs | Le test muté doit obligatoirement échouer | Rapport de mutation | — |
| **9** | **Contrôle & Revue IA** | Cppcheck, linters, tri des alertes | Décision humaine sur les faux positifs | Rapport de revue | — |
| **10** | **Doc-as-Code & Fact-Check** | Diátaxis, Mermaid, fact-checking | Chaque affirmation = source + test | Matrice fact-check | **G2** |

---

## Étape 1 : Cadrage, Baselines et Frontières de Confiance (J01 / Gate G0)

> **Règle d'ordre :** Ne JAMAIS commencer à analyser le code ou concevoir des tests avant d'avoir formellement calé le périmètre, les baselines et les permissions.

### Points à respecter impérativement :
1. **Identifier le besoin réel et l'arbitrage humain :** Qui est l'utilisateur ? Quel est le risque évité ? Quelles décisions restent **exclusivement humaines** (acceptation de risques, conformité légale, validation d'architecture) ?
2. **Figer les baselines de référence :**
   - Identifier le dépôt cible, le tag exact, le commit SHA et la date de consultation.
   - **Interdiction formelle de confondre deux baselines :** dans le fil rouge Zephyr, la baseline d'exigences (`reqmgmt-2026-08-31`, commit `b9e70278...`) est au statut `Draft` et est distincte du code noyau Zephyr (`v4.4.2`, commit `dccb0959...`).
3. **Appliquer le principe de moindre privilège (Permissions) :**
   - `ALLOW` : Lecture seule sur le dépôt, analyse de code, outils de recherche (grep, glob, read).
   - `CONFIRM / ASK` : Écriture de code, exécution de scripts modifiant l'environnement, création de branches.
   - `DENY` : Toute écriture dans `upstream/**`, suppression irréversible, exécution de commandes arbitraires avec secrets, contournement de paywalls/contrôles d'accès.
4. **Typologie fondamentale de l'information (J01) :**
   - Toute sortie générée par une IA est une **Proposition**.
   - Tout extrait textuel relevé dans les sources sans extrapolation est une **Observation**.
   - Tout résultat d'une commande exécutée avec succès est une **Preuve vérifiée**.
   - Tout point manquant ou incertain est une **Question ouverte** qui doit rester visible.

---

## Étape 2 : Audit de l'Exigence Brute & Détection des Ambiguïtés (J02)

> **Règle d'ordre :** Prendre l'énoncé de l'exigence tel qu'il a été écrit, sans chercher à deviner ce que le code fait.

### Points à respecter impérativement :
1. **Séparer les niveaux d'exigence :**
   - Exigence Système (besoin utilisateur / véhicule / système global).
   - Exigence Logicielle (spécification fonctionnelle d'un composant, API, contrat d'interface).
2. **Évaluer la qualité intrinsèque :**
   - *Singularité :* L'exigence exprime-t-elle une seule chose à la fois ?
   - *Clarté & Non-ambiguïté :* Le vocabulaire est-il précis (ex: éviter « rapide », « optimisé », « suffisant ») ?
   - *Vérifiabilité :* Existe-t-il un moyen technique de concevoir un test capable de prouver son respect ou sa violation ?
3. **Formaliser les ambiguïtés :**
   - Si une information manque (ex: que se passe-t-il si un paramètre est NULL ou dépasse la borne ?), consigner le doute dans le **Registre d'ambiguïtés**.
   - **Interdiction :** L'assistant IA ne doit jamais inventer une décision technique pour masquer une lacune de spécification.

---

## Étape 3 : Example Mapping & Table de Décision (J02)

> **Règle d'ordre :** Extraire les règles métier et leurs exemples concrets AVANT toute rédaction de scénarios formels ou de code.

### Points à respecter impérativement :
1. **Identifier les règles métier sous-jacentes :** Chaque exigence encapsule une ou plusieurs règles concrètes.
2. **Pour chaque règle, dériver la triade d'exemples :**
   - **Exemple nominal :** Cas d'utilisation normal avec données valides.
   - **Exemple aux limites (frontière) :** Valeur min, max, compteur à zéro, capacité pleine, timeout nul.
   - **Contre-exemple (erreur / refus) :** Entrée invalide, ressource saturée, appel interdit en contexte d'interruption (ISR).
3. **Construire la table de décision si conditions multiples :**
   - Lister toutes les combinaisons d'entrées et l'action attendue pour chaque ligne.
4. **Isoler les questions ouvertes :** Toute question bloquante doit être signalée avant l'étape suivante.

---

## Étape 4 : Scénarios Gherkin & Oracles Indépendants (J02)

> **Règle d'ordre :** Définir la condition d'oracle AVANT de regarder l'implémentation ou de coder le test.

### Points à respecter impérativement :
1. **Rédiger en syntaxe Gherkin standard :**
   - `Fonctionnalité`, `Contexte`, `Scénario`, `Étant donné`, `Quand`, `Alors`, `Et`.
2. **Couvrir l'ensemble du spectre comportemental :**
   - Scénarios nominaux.
   - Scénarios aux limites et de robustesse.
   - Scénarios d'erreur (code retour d'erreur, exception levée, non-altération de l'état).
   - Scénarios temporels ou asynchrones (timeouts, réinitialisation, concurrence, ISR).
3. **Garantir l'indépendance de l'oracle :**
   - Un oracle doit être capable de **contredire** une implémentation erronée.
   - **Interdiction absolue des tests tautologiques :** un test qui reproduit la logique interne du code ou qui utilise une assertion triviale (`assert(true)`) ne démontre rien et doit être rejeté.

---

## Étape 5 : Matrice de Traçabilité v0 & Validation Gate G1 (J02)

> **Règle d'ordre :** Consigner la chaîne de traçabilité en lecture seule et franchir formellement la Gate G1.

### Points à respecter impérativement :
1. **Établir le chaînage complet :**
   - `Exigence (UID, texte, baseline)` ↔ `Documentation / API publique` ↔ `Code source (fichier, ligne, fonction)` ↔ `Suite de tests (fichier, test, oracle)`.
2. **Appliquer les 5 statuts autorisés :**
   - `Vérifié` : Preuve formelle existante et testée.
   - `Candidat` : Lien proposé par l'analyse, en attente de démonstration runtime.
   - `Observé` : Élément constaté dans les sources brutes sans lien démontré.
   - `Non vérifié` : Absence de lien ou implémentation introuvable.
   - `Bloqué` : Dépendance manquante ou décision suspendue.
3. **Règle anti-hallucination :** Une ressemblance lexicale (mêmes mots) ne constitue jamais une preuve de couverture.
4. **Schéma JSON fermé :** Exporter la matrice dans un format JSON validé par schéma strict.
5. **Passage de la Gate G1 :**
   - [ ] Toutes les exigences auditées possèdent un statut et une baseline.
   - [ ] Les scénarios couvrent nominaux, frontières et erreurs avec des oracles indépendants.
   - [ ] Le plan de travail est resté strictement en lecture seule.

---

## Étape 6 : Enquête Scientifique Falsifiable & Fiche de Reproduction (J03)

> **Règle d'ordre :** Ne JAMAIS modifier une seule ligne de code pour corriger un bogue sans avoir d'abord reproduit le symptôme dans une démarche scientifique falsifiable.

### Points à respecter impérativement :
1. **Observer sans interpréter (Fait brut) :**
   - Noter exactement ce qui s'est passé (commande exacte, log brut, valeur lue, code retour).
   - Ne pas mélanger le symptôme constaté avec une théorie explicative.
2. **Formuler au moins deux hypothèses explicatives concurrentes :**
   - $H_1$ : Explication causale A (ex: débordement de tampon lors du release).
   - $H_2$ : Explication causale B (ex: mauvaise gestion du contexte thread vs ISR).
3. **Concevoir un test discriminant :**
   - Créer une expérience dont le résultat éliminera au moins l'une des hypothèses (falsification au sens poppérien).
4. **Remplir la Fiche de Reproduction (`ENQ-*`) :**
   - Environnement précis, révision Git, commande unique rejouable, comportement attendu vs comportement observé.

---

## Étape 7 : Preuve ROUGE & Cycle Red–Green–Refactor (J03)

> **Règle d'ordre :** Le test doit être exécuté et échouer (ROUGE) avant d'écrire le correctif.

### Points à respecter impérativement :
1. **Obtenir et archiver la preuve ROUGE :**
   - Exécuter le test discriminant.
   - Constater l'échec et vérifier qu'il échoue **pour la raison identifiée** (et non à cause d'une erreur de compilation, de syntaxe ou d'environnement).
2. **Rédiger le correctif minimal (Patch KISS, YAGNI, SRP) :**
   - **KISS :** Solution la plus simple et directe possible.
   - **YAGNI :** Aucun code d'anticipation, aucune généralisation prématurée.
   - **SRP :** Ne toucher qu'au comportement incriminé, une seule responsabilité par modification.
   - **Interdiction de refactorisation opportuniste :** Ne pas reformater ou réécrire du code adjacent sans rapport avec le défaut.
3. **Obtenir et archiver la preuve VERTE :**
   - Rejouer exactement la même commande de test.
   - Constater le succès (code retour 0).
   - Rejouer l'ensemble de la suite de non-régression.

---

## Étape 8 : Épreuve par Mutation / Faux Correctif (J03)

> **Règle d'ordre :** Prouver la sensibilité et la robustesse du test avant de considérer la correction comme acquise.

### Points à respecter impérativement :
1. **Principe :** Un test qui passe peut être aveugle si son assertion est trop faible.
2. **Méthode de mutation conceptuelle :**
   - Introduire une altération intentionnelle dans le code de production corrigé (ex: changer `<` en `<=`, supprimer la décrémentation, ou injecter un faux correctif plausible généré par une IA).
3. **Vérification de détection :**
   - Relancer le test : le test **DOIT ÉCHOUER**.
   - Si le test passe malgré la mutation, l'oracle est défaillant ou incomplet.
4. **Restauration :**
   - Restaurer immédiatement le code propre validé.

---

## Étape 9 : Contrôles Qualité Automatisés & Tri Humain des Alertes (J03)

> **Règle d'ordre :** Les outils statiques et l'IA émettent des signaux ; l'ingénieur humain effectue le tri et prend la décision.

### Points à respecter impérativement :
1. **Exécution des contrôles qualité :**
   - Analyse statique (Cppcheck, clang-tidy, linters).
   - Vérification des règles de codage (ex: MISRA, règles Zephyr).
2. **Tri humain obligatoire des signalements :**
   - Ne jamais faire confiance aveugle à un scanner ou à une revue IA.
   - Pour chaque alerte, consigner une décision argumentée :
     - **Anomalie confirmée :** bogue ou non-conformité réelle → correction obligatoire.
     - **Faux positif :** alerte sans fondement due aux limites de l'analyseur → justification technique consignée.
     - **Déviation documentée :** pratique acceptée et tracée dans le contexte embarqué.
3. **Consignation dans le rapport de revue (`REV-*`).**

---

## Étape 10 : Doc-as-Code Diátaxis, Fact-Checking & Gate G2 (J03)

> **Règle d'ordre :** Aucune documentation n'est réputée valide tant que chaque affirmation technique n'a pas été formellement vérifiée contre le code réel.

### Points à respecter impérativement :
1. **Adopter l'architecture documentaire Diátaxis :**
   - Séparer nettement *Tutoriel*, *Guide pratique (How-To)*, *Référence technique* et *Explication*.
2. **Fact-Checking documentaire systématique (`FACT-*`) :**
   - Extraire chaque phrase de la documentation affirmant un comportement technique.
   - Relier l'affirmation à sa **source canonique** (fichier code, ligne, en-tête d'API).
   - Associer une **commande de check** ou un test vérifiant l'affirmation.
   - Statuts de vérité : `Prouvé`, `Partiellement vrai`, `Non prouvé (à retirer)`, `Contredit (erreur critique)`.
3. **Vérifier les diagrammes Mermaid :**
   - Contrôler la syntaxe et la conformité stricte des séquences d'appels avec le code réel.
4. **Passage de la Gate G2 :**
   - [ ] Défaut reproduit avec trace rouge archivée.
   - [ ] Patch minimal appliqué et validé par trace verte rejouable.
   - [ ] Test de mutation exécuté avec succès (sensibilité prouvée).
   - [ ] Alertes qualité triées avec justifications humaines des faux positifs.
   - [ ] Documentation Diátaxis auditée avec matrice de fact-checking.
   - [ ] `upstream/**` rigoureusement intact.
5. **Intégration finale :**
   - Synchroniser la branche avec `develop`.
   - Soumettre la PR avec le dossier de preuves G2 complet pour revue croisée par les pairs.
