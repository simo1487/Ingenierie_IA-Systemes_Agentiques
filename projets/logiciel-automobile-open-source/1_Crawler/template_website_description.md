# Template — Fiche discriminante d’un site web

> Document de référence pour une extraction. Remplir un champ uniquement lorsqu’il est observé et conserver la source ou la preuve associée. Utiliser `Non vérifié` lorsqu’une information n’a pas été contrôlée.

## 1. Identification du site

| Champ | Valeur | Statut | Source / preuve | Notes |
|---|---|---|---|---|
| Identifiant interne | `SITE-XXX` | À renseigner | | Identifiant stable attribué par l’équipe |
| Nom affiché du site | | À vérifier | | Nom visible dans la page ou les métadonnées |
| Nom de domaine registrable | | À vérifier | | Exemple : `example.org` |
| Sous-domaine | | À vérifier | | Exemple : `docs.example.org` |
| URL canonique déclarée | | À vérifier | | Valeur de `link[rel=canonical]`, si présente |
| URL extraite | | À renseigner | | URL effectivement fournie au crawler |
| URL finale après redirections | | À vérifier | | Conserver la chaîne complète des redirections |
| Type de site | | À qualifier | | Documentation, dépôt, catalogue, blog, forum, portail, autre |
| Domaine fonctionnel | | À qualifier | | Automobile, embarqué, outillage, généraliste, autre |
| Organisation éditrice | | À vérifier | | Nom observé, sans déduction |
| Propriétaire ou éditeur annoncé | | À vérifier | | Distinguer de l’hébergeur |
| Langue(s) détectée(s) | | À vérifier | | Langue de l’interface et langues des contenus |

## 2. Extraction et reproductibilité

| Champ | Valeur | Statut | Source / preuve | Notes |
|---|---|---|---|---|
| Date et heure de début d’extraction (UTC) | | À renseigner | | Format recommandé : `YYYY-MM-DDThh:mm:ssZ` |
| Date et heure de fin d’extraction (UTC) | | À renseigner | | |
| Date de dernière mise à jour visible | | À vérifier | | Ne pas la confondre avec la date d’extraction |
| Version du template | `1.0` | À renseigner | | Version du présent modèle utilisé |
| Version du crawler | | À renseigner | | Commit, tag ou version du logiciel d’extraction |
| Configuration du crawler | | À renseigner | | Référence vers la configuration appliquée |
| Profondeur maximale visitée | | À renseigner | | |
| Nombre de pages demandées | | À renseigner | | |
| Nombre de pages reçues | | À renseigner | | |
| Nombre de pages retenues | | À renseigner | | Règle de filtrage à préciser |
| Identifiant d’exécution | | À renseigner | | Permet de relier les artefacts produits |
| Fuseau horaire utilisé | `UTC` | À renseigner | | Confirmer la valeur réellement utilisée |
| Empreinte de l’archive extraite | | À vérifier | | Algorithme et valeur à préciser |
| Emplacement des preuves | | À renseigner | | Chemin relatif dans `evidence/` ou lien autorisé |

## 3. Version et état du contenu

| Champ | Valeur | Statut | Source / preuve | Notes |
|---|---|---|---|---|
| Version affichée du site | | À vérifier | | Bannière, pied de page, page “À propos”, etc. |
| Version de la documentation | | À vérifier | | Version explicitement publiée |
| Version de l’API ou du produit | | À vérifier | | Si le site en présente une |
| Révision du dépôt associée | | À vérifier | | Tag, release ou commit exact |
| Date de publication de la version | | À vérifier | | |
| Date de dernière release | | À vérifier | | Distinguer d’une date de modification de page |
| Statut annoncé | | À qualifier | | Actif, maintenance, archivé, expérimental, inconnu |
| Pages d’archive ou de versions | | À vérifier | | URL(s) observée(s) |
| Version de la page extraite | | À vérifier | | Hash ou autre identifiant si disponible |

## 4. Empreinte technique du site

| Champ | Valeur | Statut | Source / preuve | Notes |
|---|---|---|---|---|
| Schéma d’URL principal | | À vérifier | | HTTPS, chemins, extensions, paramètres |
| Code HTTP initial | | À vérifier | | Pour l’URL demandée |
| Code HTTP final | | À vérifier | | Pour la ressource finale |
| Chaîne de redirections | | À vérifier | | Liste ordonnée des URLs et codes |
| Type de contenu principal | | À vérifier | | `Content-Type` observé |
| Encodage déclaré | | À vérifier | | En-tête ou balise observée |
| Taille de la réponse | | À vérifier | | Valeur et unité |
| Compression observée | | À vérifier | | En-tête observé |
| Serveur déclaré | | À vérifier | | Valeur d’en-tête, sans en déduire l’infrastructure complète |
| CDN ou proxy déclaré | | À vérifier | | Valeur observée uniquement |
| Technologies détectées | | À vérifier | | Méthode de détection et niveau de confiance à préciser |
| CMS détecté | | À vérifier | | Version seulement si explicitement détectée |
| Framework frontend détecté | | À vérifier | | Version seulement si explicitement détectée |
| Framework backend détecté | | À vérifier | | Version seulement si explicitement détectée |
| Bibliothèques tierces visibles | | À vérifier | | Nom, version, source et méthode de détection |
| Services externes appelés | | À vérifier | | Domaine, type de service, preuve |
| API ou flux publics | | À vérifier | | URL, format, méthode d’accès observée |
| Ressources statiques distinctives | | À vérifier | | Favicon, manifest, fichiers de configuration publics |

## 5. Identité visuelle et structure éditoriale

