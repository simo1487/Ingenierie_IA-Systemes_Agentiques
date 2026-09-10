# Corpus Qualité — Diagnostics Cppcheck, MISRA C:2012 et Revue Humaine

**Origine :** `projets/qualite-code/evidence/`
**Baseline :** `Cppcheck-2.21.0-C11`
**Statut :** `Vérifié`

## QUAL-DIAG-01 — Débordement de tampon détecté (Buffer Overflow)
Lors de l'analyse statique de la fixture `defect.c`, Cppcheck a détecté une écriture hors limites causée par l'usage non sécurisé de `strcpy`.
- **Identifiant :** `QUAL-DIAG-01`
- **Fichier :** `tests/fixtures/defect.c:25:12`
- **Règle :** `bufferAccessOutOfBounds`
- **Sévérité :** Erreur bloquante
- **Statut :** `Anomalie confirmée`
- **Diagnostic exact :** `error: Buffer is accessed out of bounds: buffer [bufferAccessOutOfBounds]`
- **Décision humaine :** Bloquant pour l'intégration, nécessite un remplacement par `strncpy` ou contrôle de taille préalable.

## QUAL-MISRA-Dir4.6 — Utilisation obligatoire de types de base à taille fixée
La directive MISRA C:2012 Dir 4.6 exige que les types numériques de base (`int`, `short`, `long`) soient remplacés par des types explicites (`int32_t`, `uint16_t`, etc.) définis dans `<stdint.h>`.
- **Identifiant :** `MISRA-C-2012-Dir-4.6`
- **Catégorie :** Portabilité et robustesse
- **Sévérité :** Recommandation
- **Statut :** `Déviation documentée` pour les fonctions d'interface C standard.

## QUAL-CLANG-01 — Nombre magique dans l'initialisation (Faux positif)
Clang-tidy signale un avertissement de lisibilité sur des constantes 5 et 10 utilisées comme paramètres de temporisation.
- **Identifiant :** `QUAL-CLANG-01`
- **Fichier :** `tests/fixtures/success.c:12`
- **Règle :** `cppcoreguidelines-avoid-magic-numbers`
- **Statut :** `Faux positif classé`
- **Décision humaine :** Avertissement non bloquant pour le prototype, documentation de la constante suffisante.
