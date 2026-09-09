# SPEC — Contrôles qualité statiques et dynamiques

## 1. Informations générales

- **Identifiant :** `PROJ-QUAL-001`
- **Branche :** `feat_Cppcheck`
- **Équipe :** Qualité du code
- **Responsables :** Eric, Céline et Damien
- **Mission source :** « Recherche de contrôles qualité statiques et dynamiques » dans `travail.md`
- **Statut initial :** À prototyper

## 2. Objectif

Identifier, comparer puis prototyper un ensemble minimal de contrôles reproductibles permettant de détecter des défauts avant intégration d’un changement.

## 3. Besoin utilisateur

> En tant que développeur ou relecteur, je veux lancer les mêmes contrôles localement et en intégration afin de détecter les défauts reproductibles et de disposer d’un rapport exploitable.

## 4. Questions à résoudre avant l’implémentation

- Quel code ou projet cible doit être contrôlé ?
- Quels langages, compilateurs et systèmes de build sont utilisés ?
- Quels tests dynamiques existent déjà ?
- Quels outils sont compatibles avec les licences et l’environnement disponibles ?
- Quel temps maximal est acceptable localement et en CI ?
- Quelles catégories d’anomalies doivent bloquer l’intégration ?

## 5. Périmètre

### Inclus

- Inventaire comparatif des outils statiques et dynamiques candidats.
- Versions, licences, langages, commandes, formats de rapport et limites.
- Choix justifié d’un contrôle statique et d’un contrôle dynamique minimaux.
- Prototype exécutable localement sur une cible explicitement définie.
- Cas de succès, d’échec et d’outil indisponible.
- Proposition d’intégration dans un hook partagé ou une CI.

### Exclus

- Déclaration d’absence totale de défauts.
- Certification automatique de conformité à une norme.
- Correction silencieuse du code analysé.
- Activation d’un blocage sur tout le dépôt avant validation du prototype.

## 6. Livrables attendus

- Une matrice de comparaison des outils.
- Une décision de choix avec alternatives et limites.
- Des fichiers de configuration versionnés.
- Une commande unique documentée pour le profil rapide.
- Une commande documentée pour le profil complet.
- Un exemple de rapport de succès et un exemple d’échec contrôlé.
- Une procédure de reproduction par un autre membre de l’équipe.

## 7. Règles

- Un contrôle non exécuté ne peut pas être déclaré réussi.
- Les versions des outils et commandes doivent être enregistrées.
- Le prototype doit retourner un code non nul pour un défaut bloquant connu.
- Les faux positifs et exclusions sont documentés et revus humainement.
- Aucun secret, cache personnel ou rapport volumineux n’est commité.
- Le hook local ne constitue pas à lui seul une garantie, car il peut être absent ou contourné.

## 8. Critères d’acceptation

- [ ] `CA-QUAL-01` : la cible, le langage et la commande de build sont définis.
- [ ] `CA-QUAL-02` : au moins deux outils statiques et deux approches dynamiques sont comparés.
- [ ] `CA-QUAL-03` : le choix des outils et versions est justifié.
- [ ] `CA-QUAL-04` : le profil rapide est exécutable avec une commande documentée.
- [ ] `CA-QUAL-05` : un défaut contrôlé produit un code non nul et un diagnostic lisible.
- [ ] `CA-QUAL-06` : l’absence d’un outil produit un échec ou un état inconclusif visible.
- [ ] `CA-QUAL-07` : une autre personne peut reproduire le contrôle.
- [ ] `CA-QUAL-08` : les limites et éléments non testés sont listés.

## 9. Scénarios de vérification

```gherkin
Fonctionnalité: Exécuter les contrôles qualité

  Scénario: Profil rapide réussi
    Étant donné une cible compilable et les outils requis installés
    Quand le profil rapide est lancé
    Alors les contrôles configurés sont exécutés
    Et le résultat indique les commandes, versions et statuts

  Scénario: Défaut bloquant connu
    Étant donné un exemple de démonstration contenant un défaut attendu
    Quand le profil rapide est lancé
    Alors la commande retourne un code non nul
    Et le rapport localise la cause

  Scénario: Outil absent
    Étant donné qu’un outil requis n’est pas disponible
    Quand le contrôle est lancé
    Alors aucun succès global n’est annoncé
    Et l’installation manquante est indiquée
```

## 10. Définition de terminé

La recherche est terminée lorsqu’elle aboutit à un choix justifié et à un prototype reproductible. Une matrice d’outils sans exécution réelle ne suffit pas à satisfaire la spécification.
