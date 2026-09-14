# Référence — Contrats de mesure et d'évaluation candidats

**Nature :** Proposition. **Statut documentaire :** Candidate. **Statut de preuve :** Candidat. **Exécution :** aucune nouvelle mesure produite par ce document.

Ces contrats complètent les US du [backlog canonique](../backlog.json) et les [sources de formation](../formation-alignment.json). Les attendus, annotations, paramètres et hypothèses réels doivent être approuvés avant essai. Aucune valeur citée en séance n'est un seuil universel. Les liens de formation décrivent un alignement pédagogique candidat, pas une preuve d'implémentation.

## MES-01 — Comparaison d'organisations (US-FIL-103)

- Unité : un même cas identifié, avec entrée figée, révision du corpus, attendu indépendant et mode d'exécution déclaré.
- A : séquence baseline. B : producteur puis vérificateur recevant les sources de référence et un critère distinct ; le vérificateur ne signe pas la décision finale. Le choix initial règle/recherche/workflow/agent relève de US-FIL-1, avant cette comparaison.
- Capturer pour chaque couple cas/organisation : références d'entrée et d'oracle, versions du code/configuration, mode, début/fin, résultat observé, écarts à l'attendu, revue et erreurs de mesure.
- Une erreur est un écart à un attendu préalablement approuvé, pas un désaccord arbitraire entre modèles.
- Présenter les observations par cas d'abord. Cas manquant, autre oracle, autre entrée ou mélange réel/replay : comparaison concernée non comparable ; ne pas l'exclure silencieusement.
- Erreurs identiques : « écart nul sur les cas observés ». Aucun gain de fiabilité générale ni besoin de multi-agent n'en découle.
- Durée réelle : différence début/fin selon une même horloge monotone. Une durée rejouée est une donnée fournie, pas une nouvelle mesure. Le temps humain est relevé séparément.
- L'IA peut proposer une lecture des écarts ; le choix A/B et les limites de conclusion sont humains.

## MES-02 — Cas, protection et non-régression (US-FIL-401/402)

Chaque cas contient : `case_id`, `dataset_version`, `class`, `input_ref`, `identity_ref`, `scope_ref`, `expected_decision`, `expected_access`, `expected_trace_order`, `oracle_ref`, `owner`, `critical`. Contrat documentaire candidat, pas une API implémentée.

- Classes : nominal, argument invalide, hors périmètre, identité inconnue, instruction dans demande et dans donnée. Les cas de concurrence, timeout et interruption sont ajoutés lorsqu'ils s'appliquent ; aucun quota de trois cas.
- L'attendu vient d'une politique revue indépendamment. Un refus vérifie zéro appel au lecteur hors portée, raison et ordre des événements. Une phrase « refusé » n'est pas un contrôle.
- Résultats séparés : `pass`, `fail`, `not_run`, `undecidable`. Sans attendu indépendant, le cas est `undecidable`, jamais `pass`.
- Rapporter chaque catégorie et les cas associés. Un taux descriptif éventuel vaut `pass / (pass + fail)` uniquement avec dénominateur non nul ; afficher aussi le total prévu et les cas non exécutés/non décidables. Un jeu partiel n'est pas entièrement validé.
- Violation critique : bloquante indépendamment d'un score agrégé. Cas critique non exécuté/non décidable : protection non démontrée.
- Mutation défensive sur copie isolée : retirer uniquement le garde ciblé ; le même cas échoue sur l'accès réellement observé, puis repasse avec le garde restauré. Ne jamais altérer les politiques du dépôt ou un service partagé.
- Un mutant survivant demande d'examiner le chemin exécuté, le test et la pertinence du mutant ; il ne prouve pas automatiquement un défaut produit. Conserver cette observation négative.
- Cas et caractère critique sont revus humainement avant de figer le jeu ; aucun juge LLM seul ne clôt la Gate.

## MES-03 — Retrieval et abstention (US-FIL-4/404)

Sources : cours J04 `#comprendre`, notamment lignes 98–109. Préparer d'abord questions et passages attendus, puis tester une requête directe. Le lexical constitue une baseline possible sans modèle. L'alternative sémantique demeure une extension, non un prérequis à cette préparation.

Avant comparaison, faire approuver : corpus autorisé et empreinte, révisions, questions, annotations indépendantes, catégories répondable/sans réponse, données de réglage distinctes des données de vérification, découpage, k et règles d'abstention. Pour un adaptateur vectoriel, ajouter modèle d'embedding et version d'index. Aucun k ni seuil réel n'est imposé ici.

Pour une question répondable q, R(q) est l'ensemble non vide de passages pertinents annotés. T(q) est la liste ordonnée des k premiers identifiants uniques retournés. Les doublons sont éliminés pour le calcul en conservant le premier rang ; les résultats bruts restent disponibles.

- `Hit@k(q) = 1` si au moins un élément de R(q) apparaît dans T(q), sinon 0.
- `RR@k(q) = 1/r` où r est le rang du premier passage pertinent dans T(q), sinon 0. `MRR@k` est la moyenne de ces rangs réciproques sur les questions répondables effectivement exécutées sous le même protocole.
- `recall@k(q) = |R(q) ∩ set(T(q))| / |R(q)|` complète ces mesures lorsqu'une réponse exige plusieurs passages ; Hit@k seul peut masquer une preuve incomplète.
- Conserver effectif prévu, effectif exécuté et cas manquants. Aucun résultat si le dénominateur est nul ; un échec d'exécution n'est pas arbitrairement transformé en question non pertinente ou exclu sans mention.
- Les questions sans réponse sont évaluées séparément par abstention correcte ou citation indue. Ne pas diviser par un ensemble pertinent vide ni les fusionner dans le MRR/recall répondable.
- Les mêmes identifiants et la même granularité d'annotation sont nécessaires aux deux moteurs. Changer le découpage exige une correspondance revue, pas un rapprochement lexical automatique.
- Un score de similarité n'est ni une probabilité de vérité ni une autorisation. Ne pas additionner directement les scores hétérogènes de moteurs différents.
- Provenance introuvable : erreur, pas passage pertinent. Les seuils d'adoption doivent être décidés avant essai ; sinon publier uniquement les observations. Le résultat négatif historique de Zephyr reste une preuve fournie, pas une nouvelle exécution.

