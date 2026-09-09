# SPEC — Récupération et nettoyage des normes

## 1. Informations générales

- **Identifiant :** `PROJ-NORM-001`
- **Branche :** `feat/GetNormes`
- **Équipe :** Normes
- **Responsables :** Alain et Moustapha
- **Mission source :** « Récupération et nettoyage des normes » dans `travail.md`
- **Statut initial :** En cours

## 2. Objectif

Transformer le corpus initial en un jeu de données propre, sourcé et exploitable pour rechercher des obligations ou recommandations applicables au logiciel embarqué automobile.

## 3. Besoin utilisateur

> En tant qu’analyste d’exigences, je veux consulter des règles normalisées avec leur provenance et leur statut afin de préparer une spécification sans confondre réglementation, norme, guide et interprétation.

## 4. Périmètre

### Inclus

- Déduplication et normalisation des métadonnées du catalogue.
- Classement par réglementation, sûreté, cybersécurité, processus, architecture et codage.
- Extraction d’exigences candidates dans un format tabulaire stable.
- Conservation du passage source ou d’un pointeur précis lorsqu’il est légalement disponible.
- Identification des éditions, dates et restrictions d’accès.
- Rapport sur les doublons, incohérences et informations manquantes.

### Exclus

- Invention du contenu d’une norme indisponible.
- Certification ou avis juridique sur l’applicabilité.
- Mélange d’une reformulation générée avec une citation officielle.
- Téléchargement non autorisé de textes protégés.

## 5. Schéma minimal des exigences

| Champ | Attendu |
|---|---|
| `norme_id` | Identifiant stable de la source |
| `norme_titre` | Titre et édition lorsque connus |
| `categorie` | Famille cohérente et documentée |
| `exigence_id` | Identifiant unique dans le jeu de données |
| `exigence_description` | Citation autorisée ou reformulation explicitement signalée |
| `source` | URL, document et passage précis |
| `statut` | Candidat, vérifié, non vérifié ou bloqué |
| `date_verification` | Date du dernier contrôle humain |

## 6. Livrables attendus

- Un catalogue nettoyé sans doublons non justifiés.
- Un ou plusieurs CSV valides suivant le schéma retenu.
- Une table de correspondance entre les entrées historiques et normalisées.
- Un journal des décisions de nettoyage.
- Une liste des éléments qui nécessitent un accès ou une expertise supplémentaire.

## 7. Règles

- Les identifiants restent stables après publication.
- Une reformulation ne porte pas de guillemets laissant croire à une citation.
- Deux éditions d’une même norme sont deux versions distinctes.
- Une exigence sans passage source reste `Non vérifié`.
- Les catégories proches sont fusionnées uniquement selon une règle documentée.
- Les CSV doivent conserver un en-tête unique, le même nombre de colonnes par ligne et un encodage UTF-8.

## 8. Critères d’acceptation

- [ ] `CA-NORM-01` : chaque exigence possède une source et un statut.
- [ ] `CA-NORM-02` : aucun identifiant d’exigence n’est dupliqué.
- [ ] `CA-NORM-03` : les fichiers tabulaires sont lisibles par un parseur CSV standard.
- [ ] `CA-NORM-04` : les éditions différentes ne sont pas fusionnées silencieusement.
- [ ] `CA-NORM-05` : les affirmations non contrôlées restent signalées comme telles.
- [ ] `CA-NORM-06` : les contenus protégés ne sont pas reproduits sans autorisation.
- [ ] `CA-NORM-07` : un relecteur peut retrouver le passage associé à un échantillon d’exigences.
- [ ] `CA-NORM-08` : le rapport de nettoyage liste les décisions et questions ouvertes.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Nettoyer une exigence issue d’une norme

  Scénario: Exigence traçable
    Étant donné une exigence candidate associée à une édition et un passage source
    Quand un relecteur compare la reformulation au passage
    Alors il peut attribuer le statut Vérifié
    Et la date de vérification est conservée

  Scénario: Source insuffisante
    Étant donné une exigence sans édition ou sans passage retrouvable
    Quand le jeu de données est contrôlé
    Alors l’exigence reste Non vérifié ou Bloqué
    Et elle n’est pas présentée comme une obligation démontrée

  Scénario: Identifiant dupliqué
    Étant donné deux lignes portant le même identifiant
    Quand le contrôle de structure est exécuté
    Alors le contrôle échoue
    Et le doublon doit être fusionné ou renommé avec justification
```

## 10. Définition de terminé

Le travail est terminé lorsqu’un tiers peut parser les données, retrouver la provenance d’un échantillon, distinguer les contenus vérifiés des propositions et reproduire les décisions de nettoyage.
