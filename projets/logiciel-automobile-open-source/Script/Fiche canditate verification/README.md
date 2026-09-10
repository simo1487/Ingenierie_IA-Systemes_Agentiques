# Scripts de Vérification des Fiches Candidat

Ce répertoire contient des scripts pour automatiser la vérification des fiches candidat JSON.

## verify_fiches_cand.py

Script de vérification des fiches candidat JSON qui :
- Trouve tous les fichiers `fiche_cand_*.json` dans le projet
- Vérifie l'existence et l'accessibilité des URLs canoniques des dépôts
- Vérifie l'activité des projets selon les critères définis (< 30 jours)
- Génère un rapport détaillé des résultats

### Installation des dépendances

```bash
pip install -r requirements.txt
```

### Utilisation

```bash
python verify_fiches_cand.py
```

### Critères de vérification

**Accessibilité URL :**
- Vérifie que l'URL canonique du dépôt répond avec un code HTTP 2xx ou 3xx
- Timeout de 10 secondes
- Suit les redirections automatiquement

**Activité projet :**
- Considère le projet comme actif si le statut est déclaré "Actif" dans la fiche
- Sinon, vérifie que le dernier commit est daté de moins de 30 jours
- Seuil d'inactivité : 30 jours

### Sortie

Le script génère :
- Un rapport affiché dans la console
- Un fichier `rapport_verification_fiches.txt` dans le répertoire racine du projet

### Format du rapport

```
================================================================================
RAPPORT DE VÉRIFICATION DES FICHES CANDIDAT
================================================================================
Date: 2026-09-09 HH:MM:SS
Total fiches vérifiées: X

STATISTIQUES:
  ✓ OK: X
  ⚠ ATTENTION: X
  ✗ ERREUR: X

DÉTAILS PAR FICHE:
--------------------------------------------------------------------------------
✓ projets/logiciel-automobile-open-source/fiche_cand_001_vesc.json
  URL canonique: https://github.com/vedderb/bldc
  Accessibilité: OUI (HTTP 200)
  Activité: ACTIF (Statut déclaré: Actif)
  Statut global: OK
...
```

### Codes de retour

- `0` : Aucune erreur critique
- `1` : Au moins une erreur critique détectée

### Structure des fichiers JSON attendus

Les fichiers `fiche_cand_*.json` doivent contenir au minimum :

```json
{
  "informations_identification": {
    "url_canonique_depot": "https://github.com/user/repo"
  },
  "activite_projet": {
    "statut": "Actif",
    "dernier_commit": "2026-09-04 (pushed_at)"
  }
}
```

## Développement

Pour ajouter de nouveaux scripts de vérification :
1. Créer un nouveau fichier Python dans ce répertoire
2. Suivre les conventions de nommage et de documentation
3. Ajouter les dépendances nécessaires dans `requirements.txt`
4. Documenter l'utilisation dans ce README