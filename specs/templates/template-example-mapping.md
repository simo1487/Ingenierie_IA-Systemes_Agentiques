# Modèle d'Atelier Example Mapping & Table de Décision

Ce document sert de support pour formaliser les règles métier, exemples concrets et tables de décision d’une User Story avant tout codage ou génération de scénarios Gherkin.

---

## 1. Métadonnées de l'atelier

- **Feature / Exigence associée :** `[ID-EXIGENCE]` (ex: `ZEP-SRS-5-2`, `FEAT-QUAL-001`)
- **Titre :** [Titre de la règle métier explorée]
- **Participants :** [Noms des membres du binôme / trinôme]
- **Date :** `AAAA-MM-JJ`
- **Statut de l'analyse :** `Candidat` / `Vérifié`

---

## 2. Carte d'Example Mapping

### Règle métier (Règle principale)
> **Règle :** [Énoncer la règle de manière concise, sans ambiguïté.]

### Exemples concrets (Cas nominaux)
1. **Exemple 1 (Cas standard) :**
   - *Contexte initial :* [État du système]
   - *Action déclenchée :* [Événement ou appel d'API]
   - *Résultat attendu :* [Valeur retournée et état final]
2. **Exemple 2 (Alternative valide) :**
   - *Contexte initial :* [État du système]
   - *Action déclenchée :* [Événement]
   - *Résultat attendu :* [Résultat observable]

### Contre-exemples et cas limites (Frontières et erreurs)
1. **Contre-exemple 1 (Dépassement de borne / Frontière) :**
   - *Contexte initial :* [Valeur limite]
   - *Action déclenchée :* [Action franchissant la limite]
   - *Résultat attendu :* [Code d'erreur précis, blocage ou préservation de l'état]
2. **Contre-exemple 2 (Ressource indisponible / Timeout / Concurrence) :**
   - *Contexte initial :* [Ressource verrouillée ou contexte ISR]
   - *Action déclenchée :* [Tentative d'accès]
   - *Résultat attendu :* [Retour immédiat, code `-EBUSY` ou `-EAGAIN`]

### Questions ouvertes et inconnues (À ne pas inventer !)
- [ ] **Q1 :** [Point imprécis dans la spécification d'origine]
- [ ] **Q2 :** [Comportement indéfini dans la baseline étudiée]

---

## 3. Table de Décision

Lorsque le comportement dépend de plusieurs conditions combinées, utiliser cette table :

| Cas # | Condition 1 | Condition 2 | Condition 3 | Action attendue | Résultat attendu | Statut du cas |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 1 | [Valeur] | [Valeur] | [Valeur] | [Action] | [Résultat observable] | Nominal |
| 2 | [Valeur limite] | [Valeur] | [Valeur] | [Action] | [Résultat frontière] | Frontière |
| 3 | [Valeur invalide] | [Valeur] | [Valeur] | [Refus] | [Erreur documentée] | Erreur |

---

## 4. Dérivation en Scénarios Gherkin candidats

Traduire les lignes de la table de décision en scénarios Gherkin dans la feature spec associée (`FEAT-*`).
S'assurer que chaque scénario :
1. Possède un **oracle indépendant** (défini avant d'avoir vu le code).
2. Ne constitue pas un test tautologique.
3. Est falsifiable par un test de mutation conceptuelle.
