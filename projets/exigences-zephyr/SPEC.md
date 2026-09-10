# SPEC — Recherche et analyse des exigences Zephyr

## 1. Informations générales

- **Identifiant :** `PROJ-ZEPHYR-REQ-001`
- **Branche :** `feat_getReq`
- **Équipe :** Exigences Zephyr
- **Responsables :** Mohammed et Florient
- **Mission source :** « Recherche et analyse des exigences de Zephyr » dans `travail.md`
- **Statut initial :** En cours

## 2. Objectif

Constituer un corpus d’exigences Zephyr traçable vers des sources versionnées, puis évaluer lesquelles peuvent alimenter le projet fil rouge sans inventer de relation de conformité automobile.

## 3. Besoin utilisateur

> En tant qu’ingénieur exigences, je veux retrouver chaque exigence Zephyr dans une révision précise et connaître ses liens vérifiés vers le code ou les tests afin de l’utiliser comme référence reproductible.

## 4. Périmètre

### Inclus

- Identification des dépôts officiels contenant les exigences ou documents de conception Zephyr.
- Sélection d’une révision source figée.
- Extraction des identifiants, textes, catégories et relations explicitement disponibles.
- Recherche des liens vers code, tests et documentation.
- Analyse d’écart entre les données trouvées et les besoins de traçabilité automobile.
- Qualification séparée des correspondances proposées vers ISO 26262, ISO/SAE 21434 ou Automotive SPICE.

### Exclus

- Création d’une exigence Zephyr absente des sources.
- Attribution automatique d’une conformité à une norme automobile.
- Confusion entre documentation d’API, comportement observé et exigence normative.
- Analyse de la branche mobile ou de toute source non reliée à la révision retenue.

## 5. Schéma minimal

| Champ | Attendu |
|---|---|
| `requirement_id` | Identifiant original, sans renumérotation silencieuse |
| `requirement_text` | Texte source ou reformulation signalée |
| `source_repository` | Dépôt officiel ou source justifiée |
| `source_revision` | Tag ou SHA exact |
| `source_path` | Fichier et section ou ligne |
| `category` | Catégorie documentée |
| `implementation_links` | Liens observés vers le code |
| `test_links` | Liens observés vers les tests |
| `automotive_mapping` | Proposition séparée et justifiée |
| `status` | Observé, candidat, vérifié, non vérifié ou bloqué |

## 6. Livrables attendus

- Un inventaire des sources Zephyr officielles consultées.
- Une révision de référence explicitement figée.
- Un tableau d’exigences conforme au schéma minimal.
- Une matrice de traçabilité vers le code et les tests lorsqu’elle est démontrable.
- Une analyse des manques et ambiguïtés.
- Une liste séparée de correspondances automobiles candidates.
- Une procédure permettant de reproduire l’extraction.

## 7. Règles

- Un numéro de section sans dépôt, révision et chemin n’est pas une source suffisante.
- Les identifiants originaux sont conservés lorsqu’ils existent.
- Un lien de vocabulaire ne prouve pas une relation de traçabilité.
- Une correspondance vers une norme automobile reste `Candidate` sans revue spécialisée.
- Les exigences générées par un agent sont comparées aux textes sources.
- Une exigence introuvable est marquée `Non vérifié`, jamais reconstituée comme certaine.

## 8. Critères d’acceptation

- [ ] `CA-ZEP-01` : la révision Zephyr ou du dépôt d’exigences est figée.
- [ ] `CA-ZEP-02` : chaque exigence possède un chemin et un passage source retrouvables.
- [ ] `CA-ZEP-03` : les identifiants dupliqués ou inventés sont détectés.
- [ ] `CA-ZEP-04` : les liens vers le code et les tests sont distingués des hypothèses.
- [ ] `CA-ZEP-05` : les correspondances automobiles sont séparées du corpus Zephyr observé.
- [ ] `CA-ZEP-06` : un échantillon est revu manuellement contre la source.
- [ ] `CA-ZEP-07` : la procédure d’extraction est reproductible.
- [ ] `CA-ZEP-08` : les limites de couverture sont documentées.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Tracer une exigence Zephyr

  Scénario: Exigence retrouvée
    Étant donné une exigence associée à un dépôt, une révision et un chemin
    Quand un relecteur ouvre la source indiquée
    Alors il retrouve le passage correspondant
    Et peut confirmer ou refuser le statut Vérifié

  Scénario: Numéro de section ambigu
    Étant donné une exigence qui indique seulement un numéro de section
    Quand la révision et le fichier source ne sont pas connus
    Alors l’exigence reste Non vérifié
    Et elle n’est pas utilisée comme preuve de traçabilité

  Scénario: Correspondance automobile proposée
    Étant donné une exigence Zephyr vérifiée
    Quand un agent propose un lien vers ISO 26262
    Alors ce lien est enregistré séparément avec le statut Candidat
    Et nécessite une revue humaine spécialisée
```

## 10. Définition de terminé

Le travail est terminé lorsqu’un tiers peut retrouver les exigences dans une révision figée, distinguer les liens observés des hypothèses et reproduire l’extraction sans dépendre du contexte conversationnel de l’agent.