| Champ | Valeur | Statut | Source / preuve | Notes |
|---|---|---|---|---|
| Titre HTML | | À vérifier | | Balise `title` |
| Description meta | | À vérifier | | Balise `meta description` |
| Balises Open Graph | | À vérifier | | Valeurs observées |
| Image ou logo principal | | À vérifier | | URL et empreinte si conservée |
| Favicon | | À vérifier | | URL et type |
| Thème visuel | | À qualifier | | Description factuelle, sans jugement |
| Structure de navigation | | À vérifier | | Menus, niveaux, liens caractéristiques |
| Types de pages | | À qualifier | | README, référence, actualités, tickets, téléchargements, etc. |
| Formats de contenu | | À vérifier | | HTML, Markdown, PDF, JSON, RSS, autre |
| Recherche interne | | À vérifier | | Présente, absente ou Non vérifié |
| Pagination ou défilement | | À vérifier | | Mécanisme observé |
| Contenu généré côté client | | À vérifier | | Indiquer la méthode d’observation |
| Éléments nécessitant JavaScript | | À vérifier | | Pages ou fonctionnalités concernées |

## 6. Signaux de projet et de versionnement

| Champ | Valeur | Statut | Source / preuve | Notes |
|---|---|---|---|---|
| Dépôt source officiel | | À vérifier | | URL explicitement reliée au site |
| Miroir(s) ou dépôt(s) secondaire(s) | | À vérifier | | Les distinguer du dépôt canonique |
| Plateforme de dépôt | | À vérifier | | GitHub, GitLab, forge propre, autre |
| Licence annoncée | | À vérifier | | Nom exact et emplacement de la preuve |
| Fichier de licence observé | | À vérifier | | Nom du fichier ou URL |
| Releases visibles | | À vérifier | | Dernière release, nombre ou liste selon le besoin |
| Tags ou branches visibles | | À vérifier | | Référence exacte si utilisée |
| Date du dernier commit visible | | À vérifier | | Date et fuseau à conserver |
| Activité récente observable | | À qualifier | | Décrire les observations et la période examinée |
| Documentation liée aux exigences | | À vérifier | | URL ou chemin précis |
| Tests publiés | | À vérifier | | URL ou chemin précis |
| CI/CD publiquement visible | | À vérifier | | URL ou chemin précis |
| Mécanismes qualité visibles | | À vérifier | | Outils, rapports ou workflows observés |

## 7. Accessibilité, droits et contraintes d’extraction

| Champ | Valeur | Statut | Source / preuve | Notes |
|---|---|---|---|---|
| `robots.txt` observé | | À vérifier | | URL, date et contenu pertinent |
| Sitemap observé | | À vérifier | | URL et format |
| Conditions d’utilisation | | À vérifier | | URL et date de consultation |
| Politique de confidentialité | | À vérifier | | URL et date de consultation |
| Licence du contenu | | À vérifier | | Distinguer du logiciel associé |
| Restrictions de réutilisation | | À vérifier | | Reproduire la restriction sans l’interpréter |
| Authentification requise | | À vérifier | | Aucune donnée d’identification ne doit être collectée dans cette fiche |
| Consentement ou bannière nécessaire | | À vérifier | | Décrire uniquement l’observation |
| Limitation de débit observée | | À vérifier | | Réponse, en-tête ou comportement observé |
| Blocage ou refus d’accès | | À vérifier | | URL, date, code et message observés |
| Autorisation d’extraction | | À qualifier | | Décision humaine séparée de l’observation |

## 8. Distinction avec les autres sites

> Renseigner cette section après comparaison avec les autres fiches. Une différence doit renvoyer vers une observation ou une preuve.

| Discriminant | Valeur observée | Comparaison / impact | Preuve | Statut |
|---|---|---|---|---|
| Domaine et sous-domaine | | | | À qualifier |
| URL canonique | | | | À qualifier |
| Organisation éditrice | | | | À qualifier |
| Type et public du site | | | | À qualifier |
| Version ou release de référence | | | | À qualifier |
| Date d’extraction comparable | | | | À qualifier |
| Dépôt canonique associé | | | | À qualifier |
| Licence | | | | À qualifier |
| Empreinte technique | | | | À qualifier |
| Structure et formats de contenu | | | | À qualifier |
| Niveau de documentation | | | | À qualifier |
| Exigences, tests et qualité publiés | | | | À qualifier |
| Politique d’accès et de réutilisation | | | | À qualifier |
| Autre discriminant observé | | | | À qualifier |

## 9. Résumé contrôlé

- **Observation principale :**
- **Éléments qui différencient ce site :**
- **Éléments communs avec d’autres sites :**
- **Informations absentes ou Non vérifiées :**
- **Questions ouvertes :**
- **Décision humaine éventuelle :**

## 10. Contrôle de qualité de la fiche

- [ ] L’URL extraite, l’URL finale et l’URL canonique sont distinguées.
- [ ] La date d’extraction est enregistrée en UTC avec l’identifiant d’exécution.
- [ ] La version du site, de la documentation ou du dépôt est sourcée lorsqu’elle est renseignée.
- [ ] Les versions détectées automatiquement sont accompagnées de leur méthode de détection.
- [ ] Les observations sont séparées des propositions, hypothèses et décisions humaines.
- [ ] Les valeurs absentes restent `Non vérifié` et ne sont pas déduites.
- [ ] Les preuves sont rattachées à une URL, un fichier, un passage ou une empreinte.
- [ ] Les contraintes de licence, d’accès et de réutilisation ont été examinées avant diffusion.
- [ ] La fiche peut être relue et reproduite à partir de la configuration du crawler.
