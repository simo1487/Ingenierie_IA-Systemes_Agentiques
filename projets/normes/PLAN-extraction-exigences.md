# Plan : Extraction exhaustive des exigences d'une norme vers Markdown (plan générique)

Extraire le maximum d'exigences d'une norme depuis sa source officielle (quel qu'en soit le format — PDF, HTML, portail web, etc.), les structurer conformément aux 9 objectifs du README du projet normes et produire un fichier Markdown en anglais dans le dossier `projets/normes/exigences/`. Ce plan est générique et s'applique à toute norme listée dans le README.

## Objectifs de référence (README `projets/normes/README.md`)

1. **Extraire les exigences depuis les sources officielles** — consulter la source officielle (page éditeur, portail normatif, PDF téléchargeable légalement) et identifier les exigences normatives réellement présentes dans le document officiel.
2. **Garantir la conformité aux sources** — chaque exigence extraite doit être rattachée à une clause, sous-clause ou section identifiable du PDF source ; aucune exigence inventée ou non retrouvable ne peut recevoir le statut `Vérifié`.
3. **Utiliser les identifiants officiels** — chaque exigence porte l'identifiant officiel de la norme (numéro de clause, ID de requis `RQ-XX-XX`, ID de work product `WP-XX-XX`, identifiant de processus `SYS.x` / `SWE.x`, etc.) tel qu'il figure dans le document source.
4. **Être exhaustif** — maximiser le nombre d'exigences extraites par norme (maximum retrouvable dans le source) sans doublon ni omission volontaire de clauses couvertes.
5. **Structurer chaque exigence** — chaque exigence dispose au minimum de : un identifiant officiel unique, une catégorie, une description, les informations contextuelles pertinentes, la version de la norme relative à l'exigence et une référence source précise (clause, page ou section).
6. **Automatiser la vérification** — un script de contrôle valide pour chaque norme : identifiants uniques sans doublon, présence d'une catégorie, présence d'une référence source et description présente.
7. **Comparer les extractions aux sources** — avant publication, repasser les tests et comparer chaque exigence extraite au PDF source pour détecter et corriger tout écart (mismatch de clause, contenu absent, référence incorrecte).
8. **Documenter les limites et questions ouvertes** — toute norme dont le PDF disponible est un aperçu, une édition partielle ou une version non officielle est signalée explicitement, et les exigences non vérifiables restent au statut `Candidat` ou `Non vérifié`.
9. **Générer les livrables en anglais** — le document généré pour chaque norme est rédigé en anglais, conformément à la langue des sources officielles.

## Normes concernées

| Norme | Version | Source officielle |
|---|---|---|
| Automotive SPICE PAM | v4.0 | https://automotivespice.com/ (PDF : https://vda-qmc.de/wp-content/uploads/2023/12/Automotive-SPICE-PAM-v40.pdf) |
| IEC 61508 | éd. 2.0 | https://www.iec.ch/functionalsafety |
| ISO 15765 | à confirmer | https://www.iso.org/standard/71611.html |
| ISO/PAS 5112 | 2022 | https://www.iso.org/standard/80840.html |
| ISO/SAE 21434 | 2021 | https://www.iso.org/standard/70918.html |

## Paramètres d'entrée (à définir pour chaque exécution)

Avant de lancer l'extraction pour une norme donnée, définir :

- **`<norme-id>`** : identifiant stable de la norme (ex. `automotive-spice`, `iec-61508`, `iso-sae-21434`).
- **`<norme-nom>`** : nom complet de la norme en anglais (ex. "Automotive SPICE PAM v4.0").
- **`<norme-version>`** : version/édition officielle (ex. "PAM v4.0", "2021 (E)", "Edition 2.0 (2010)").
- **`<source-url>`** : URL de la source officielle (page éditeur, portail, PDF téléchargeable).
- **`<format-source>`** : format attendu de la source (PDF, HTML, portail web, mixte) — à confirmer en consultant l'URL.

## Méthode d'extraction (générique, adaptée au format de la source)

La source officielle peut être un PDF, une page HTML, un portail web ou un autre format. La méthode d'extraction s'adapte :

1. **Identifier le format de la source** en consultant l'URL officielle (Content-Type, extension, contenu).
2. **Plan A — PDF** : si la source est un PDF, extraire le texte via PowerShell/.NET (parser des flux `/Content` FlateDecode) ou Edge Chromium headless (`--print-to-pdf` / `--dump-dom`).
3. **Plan B — HTML / portail web** : si la source est une page HTML ou un portail, récupérer le contenu via `Invoke-WebRequest` PowerShell et parser le HTML (regex ou propriété `.ParsedHtml`).
4. **Plan C — Format non lisible ou accès restreint** : s'appuyer sur la structure publique connue de la norme (sommaire, table des matières, index des clauses/processus publié par l'éditeur ou des sources secondaires fiables) pour identifier la liste exhaustive des clauses/exigences, puis valider chaque entrée contre le contenu extrait. Toute exigence non vérifiable reste au statut `Candidat` conformément à `US-NORM-003` / `RM-NORM-003`.
5. **Plan D — Source inaccessible** : documenter l'échec d'accès, marquer toutes les exigences `Non vérifié` et signaler la limitation dans le livrable.

