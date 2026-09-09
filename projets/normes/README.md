# Projet Normes

- **Équipe :** Alain et Mostapha
- **Branche principale :** `feat/GetNormes`
- **Préparation :** `feat/initSearchSystem`
- **Spécification :** [SPEC.md](SPEC.md)
- **Statut :** expérimentation et structuration du corpus en cours

## Actifs actuels

L’implémentation historique se trouve encore dans [`normes-software-embarque-automobile/`](../../normes-software-embarque-automobile/). Elle contient le catalogue, le registre des sources, le script de récupération et le manifeste. Elle sera déplacée ici dans une pull request de migration dédiée, sans changement fonctionnel simultané.

## Commandes actuelles

```bash
python3 normes-software-embarque-automobile/telecharger_sources.py --help
```

L’exécution réseau réelle n’est pas un contrôle pre-commit et peut produire des échecs d’accès attendus.

## Feature : Récupération et mise en forme des exigences issues des normes

Normes concernées (extraction depuis les sources officielles) :

- **Automotive SPICE PAM v4.0** — Automotive SPICE Process Assessment / Reference Model — source officielle : https://automotivespice.com/ (PDF VDA QMC : https://vda-qmc.de/wp-content/uploads/2023/12/Automotive-SPICE-PAM-v40.pdf)
- **IEC 61508** — Functional safety of E/E/PE systems — source officielle : https://www.iec.ch/functionalsafety
- **ISO 15765** — Diagnostic communication over CAN (DoCAN) — source officielle : https://www.iso.org/standard/71611.html (à confirmer)
- **ISO/PAS 5112:2022** — Guidelines for auditing cybersecurity engineering — source officielle : https://www.iso.org/standard/80840.html
- **ISO/SAE 21434:2021** — Cybersecurity engineering — source officielle : https://www.iso.org/standard/70918.html

> Conformément à `US-NORM-INIT-001` / `RM-NORM-INIT-001`, une version absente de la source officielle est conservée comme inconnue jusqu’à vérification directe.

### Objectifs
1. **Extraire les exigences depuis les sources officielles** — pour chaque norme listée ci-dessus, consulter la source officielle (page éditeur, portail normatif, PDF téléchargeable légalement) et identifier les exigences normatives réellement présentes dans le document officiel.
2. **Garantir la conformité aux sources** — chaque exigence extraite doit être rattachée à une clause, sous-clause ou section identifiable du PDF source ; aucune exigence inventée ou non retrouvable ne peut recevoir le statut `Vérifié`.
3. **Utiliser les identifiants officiels** — chaque exigence porte l’identifiant officiel de la norme (numéro de clause, ID de requis `RQ-XX-XX`, ID de work product `WP-XX-XX`, identifiant de processus `SYS.x` / `SWE.x`, etc.) tel qu’il figure dans le document source.
4. **Être exhaustif** — maximiser le nombre d'exigences extraites par norme (le maximum retrouvable dans le source) sans doublon ni omission volontaire de clauses couvertes.
5. **Structurer chaque exigence** — chaque exigence dispose au minimum de : un identifiant officiel unique, une catégorie, une description, les informations contextuelles pertinentes, la version de la norme relative à l'exigence (par ex. ISO/SAE 21434:2021, IEC 61508 éd. 2.0, Automotive SPICE PAM v4.0) et une référence source précise (clause, page ou section).
6. **Automatiser la vérification** — un script de contrôle valide pour chaque norme : identifiants uniques sans doublon, présence d’une catégorie, présence d’une référence source et description présente.
7. **Comparer les extractions aux sources** — avant publication, repasser les tests et comparer chaque exigence extraite au PDF source pour détecter et corriger tout écart (mismatch de clause, contenu absent, référence incorrecte).
8. **Documenter les limites et questions ouvertes** — toute norme dont le PDF disponible est un aperçu, une édition partielle ou une version non officielle est signalée explicitement, et les exigences non vérifiables restent au statut `Candidat` ou `Non vérifié`.
9. **Générer les livrables en anglais** — le document généré pour chaque norme est rédigé en anglais, conformément à la langue des sources officielles.

## Livrables d'extraction

Les fichiers d'exigences sont générés dans le dossier [`exigences/`](exigences/).

| Norme | Version | Livrable | Exigences | Statut |
|---|---|---|---|---|
| Automotive SPICE PAM | v4.0 | [`automotive-spice-exigences.md`](exigences/automotive-spice-exigences.md) | 211 | Vérifié |
| IEC 61508 | éd. 2.0 | [`iec-61508-exigences.md`](exigences/iec-61508-exigences.md) | 17 | Partiel (preview) |
| ISO 15765 | 2011/2021/2024 | [`iso-15765-exigences.md`](exigences/iso-15765-exigences.md) | 51 | Partiel (preview) |
| ISO/PAS 5112 | 2022 | [`iso-pas-5112-exigences.md`](exigences/iso-pas-5112-exigences.md) | 34 | Partiel (preview) |
| ISO/SAE 21434 | 2021 | [`iso-sae-21434-exigences.md`](exigences/iso-sae-21434-exigences.md) | 29 | Partiel (preview) |

Pour vérifier un livrable :

```powershell
powershell -ExecutionPolicy Bypass -File exigences/verify-exigences.ps1 -MdPath exigences/<norme-id>-exigences.md
```
