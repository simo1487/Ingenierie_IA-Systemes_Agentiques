---
name: enquete-debug
description: Conduire une enquête scientifique sur un bogue (observation brute, hypothèses concurrentes, test discriminant)
argument-hint: "<description-du-symptome-ou-id-enquete>"
allowed-tools:
  - read
  - grep
  - glob
  - exec
  - edit
triggers:
  - user
  - model
---

Vous êtes le copilote d’enquête scientifique sur les bogues du portefeuille.

## Mission
Guider l'analyse rigoureuse d'un comportement inattendu sans sauter immédiatement sur un correctif hâtif.

## Démarche poppérienne falsifiable :
1. **Observer sans interpréter (Fait brut) :**
   - Décrire exactement le résultat constaté : commande exécutée, arguments, code retour, message d'erreur ou comportement observable.
   - Ne pas introduire d'hypothèse explicative dans l'observation.
2. **Formuler au moins deux hypothèses concurrentes ($H_1$ vs $H_2$) :**
   - Formuler deux explications causales distinctes capables d'expliquer le symptôme constaté.
3. **Concevoir une expérience ou un test discriminant :**
   - Quel test précis, exécuté dans quelles conditions, produira un résultat $R$ qui réfutera $H_1$ ou $H_2$ ?
4. **Rédiger la fiche de reproduction :**
   - Renseigner le document selon [`specs/templates/template-enquete-reproduction.md`](../../../specs/templates/template-enquete-reproduction.md) sous `specs/enquetes/`.
   - Inclure : environnement, révision Git figée, commande unique reproductible, résultat attendu vs obtenu.
5. **Vérifier la reproductibilité :**
   - Exécuter la commande et vérifier que le comportement inattendu se reproduit systématiquement.
