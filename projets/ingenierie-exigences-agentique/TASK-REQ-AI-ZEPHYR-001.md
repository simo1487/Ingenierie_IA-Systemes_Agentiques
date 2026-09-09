# Tâche — Collecte et structuration JSON des exigences Zephyr

## 1. Informations générales

- **Identifiant de tâche :** `TASK-REQ-AI-ZEPHYR-001`
- **Projet parent :** `PROJ-REQ-AI-001`
- **Epic parente :** `EPIC-REQ-AI-001` — Orchestrer une ingénierie des exigences vérifiable
- **User Story parente :** `US-REQ-AI-003` — Auditer et structurer les exigences
- **Baseline complémentaire :** [`projets/exigences-zephyr/SPEC.md`](../exigences-zephyr/SPEC.md) (`PROJ-ZEPHYR-REQ-001`)
- **Responsable(s) :** Mohammed, Florian, Shengjie
- **Branche :** `feat_getReq`
- **Date :** `2026-09-09`
- **Statut :** `Draft`

## 2. Objectif et valeur attendue

Produire, à partir du site de gestion d’exigences Zephyr, un corpus d’exigences structurées en JSON traçable, auditable et prêt à alimenter la chaîne d’ingénierie des exigences agentique. Le corpus doit pouvoir être reproductible par un tiers et ne pas inventer de liens de conformité automobile.

## 3. Besoin utilisateur

> En tant qu’ingénieur exigences,  
> Je veux récupérer les exigences du site Zephyr et les structurer en JSON selon un schéma explicite,  
> Afin de pouvoir les auditer, les relier à leurs sources et les comparer aux besoins du projet sans perdre la provenance de chaque donnée.

## 4. Baselines et sources

| Entrée | Source canonique | Révision / date | Statut d’accès | Niveau de confiance |
|---|---|---|---|---|
| Index des exigences Zephyr | `https://zephyrproject-rtos.github.io/reqmgmt/index.html` | Relevé le `2026-09-09`, pas de révision figée connue | Lecture publique | `Candidat` |
| Schéma minimal d’exigence | `projets/exigences-zephyr/SPEC.md` § 5 | Version en cours | Lecture | `Candidat` |
| Règles d’audit d’exigence | `.devin/skills/audit-exigence/SKILL.md` | Version en cours | Lecture | `Vérifié` |

## 5. Périmètre

### Inclus

- Collecte des pages du site de gestion d’exigences (`software_requirements/` et `system_requirements/`).
- Extraction non destructive du texte, de l’identifiant, du titre et de la catégorie observés.
- Structuration en JSON conforme au schéma ci-dessous.
- Qualification de chaque champ : `Observé`, `Proposition`, `Candidat`.
- Registre des ambiguïtés et exigences non retrouvées.
- Tests écrits **avant** le code de collecte (TDD).

### Exclus

- Écriture, modification ou suppression dans `upstream/**`.
- Déclaration de conformité ISO 26262 / ISO/SAE 21434 / Automotive SPICE.
- Reconstruction d’une exigence absente des sources.
- Traçabilité lexicale non justifiée vers le code ou les tests.

## 6. Schéma JSON attendu

Chaque exigence est un objet de la forme suivante. Le document JSON global est une liste (ou un objet contenant une liste `requirements`) de ces objets.

```json
{
  "requirement_id": "IDENTIFIANT_ORIGINAL_OU_GENERE",
  "requirement_text": "Texte exact ou reformulation signalée",
  "reformulation": false,
  "title": "Titre de l’exigence s’il existe",
  "category": "software_requirements / system_requirements / autre",
  "subcategory": "Nom du sous-document (ex: atomic_service)",
  "source_url": "https://zephyrproject-rtos.github.io/reqmgmt/.../fichier.html",
  "source_path": "...",
  "source_revision": null,
  "status": "Observé",
  "confidence": "Candidat",
  "implementation_links": [],
  "test_links": [],
  "automotive_mapping": [],
  "traceability": {
    "parent_ids": [],
    "child_ids": [],
    "links_source": "page index observée"
  },
  "audit": {
    "singularite": "Candidat",
    "clarte": "Candidat",
    "verifiabilite": "Candidat",
    "questions_ouvertes": []
  },
  "ambiguities": []
}
```

Le document global peut être un objet : `{ "projet": "zephyr", "baseline_url": "...", "date_collecte": "...", "statut": "Proposition", "requirements": [ ... ] }`.

## 7. Règles métier et Example Mapping

### Règle 1 — Identifiant conservé

