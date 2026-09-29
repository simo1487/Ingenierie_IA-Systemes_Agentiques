# Projet Cybersecurity

- **Équipe :** À définir
- **Branche principale :** `feat_getReq`
- **Spécification :** [SPEC.md](SPEC.md)
- **Statut :** Recherche et collecte de normes en cours

## Actifs actuels

Extraction des exigences des normes de cybersécurité selon la méthodologie du projet `normes` :
- **ISO/IEC 27001:2022** - Information security management systems
- **ISO/SAE 21434:2021** - Road vehicles Cybersecurity engineering

## Commandes actuelles

Les fichiers d'exigences sont générés dans le dossier [`exigences/`](exigences/).

## Normes concernées

| Norme | Version | Livrable | Exigences | Statut |
|---|---|---|---|---|
| ISO/IEC 27001 | 2022 | [`iso-27001-exigences.md`](exigences/iso-27001-exigences.md) | 15 | Partiel |
| ISO/SAE 21434 | 2021 | [`iso-sae-21434-exigences.md`](exigences/iso-sae-21434-exigences.md) | 25 | Partiel |

## Objectifs

1. **Extraire les exigences depuis les sources officielles** — pour chaque norme listée ci-dessus, consulter la source officielle et identifier les exigences normatives réellement présentes.
2. **Garantir la conformité aux sources** — chaque exigence extraite doit être rattachée à une clause ou section identifiable du document source.
3. **Utiliser les identifiants officiels** — chaque exigence porte l'identifiant officiel de la norme tel qu'il figure dans le document source.
4. **Être exhaustif** — maximiser le nombre d'exigences extraites par norme sans doublon ni omission.
5. **Structurer chaque exigence** — chaque exigence dispose au minimum de : un identifiant officiel unique, une catégorie, une description, la version de la norme et une référence source précise.
6. **Adapter au contexte automobile** — ajouter des exigences spécifiques au contexte automobile (marquées comme Candidate).

## Livrables d'extraction

Les fichiers d'exigences sont générés dans le dossier [`exigences/`](exigences/).

## Arborescence réelle

```text
projets/cybersecurity/
├── README.md
├── SPEC.md
├── exigences/
│   ├── iso-27001-exigences.md
│   └── iso-sae-21434-exigences.md
├── experiments/
├── src/
├── tests/
├── docs/
├── data/
└── evidence/
```

## Installation

À définir

## Entrées et baselines

- **Sources officielles ISO** : Site web et documentation officielle
- **Méthodologie** : Basée sur le projet `normes` (branche `feat/GetNormes`)

## Sorties et preuves

- Fichiers d'exigences structurés en Markdown
- Traçabilité vers les clauses source
- Identification du statut de vérification

## Limites et questions ouvertes

- Les extractions sont partielles et nécessitent validation contre les documents complets
- Les exigences spécifiques au contexte automobile (AUTO series) sont candidates et nécessitent validation
- L'accès aux documents complets des normes peut nécessiter des licences appropriées
