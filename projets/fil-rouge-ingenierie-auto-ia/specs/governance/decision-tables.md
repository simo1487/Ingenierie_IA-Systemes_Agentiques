# Référence — Tables de décision candidates

**Nature :** Proposition. **Statut :** Candidate / Candidat. Ces tables explicitent les règles du backlog avant implémentation. `—` signifie indifférent : les lignes partitionnent toutes les combinaisons. Elles ne décrivent pas une protection déjà présente dans le MVP.

## Prévalidation — RM-FIL-101

Les quatre conditions sont : structure du manifeste valide, corpus non vide, révisions présentes, approbation applicable à cette version. Les valeurs absentes ne satisfont pas une condition. L’autorisation ci-dessous ne vaut pas décision finale de Gate.

| Structure valide | Corpus non vide | Révisions présentes | Approbation applicable | Étapes dépendantes |
|---|---|---|---|---|
| Non | — | — | — | Interdites avant retrieval/fournisseur |
| Oui | Non | — | — | Interdites avant retrieval/fournisseur |
| Oui | Oui | Non | — | Interdites avant retrieval/fournisseur |
| Oui | Oui | Oui | Non | Interdites avant retrieval/fournisseur |
| Oui | Oui | Oui | Oui | Autorisées pour cette version |

## Mémoire — RM-FIL-203

L’expiration compare l’horloge contrôlée à `expires_at`. L’égalité est expirée. Des métadonnées incomplètes ne permettent pas de conclure que l’entrée est utilisable.

| Métadonnées complètes | Portée autorisée | Instant strictement avant expiration | Injection dans le contexte |
|---|---|---|---|
| Non | — | — | Refusée |
| Oui | Non | — | Refusée |
| Oui | Oui | Non | Refusée |
| Oui | Oui | Oui | Permise avec source et révision |

## Lecture d’outil — RM-FIL-301

L’identité est issue d’un contexte de confiance, jamais des champs proposés par le modèle. La politique doit accorder explicitement l’outil ET la ressource demandée ; un droit inconnu vaut absence d’autorisation.

| Arguments valides | Identité connue | Outil et ressource explicitement autorisés | Décision | Appel au lecteur |
|---|---|---|---|---|
| Non | — | — | Refus de validation | Aucun |
| Oui | Non | — | Refus de politique | Aucun |
| Oui | Oui | Non | Refus de politique | Aucun |
| Oui | Oui | Oui | Autorisation tracée avant accès | Permis après décision |

Les messages et codes d’erreur exacts restent à définir dans les contrats d’implémentation. L’oracle de refus doit observer le lecteur, pas seulement une phrase produite par le modèle.