- **Règle :** Lorsqu’un identifiant d’exigence est visible dans la source, il est conservé sans renumérotation silencieuse.
- **Exemple nominal :** Une page HTML contient `[ZEP-SRS-5-2]` ; le JSON `requirement_id` est `ZEP-SRS-5-2`.
- **Exemple frontière :** L’identifiant est partagé par plusieurs sections ; chaque occurrence est enregistrée avec son `source_path` distinct.
- **Contre-exemple :** Aucun identifiant n’existe ; l’agent ne crée pas `ZEP-SRS-XXX`, il laisse `requirement_id` à `null` et inscrit une ambiguïté.

### Règle 2 — Texte source prioritaire

- **Règle :** `requirement_text` provient du texte source. Toute reformulation est signalée et justifiée.
- **Exemple nominal :** Le texte `<p>Le noyau doit fournir ...</p>` est copié littéralement dans `requirement_text` avec `reformulation: false`.
- **Exemple frontière :** Le texte source contient du HTML ; seul le contenu textuel est conservé, la source HTML est indiquée.
- **Contre-exemple :** L’agent résume l’exigence en neuf mots sans le signaler ; c’est rejeté comme `Proposition` non vérifiée.

### Règle 3 — Source et catégorie documentée

- **Règle :** Chaque exigence indique son `source_url`, sa `category` et sa `subcategory` observés sur le site.
- **Exemple nominal :** `atomic_service.html` produit `category: "software_requirements"`, `subcategory: "atomic_service"`.
- **Exemple frontière :** Un lien est cassé (`404`) ; la page est listée dans le registre d’ambiguïtés avec le code HTTP observé.

### Règle 4 — Pas de conformité automobile auto-attribuée

- **Règle :** Toute correspondance avec une norme automobile est enregistrée dans `automotive_mapping` avec le statut `Candidat`.
- **Exemple nominal :** Une exigence de protection mémoire est **proposée** comme candidate ISO 26262 ; elle est isolée et non pas intégrée au corpus observé.
- **Contre-exemple :** L’agent marque une exigence `ISO 26262 ASIL-D` sans revue humaine ; c’est interdit.

## 8. Critères d’acceptation observables

- [ ] `CA-ZEP-AI-01` : Un run de collecte produit un fichier JSON lisible et conforme au schéma minimal.
- [ ] `CA-ZEP-AI-02` : Chaque exigence JSON possède un `source_url` et un `requirement_text` non vide, ou un `status` explicite `Bloqué`/`Non vérifié`.
- [ ] `CA-ZEP-AI-03` : Aucun identifiant n’est inventé silencieusement ; les identifiants dupliqués ou absents sont signalés dans le registre d’ambiguïtés.
- [ ] `CA-ZEP-AI-04` : Les liens `implementation_links` et `test_links` ne contiennent que des liens observés ou explicitement `Candidat`.
- [ ] `CA-ZEP-AI-05` : Les correspondances automobiles restent séparées du corpus principal.
- [ ] `CA-ZEP-AI-06` : La suite de tests échoue sur l’implémentation initiale (preuve rouge) et passe après le code minimal (preuve verte).
- [ ] `CA-ZEP-AI-07` : Le corpus est reproductible : un second run avec le même point d’entrée produit les mêmes identifiants et textes (hors variations du site).

## 9. Scénarios Gherkin et oracles indépendants

```gherkin
Fonctionnalité: Collecter et structurer les exigences Zephyr en JSON

  Contexte:
    Étant donné le site https://zephyrproject-rtos.github.io/reqmgmt/index.html
    Et le schéma JSON de sortie approuvé
    Et un accès en lecture seule autorisé

  Scénario: Exigence extraite d’une page secondaire
    Quand le collecteur lit la page software_requirements/atomic_service.html
    Alors il produit au moins un objet JSON avec requirement_id, requirement_text, category et source_url
    Et chaque objet est validé par le schéma JSON
    Et le statut de chaque champ est qualifié

  Scénario: Page inaccessible
    Étant donné une URL secondaire retournant 404
    Quand le collecteur tente l’extraction
    Alors aucune exigence n’est inventée
    Et l’échec est consigné dans le registre d’ambiguïtés

  Scénario: Identifiant absent
    Étant donné une section de texte sans identifiant explicite
    Quand le collecteur l’analyse
    Alors requirement_id reste null
    Et une ambiguïté est ajoutée sans valeur générée

  Scénario: Correspondance automobile proposée
    Étant donné une exigence extraite du site
    Quand un agent propose un mapping vers ISO 26262
    Alors le mapping est enregistré dans automotive_mapping
    Et son statut est Candidat
```

### Oracles indépendants

| Scénario | Oracle | Source externe |
|---|---|---|
| Exigence extraite | Un humain ouvre `source_url` et retrouve le texte | Site Zephyr |
| Page inaccessible | Code HTTP observé ou message réseau | Appel HTTP |
| Identifiant absent | Source HTML sans balise d’identifiant | Page HTML |
| Mapping automobile | Absence de référence normative dans le texte source | Norme non atteinte |

