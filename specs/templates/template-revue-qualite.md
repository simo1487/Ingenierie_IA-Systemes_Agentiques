# Modèle de Rapport de Revue Qualité & Analyse Statique / Dynamique

Ce document sert à consigner les résultats des contrôles qualité (Cppcheck, linters, SAST, SCA, tests dynamiques) et à opérer le tri humain systématique des alertes et faux positifs.

---

## 1. Métadonnées de la revue

- **Identifiant :** `REV-[OUTIL]-[NUMÉRO]` (ex: `REV-CPP-001`)
- **Composant / Branche revu(e) :** `[Nom du composant ou branche]`
- **Commit examiné :** `[Hash exact du commit]`
- **Outils exécutés :** [ex: Cppcheck 2.21.0, Clang-Tidy 17.0, Flake8, pytest]
- **Relecteur(s) humain(s) :** [Noms des ingénieurs responsables de la décision]
- **Date :** `AAAA-MM-JJ`
- **Statut global :** `Accepté` / `Accepté avec déviations justifiées` / `Bloqué`

---

## 2. Commandes d'exécution et profils

### Profil rapide (Local / Pre-commit)
```bash
[Commande exécutée en local, ex: cppcheck --enable=warning,style --error-exitcode=1 src/]
```
- Code retour : `[0 ou non nul]`
- Temps d'exécution : `[X secondes]`

### Profil complet (CI / Revue formelle)
```bash
[Commande complète incluant toutes les vérifications et rapports XML/HTML]
```

---

## 3. Registre des alertes et tri humain des faux positifs

Pour chaque signalement émis par l'analyse statique ou la revue assistée par IA, une décision humaine argumentée est obligatoire :

| ID Alerte | Outil / Règle | Fichier & Ligne | Description brute de l'alerte | Qualification humaine | Justification technique / Action corrective |
|---|---|---|---|---|---|
| `ALT-01` | Cppcheck / `nullPointer` | `sem.c:142` | Possible null pointer dereference | **Anomalie confirmée** | Patch appliqué dans le PR pour ajouter l'assertion |
| `ALT-02` | Cppcheck / `unreadVariable` | `main.c:88` | Variable 'ret' is assigned a value that is never used | **Faux positif** | Variable inspectée par la macro de test Z_TEST en mode debug |
| `ALT-03` | MISRA C:2012 / `Rule 11.4` | `sem.c:64` | Conversion between pointer and integer | **Déviation documentée** | Nécessaire pour la table d'adresses matérielle du microcontrôleur |

### Typologie des qualifications humaines :
- **Anomalie confirmée (Bloquant) :** Défaut réel nécessitant correction immédiate avant acceptation.
- **Faux positif (Rejeté) :** Alerte non fondée due aux limites de l'analyseur ; motif technique documenté.
- **Déviation documentée (Accepté sous conditions) :** Pratique nécessaire dans le contexte embarqué, tracée et approuvée.

---

## 4. Évaluation de la simplicité et de l'architecture (KISS, YAGNI, SRP)

| Principe | Question de contrôle | Constat de revue | Conforme ? |
|---|---|---|:---:|
| **KISS** (Keep It Simple) | La solution est-elle la plus simple répondant au problème sans artifice ? | [Commentaire] | Oui / Non |
| **YAGNI** (You Aren't Gonna Need It) | Du code générique, prématuré ou inutilisé a-t-il été introduit ? | [Commentaire] | Oui / Non |
| **SRP** (Single Responsibility) | Chaque fonction ou module a-t-il une unique responsabilité bien définie ? | [Commentaire] | Oui / Non |

---

## 5. Synthèse et Décision humaine

- Nombre total d'alertes : `[X]`
- Anomalies corrigées : `[X]`
- Faux positifs identifiés et justifiés : `[X]`
- Déviations approuvées : `[X]`

**Décision d'intégration :**
- [ ] **Accepté pour intégration dans `develop`**
- [ ] **Refusé — Corrections requises sur les alertes : [IDs]**

*Signature du responsable qualité :* `[Nom]` le `AAAA-MM-JJ`.
