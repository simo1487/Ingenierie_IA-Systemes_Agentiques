# Exigences extraites des normes

Ce dossier contient les livrables d'extraction des exigences normatives, un fichier Markdown par norme, conformément aux 10 objectifs définis dans le [README du projet normes](../README.md).

## Convention de nommage

- `<norme-id>-exigences.md` — livrable principal d'extraction pour une norme
  - Exemple : `automotive-spice-exigences.md`, `iso-sae-21434-exigences.md`
- `verify-exigences.ps1` — script de vérification générique, paramétrable par norme
- `_source_<norme-id>.txt` — contenu source extrait pour audit (fichier de travail)

## Structure de chaque exigence

Chaque exigence du livrable respecte la structure suivante (point 5 du README) :

- **ID officiel** : identifiant tel qu'il figure dans la source officielle
- **Norme / Version** : nom et version de la norme
- **Catégorie** : famille ou thème normatif
- **Référence source** : clause, section, page ou URL selon le format de la source
- **Statut** : `Vérifié` | `Candidat` | `Non vérifié`
- **Description** : >= 1000 caractères (contexte + exigence + critères)

## Statuts et traçabilité

Conformément à `US-NORM-003` / `RM-NORM-003` :

- **Vérifié** : le passage source a été retrouvé dans la source officielle extraite
- **Candidat** : exigence identifiée mais passage source non vérifié directement
- **Non vérifié** : source inaccessible ou contenu non extractible

## Normes traitées

| Norme | Version | Livrable | Exigences | Statut |
|---|---|---|---|---|
| Automotive SPICE PAM | v4.0 | [`automotive-spice-exigences.md`](automotive-spice-exigences.md) | 211 | Vérifié |
| IEC 61508 | éd. 2.0 | [`iec-61508-exigences.md`](iec-61508-exigences.md) | 17 | Partiel (preview) |
| ISO 15765 | 2011/2021/2024 | [`iso-15765-exigences.md`](iso-15765-exigences.md) | 51 | Partiel (preview) |
| ISO/PAS 5112 | 2022 | [`iso-pas-5112-exigences.md`](iso-pas-5112-exigences.md) | 34 | Partiel (preview) |
| ISO/SAE 21434 | 2021 | [`iso-sae-21434-exigences.md`](iso-sae-21434-exigences.md) | 29 | Partiel (preview) |
