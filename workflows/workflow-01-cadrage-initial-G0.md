# Workflow 01 — Cadrage Initial, Baselines et Frontières de Confiance (Gate G0)

Ce workflow guide l’équipe dans la mise en place d’un cadre de travail sécurisé, déterministe et mesurable avant toute analyse technique approfondie.

---

## 1. Objectif du workflow

Établir une base saine et partagée en identifiant clairement :
- Le cas d'usage utilisateur et la valeur attendue.
- Les baselines officielles et leurs révisions figées.
- Les frontières de confiance et les permissions accordées aux outils.
- Les décisions qui restent **strictement humaines**.
- Les inconnues de départ, à conserver visibles sans extrapolation.

---

## 2. Déclencheur & Entrées requises

- **Déclencheur :** Démarrage d'un nouveau projet, d'un nouveau lot d'exigences ou d'une nouvelle branche de travail.
- **Entrées :**
  - Répartition des missions : [`travail.md`](../travail.md)
  - Spécification de projet de l'équipe : [`projets/[equipe]/SPEC.md`](../projets/)
  - Sources canoniques et révisions officielles (dépôts Git, tags, commits).

---

## 3. Séquence opératoire détaillée

```text
Étape 1.1 : Qualification du besoin et de l'utilisateur
  ↓
Étape 1.2 : Identification et figeage des baselines
  ↓
Étape 1.3 : Cartographie des permissions (Moindre privilège)
  ↓
Étape 1.4 : Établissement de la baseline de mesure initiale
  ↓
Étape 1.5 : Revue collective et passage de la Gate G0
```

### Étape 1.1 : Qualification du besoin et de l'utilisateur
1. Définir le persona utilisateur (développeur embarqué, ingénieur sûreté, analyste d'exigences).
2. Énoncer le problème concret résolu et le gain opérationnel.
3. Délimiter les **décisions humaines non délégables** :
   - Décision d'acceptation d'un risque.
   - Arbitrage sur une déviation normative.
   - Validation de l'intégration dans `develop`.

### Étape 1.2 : Identification et figeage des baselines
1. Pour chaque source de données consultée, consigner :
   - L'URL officielle ou l'emplacement local.
   - La révision exacte (Tag ou SHA-1 du commit).
   - Le statut formel du document (`Draft`, `Release`, `Candidate`).
2. **Interdiction de mélange :** Consigner formellement la séparation entre les exigences et le code. Par exemple :
   - *Baseline Exigences :* dépôt ou document canonique, révision exacte et statut source.
   - *Baseline Code :* dépôt cible distinct, tag ou commit exact et statut de release.

### Étape 1.3 : Cartographie des permissions (Principe du moindre privilège)
Définir les permissions de l'environnement de travail :
- `ALLOW` (Auto-approuvé) : Lecture de code, recherche sémantique et lexicale (`read`, `grep`, `glob`).
- `CONFIRM / ASK` (Action soumise à validation humaine) : Écriture de nouveaux fichiers dans la branche d'équipe, exécution de compilations ou scripts locaux.
- `DENY` (Action strictement interdite) :
  - Écriture dans `upstream/**` ou sur la branche `main`.
  - Exécution de commandes contenant des tokens ou secrets d'authentification.
  - Tentative de contournement de paywalls ou de protections légales.

### Étape 1.4 : Mesure de la baseline initiale
1. Documenter la situation actuelle sans automatisation (temps estimé ou observé d'une revue manuelle, taux de rework).
2. Définir l'indicateur de valeur nette qui sera mesuré à l'issue du travail.

---

## 4. Critères d'acceptation de la Gate G0

Pour que la Gate G0 soit prononcée franchie, la checklist suivante doit être validée :

- [ ] Le cas d'usage utilisateur et le périmètre d'application sont explicites.
- [ ] Les baselines d'exigences et de code sont identifiées par des commits/tags distincts et non confondus.
- [ ] `upstream/**` est confirmé en lecture seule.
- [ ] Les permissions d'outils appliquent le principe du moindre privilège.
- [ ] Toute sortie générée par une IA est qualifiée de `Proposition` et non de preuve.
- [ ] Les inconnues de départ sont explicitement répertoriées sans invention.

---

## 5. Sortie du workflow

- Fiche de cadrage G0 validée (dans la section correspondante de la SPEC projet).
- Feu vert pour engager le **Workflow 02 (Spécifications & Example Mapping)**.