## MES-04 — Classement OSS (US-FIL-405)

Le score fictif 0–10 du MVP ne constitue pas une grille produit approuvée. Avant classement réel, décider critères, sources, normalisation/pondérations éventuelles, politique des inconnues, égalités et critères éliminatoires.

- Capturer chaque observation par candidat/révision/critère ; une affirmation de fiche n'est pas une preuve indépendante.
- Chaque note doit être reconstruisible depuis cette capture et la version de grille. Aucun total si l'agrégation n'est pas approuvée ; aucune pondération implicite.
- Valeur manquante : inconnue jusqu'à application de la politique décidée, pas zéro arbitraire ni valeur favorable.
- Contre-calcul indépendant depuis la capture figée, sans nouvelle recherche. Conserver les égalités.
- Choix du dépôt, révision et acceptabilité de licence : décisions humaines. Le score ne télécharge ni n'exécute un dépôt.

## MES-05 — Coût complet et ROI incrémental (US-FIL-602)

Source : cours J05 `#roi`, lignes 208–229 ; prolongement par J08 `#comprendre`, lignes 90–95. La convention retenue est le ROI incrémental enseigné en J05. Elle remplace l'ancienne convention de coût brut du backlog ; ne pas mélanger leurs dénominateurs.

Définir période, périmètre, unité d'œuvre et qualité attendue comparables. Capturer par donnée : valeur, unité, période, source, nature `observé` ou `hypothèse`, responsable de validation. Les volumes et tarifs du cours sont fictifs et ne sont jamais des mesures de ce projet.

- N = demandes effectivement traitées avec la solution sur le périmètre observé, pas appels IA ni utilisateurs inscrits.
- t0/t1 = temps humains moyens, en minutes par demande, avant/avec la solution. Inclure recherche, préparation, revue, corrections, essais infructueux et retour au traitement manuel. Préserver les cas lents/échoués dans le périmètre, sans sélection des seuls succès.
- h = coût horaire chargé, sourcé ou explicitement hypothétique.
- `B = N × (t0 − t1) / 60 × h` : valeur de capacité dégagée, pas économie budgétaire garantie.
- `C = I + R` : investissement initial et coûts récurrents supplémentaires sur la même période. Inclure intégration/formation initiale dans I ; inférence, hébergement, maintenance, support et surveillance non déjà inclus dans t1 dans R.
- `Valeur_nette = B − C` ; `ROI_incremental = (B − C) / C` uniquement si C > 0 et les données sont complètes et comparables. Multiplier par 100 pour un affichage en pourcentage.
- La revue/correction déjà intégrée dans t1 n'est pas soustraite une seconde fois dans R. Chaque poste de travail humain ou de dépense doit apparaître une seule fois dans la convention choisie ; afficher où il est compté.
- Coût complet visible ne signifie pas tout placer dans C : montrer ensemble le temps humain t1 et les coûts supplémentaires I/R. Un t1 supérieur à t0 conserve son bénéfice négatif ; ne pas le ramener à zéro.
- Donnée absente : `non mesuré` ou hypothèse nommée, pas zéro. C nul, valeur requise absente, N sans observation comparable ou périmètres incompatibles : résultat `non calculable` avec raison. Une projection ne devient pas une mesure.
- Favorable/pessimiste : hypothèses approuvées et séparées des observations, même convention comptable, hypothèse fragile explicitée. Aucun gain ni seuil de ROI imposé.
- Contre-calcul indépendant depuis une capture figée : unités, période, cas exclus, coûts humains et doubles comptes contrôlés. Un ROI favorable ne compense pas un blocage de sécurité ou l'absence de réversibilité.

## MES-06 — Support des affirmations (US-FIL-5)

Source : cours J04 `#comprendre`, lignes 105–115. Définir les affirmations et passages attendus avant de générer la réponse d'essai.

- Contrôle mécanique distinct : source existe, version correcte, locator résolvable, droits applicables. Ce contrôle ne décide pas du sens.
- Revue sémantique indépendante par affirmation : `support complet` (toute l'affirmation, conditions comprises), `support partiel` (partie étayée explicitement désignée), `contradiction`, `absence de support`.
- Une citation valide qui ne soutient qu'une partie ne devient pas support complet. L'affirmation est à restreindre ou à compléter, sans inventer le manque.
- Deux sources contradictoires : exposer le conflit et demander une décision ; ne pas choisir silencieusement celle qui favorise la réponse.
- Sans support : signaler le manque ou s'abstenir. Une liste vide n'autorise pas une exigence nouvelle.
- Conserver référence d'affirmation, référence de citation, classe de support, justification du relecteur, version et mode. Un juge LLM peut proposer une classe mais ne l'accepte pas seul.
- Pas de score global de qualité inventé ni de seuil qui compenserait une contradiction ou un défaut de provenance.

## Arbitrages requis

Le registre de gouvernance conserve les choix ouverts. Un document peut être rédigé avant leur résolution ; une réalisation ou acceptation dépendante ne peut pas supposer leur valeur. Ces contrats n'autorisent aucun changement de configuration de production, ni aucune affirmation de résultat non observé.