## Structure de chaque exigence (conforme objectif 5, en anglais)

```markdown
### <NORME-ID>-<CLAUSE-OU-PROCESSUS>-<BP-OU-NUMERO> — <Short title>

- **Official ID:** <ID as it appears in the source>
- **Standard / Version:** <norme-nom> <norme-version>
- **Category:** <family/theme of the standard>
- **Source reference:** <norme-version>, section/clause/page (or URL/section if HTML source)
- **Status:** Verified | Candidate | Unverified
- **Description:** <context + requirement + criteria>
- **Work products / outputs:** <list if applicable>
```

## Périmètre d'extraction (générique)

Pour chaque norme, identifier sa structure normative propre :

- **Normes type ISO/IEC/SAE** : clauses, sous-clauses, exigences `[RQ-...]`, work products `[WP-...]`, annexes normatives.
- **Référentiels type Automotive SPICE** : processus (SYS/SWE/HWE/MLE/VAL/SUP/MAN/ACQ/PIM), base practices (BP1-BPn), work products, niveaux de capacité.
- **Règlements type UNECE** : articles, annexes, exigences de gestion (CSMS/SUMS).
- **Guides type MISRA/SAE J3061** : règles, directives, catégories de recommandation.

L'objectif est de couvrir l'ensemble des clauses/processus/règles identifiés dans la source officielle, sans omission volontaire. Cible indicative : **maximum retrouvable** (variable selon la norme).

## Étapes d'implémentation (génériques, à exécuter par norme)