## 10. Plan TDD (Test-Driven Development)

### Itération 1 — Schéma et contrat

1. **Écrire en premier** `tests/test_zephyr_schema.py` :  
   - Un fixture JSON minimal (1 exigence valide + 1 invalide).  
   - Le test doit vérifier que le schéma accepte l’objet valide et refuse l’objet invalide.
2. **Faire échouer** ce test : le schéma JSON n’existe pas encore → **Rouge**.
3. **Implémenter** `data/zephyr-requirements.schema.json` pour obtenir le **Vert**.

### Itération 2 — Collecte de l’index

1. **Écrire** `tests/test_zephyr_collector.py` :  
   - Le collecteur appelé avec l’URL d’index doit retourner une liste de sous-pages attendues (`software_requirements/atomic_service.html`, etc.).  
   - Test en mode `pytest` avec une fixture HTML locale.
2. **Rouge** : le collecteur n’existe pas.
3. **Implémenter** `src/zephyr_collector/index_loader.py` minimal.

### Itération 3 — Extraction d’une exigence

1. **Écrire** `tests/test_zephyr_extract.py` :  
   - Étant donné un fichier HTML local d’une page d’exigence, le collecteur produit un JSON avec `requirement_id`, `requirement_text`, `category`, `subcategory`, `source_url`.
2. **Rouge** : l’extracteur n’existe pas.
3. **Implémenter** `src/zephyr_collector/extract.py` jusqu’au **Vert**.

### Itération 4 — Audit et ambiguïtés

1. **Écrire** `tests/test_zephyr_audit.py` :  
   - Une exigence sans `requirement_text` retourne `status: "Bloqué"` et une ambiguïté.  
   - Un identifiant absent retourne `requirement_id: null`.
2. **Rouge** : la fonction d’audit n’existe pas.
3. **Implémenter** `src/zephyr_collector/audit.py`.

### Itération 5 — Non-régression

- Éprouver les tests par une mutation conceptuelle (modifier un identifiant attendu dans le test, vérifier que le test échoue) et un faux correctif.

## 11. Matrice de traçabilité v0

| Exigence / Règle | Source | Test | Implémentation | Statut | Preuve |
|---|---|---|---|---|---|
| Conservation des identifiants | Règle 1 | `tests/test_zephyr_extract.py` | `src/zephyr_collector/extract.py` | Candidat | Page source |
| Texte source prioritaire | Règle 2 | `tests/test_zephyr_extract.py` | `src/zephyr_collector/extract.py` | Candidat | Page source |
| Source documentée | Règle 3 | `tests/test_zephyr_collector.py` | `src/zephyr_collector/index_loader.py` | Candidat | Index HTML |
| Mapping automobile isolé | Règle 4 | `tests/test_zephyr_audit.py` | `src/zephyr_collector/audit.py` | Candidat | SPEC Zephyr |

## 12. Registre d’ambiguïtés

| ID | Description | Décision attendue | Statut |
|---|---|---|---|
| `AMB-ZEP-AI-001` | Aucune révision figée du site web n’est fournie. Quelle date / tag / commit retient-on comme baseline ? | Figer la baseline avec l’équipe | Ouvert |
| `AMB-ZEP-AI-002` | Le format exact HTML de chaque page `.sdoc` générée n’est pas connu. | Fournir un échantillon HTML complet | Ouvert |
| `AMB-ZEP-AI-003` | Les liens `implementation_links` et `test_links` ne sont pas visibles dans la page d’index. | Confirmer la source de ces liens | Ouvert |
| `AMB-ZEP-AI-004` | La catégorisation exacte (`software` vs `system`) repose sur l’arborescence observée. | Valider le mapping | Ouvert |
| `AMB-ZEP-AI-005` | Les correspondances automobiles restent à traiter dans un autre run. | Garder hors du corpus principal | Ouvert |

## 13. Risques et maîtrise

| Risque | Gravité | Probabilité | Mesure de maîtrise |
|---|---|---|---|---|
| Changement du site entre deux collectes | Moyenne | Moyenne | Figer une date de relevé et conserver un cache local |
| HTML non stable | Moyenne | Élevée | Parser le texte visible, pas les balises internes strictes |
| Exigences sans identifiant | Faible | Élevée | Accepter `null`, consigner, ne pas inventer |
| Faux liens automobiles | Élevée | Moyenne | Isoler dans `automotive_mapping` avec statut `Candidat` |

## 14. Definition of Done

La tâche est terminée quand :

- Un fichier JSON conforme au schéma est généré.
- Au moins un test a été écrit avant chaque morceau de code (preuve rouge puis verte).
- Les identifiants, textes et catégories peuvent être vérifiés contre le site source.
- Le registre d’ambiguïtés est à jour.
- Aucune conformité automobile n’est revendiquée sans revue humaine.