1. **Créer ou réutiliser `projets/normes/exigences/`** (dossier + README court décrivant le rôle du dossier et la convention de nommage, créé une seule fois pour toutes les normes).
2. **Identifier le format de la source officielle** pour la norme concernée (PDF, HTML, portail web) en consultant `<source-url>`. Choisir la méthode d'extraction la plus pertinente (plan A/B/C/D ci-dessus) et la documenter.
3. **Extraire le contenu de la source** via la méthode choisie (PowerShell/.NET pour PDF, `Invoke-WebRequest` pour HTML, structure publique si source non lisible). Sauvegarder le contenu extrait dans `projets/normes/exigences/_source_<norme-id>.txt` (fichier de travail pour audit).
4. **Parser le contenu extrait** pour identifier la structure normative de la norme (clauses/processus/règles, base practices, work products, annexes).
5. **Construire la liste exhaustive des exigences** (maximum retrouvable) avec ID officiel, catégorie, version `<norme-version>`, référence source (page/section/URL selon le format), description (enrichie à partir du contenu source : contexte, outputs attendus, critères d'évaluation).
6. **Générer `projets/normes/exigences/<norme-id>-exigences.md`** en anglais (en-tête avec titre/version/statistiques, table des matières, sections par clause/processus, sous-sections par exigence selon la structure ci-dessus).
7. **Créer ou réutiliser `projets/normes/exigences/verify-exigences.ps1`** (script de validation générique, paramétrable par norme : identifiants uniques sans doublon, présence d'une catégorie, présence d'une référence source et description présente).
8. **Comparer à la source officielle**, corriger les mismatches, marquer `Candidat` les exigences non vérifiables (conformément à `US-NORM-003` / `RM-NORM-003`).
9. **Mettre à jour `projets/normes/README.md`** pour référencer le livrable de la norme traitée (lien vers `<norme-id>-exigences.md` dans le tableau des livrables).

## Fichiers à créer (une fois pour le dossier, puis un livrable par norme)

- `projets/normes/exigences/README.md` — README du dossier (rôle, convention de nommage, liste des normes traitées)
- `projets/normes/exigences/<norme-id>-exigences.md` — livrable principal pour la norme (markdown structuré, en anglais)
- `projets/normes/exigences/verify-exigences.ps1` — script de vérification générique (paramétrable par norme)

## Fichiers à modifier

- `projets/normes/README.md` — mettre à jour le tableau des livrables avec le lien et le statut de chaque norme traitée

## Vérification (par norme)

- [ ] Le dossier `projets/normes/exigences/` existe avec son README
- [ ] Le format de la source officielle a été identifié et la méthode d'extraction choisie documentée
- [ ] Le contenu de la source a été extrait et sauvegardé pour audit
- [ ] Nombre d'exigences extraites : maximum retrouvable
- [ ] Chaque exigence a un ID officiel unique
- [ ] Chaque exigence a une catégorie, une version, une référence source, un statut
- [ ] Chaque exigence a une description présente
- [ ] Le livrable est rédigé en anglais
- [ ] Script `verify-exigences.ps1` passe sans erreur pour la norme traitée
- [ ] Comparaison à la source : 0 mismatch sur les exigences marquées `Vérifié`
- [ ] Les exigences non vérifiables sont explicitement `Candidat` ou `Non vérifié`
- [ ] Le fichier markdown est lisible et structuré (table des matières, sections)
- [ ] Le README du projet normes référence le livrable de la norme traitée

## Risques / Considérations

- **Format de source variable** : la source officielle peut être un PDF, une page HTML, un portail web ou un contenu inaccessible. La méthode d'extraction s'adapte (plans A/B/C/D). Le livrable documente la méthode réellement utilisée.
- **Accès réseau** : le téléchargement depuis la source officielle peut échouer (403, SSL, paywall). Plan B : utiliser une copie déjà présente dans `normes-software-embarque-automobile/sources-downloads/` comme copie de travail, en gardant la référence à la source officielle dans le livrable.
- **Extraction limitée** : si le contenu n'est pas récupérable (PDF scanné, polices non standard, contenu dynamique JS), les exigences seront marquées `Candidat` conformément à `RM-NORM-003`.
- **Volume** : une norme complète peut contenir 200+ exigences. Le fichier markdown sera volumineux mais c'est attendu (exhaustivité demandée).
- **Droits** : extraction de contenu pour analyse interne, pas de redistribution du contenu intégral.
- **Langue** : les livrables sont rédigés en anglais, conformément à la langue des sources officielles (objectif 9 du README).
- **Spécificité par norme** : la structure normative (clauses vs processus vs règles) diffère selon la norme. Le parser et le livrable s'adaptent à la structure propre de chaque norme.

## Avancement

| Norme | Version | Livrable | Exigences | Statut | Date |
|---|---|---|---|---|---|
| Automotive SPICE PAM | v4.0 | `exigences/automotive-spice-exigences.md` | 211 | Vérifié | 2026-09-09 |
| IEC 61508 | éd. 2.0 | `exigences/iec-61508-exigences.md` | 17 | Partiel (preview) | 2026-09-09 |
| ISO 15765 | 2011/2021/2024 | `exigences/iso-15765-exigences.md` | 51 | Partiel (preview) | 2026-09-09 |
| ISO/PAS 5112 | 2022 | `exigences/iso-pas-5112-exigences.md` | 34 | Partiel (preview) | 2026-09-09 |
| ISO/SAE 21434 | 2021 | `exigences/iso-sae-21434-exigences.md` | 29 | Partiel (preview) | 2026-09-09 |
| **Total** | | | **342** | | |

### Scripts d'extraction

- `exigences/extract-norme.ps1` — script d'extraction générique paramétrable par norme (PDF + web + fichier local)
- `exigences/verify-exigences.ps1` — script de vérification générique (IDs uniques, champs obligatoires, descriptions)

### Limitations

- **Automotive SPICE** : PDF officiel non chiffré, extraction complète (211 exigences vérifiées)
- **IEC 61508** : preview PDF non chiffré mais limité au TOC + scope (17 exigences, 4 vérifiées, 13 candidates)
- **ISO/SAE 21434, ISO/PAS 5112, ISO 15765** : PDFs chiffrés, extraction depuis contenu web public (sources secondaires). Exigences marquées `Verified` si texte source retrouvé, `Candidate` sinon.
