# Guide de récupération manuelle des sources normatives

Ce document décrit, pour chaque norme du projet, les étapes manuelles qu'un humain peut suivre pour récupérer la source officielle ou un substitut public exploitable. Il complète le script automatisé `exigences/extract-norme.ps1` en documentant les actions que la machine ne peut pas réaliser seule (tunnels paywalled, captchas, achats, accès institutionnels).

## Conventions

- **Source officielle** : document publié par l'organisme normatif (ISO, IEC, SAE, VDA) et dont l'authenticité est vérifiable.
- **Preview** : extrait gratuit publié par l'éditeur, souvent limité à la table des matières et au scope.
- **Miroir / secondaire** : site tiers (national, universitaire, technique) reproduisant tout ou partie du contenu. À utiliser avec prudence et à marquer `Candidate`.
- **Statut final** : `Verified` (passage retrouvé dans la source), `Candidate` (inféré ou partiel), `Not verified` (source inaccessible).

Pour chaque norme, l'opérateur doit :
1. Identifier la source la plus fiable.
2. Télécharger ou consulter le document.
3. Vérifier la version et l'édition.
4. Enregistrer le fichier dans `projets/normes/exigences/_sources/<norme-id>/` (créer le dossier si besoin).
5. Noter l'URL, la date d'accès et le type de source dans le livrable Markdown.

---

## 1. Automotive SPICE PAM v4.0

### Source officielle
- **PDF VDA QMC** : https://vda-qmc.de/wp-content/uploads/2023/12/Automotive-SPICE-PAM-v40.pdf
- **Site officiel** : https://automotivespice.com/

### Étapes manuelles
1. Ouvrir https://vda-qmc.de/wp-content/uploads/2023/12/Automotive-SPICE-PAM-v40.pdf dans un navigateur.
2. Vérifier que le PDF s'affiche entièrement (≈ 240 pages, non chiffré).
3. Télécharger le fichier (`Ctrl+S` ou menu → Enregistrer sous).
4. Renommer en `Automotive-SPICE-PAM-v4.0.pdf` et le placer dans `projets/normes/exigences/_sources/automotive-spice/`.
5. Noter la date de téléchargement et la taille du fichier (≈ 2 Mo).
6. Vérifier la page de titre : « Automotive SPICE Process Assessment / Reference Model v4.0 ».

### Vérification
- Le PDF est **non chiffré** : l'extraction automatisée via `extract-norme.ps1` fonctionne.
- Aucune action manuelle supplémentaire n'est requise pour cette norme.

---

## 2. IEC 61508 (toutes parties, édition 2.0)

### Source officielle
- **Portail IEC Functional Safety** : https://www.iec.ch/functionalsafety
- **Webstore IEC** : https://webstore.iec.ch/ (rechercher « IEC 61508 »)

### Étapes manuelles

#### Option A — Achat ou accès institutionnel (recommandé)
1. Aller sur https://webstore.iec.ch/ et rechercher « IEC 61508 ».
2. Sélectionner l'édition 2.0 (2010) pour chaque partie nécessaire :
   - IEC 61508-1 (General requirements)
   - IEC 61508-2 (Requirements for E/E/PE safety-related systems)
   - IEC 61508-3 (Software requirements)
   - IEC 61508-4 (Definitions and abbreviations)
3. Acheter la version PDF ou utiliser un accès institutionnel (entreprise, université, bibliothèque nationale).
4. Télécharger le PDF et le placer dans `projets/normes/exigences/_sources/iec-61508/`.
5. Vérifier la page de titre : « IEC 61508-x Edition 2.0 2010-04 ».

#### Option B — Preview public (limité)
1. Ouvrir la page preview IEC :
   https://webstore.iec.ch/en/iec_catalog/product/preview/?id=L3B1Yi9wZGYvcHJldmlldy9pbmZvX2llYzYxNTA4LTF7ZWQyLjB9Yi5wZGY
2. Le preview contient uniquement la table des matières et le scope (≈ 10-15 pages).
3. Enregistrer le PDF affiché dans `projets/normes/exigences/_sources/iec-61508/preview/`.
4. Marquer toutes les exigences extraites comme `Candidate` sauf si le passage est retrouvé dans le preview.

#### Option C — Miroir technique tchèque (preview non chiffré)
1. Ouvrir https://www.technickenormy.cz/publicdoc/iec_previews/76615.pdf
2. Vérifier qu'il s'agit bien du preview IEC 61508-1 éd. 2.0.
3. Télécharger et placer dans `projets/normes/exigences/_sources/iec-61508/`.
4. Ce PDF est **non chiffré** et exploitable par le script, mais limité au TOC + scope.

### Vérification
- Édition 2.0 (2010-04) = référence courante.
- L'édition 3.0 n'existe pas encore à ce jour ; vérifier sur le webstore IEC si une nouvelle édition est publiée.

---

## 3. ISO 15765 (DoCAN, parties 1, 2, 4)

### Source officielle
- **ISO 15765-1:2011** : https://www.iso.org/standard/54498.html
- **ISO 15765-2:2024** : https://www.iso.org/standard/84209.html (Part 2, transport protocol)
- **ISO 15765-4:2021** : https://www.iso.org/standard/71611.html (Part 4, emissions-related)

### Étapes manuelles

#### Option A — Achat ou accès institutionnel (recommandé)
1. Ouvrir chaque page ISO ci-dessus.
2. Ajouter au panier et acheter la version PDF, ou utiliser un accès institutionnel.
3. Télécharger les PDFs et les placer dans `projets/normes/exigences/_sources/iso-15765/` :
   - `ISO-15765-1-2011.pdf`
   - `ISO-15765-2-2024.pdf`
   - `ISO-15765-4-2021.pdf`
4. Vérifier les pages de titre et les années d'édition.

#### Option B — Previews publics (limités, PDFs chiffrés)
1. **Part 1 (2011)** : https://cdn.standards.iteh.ai/samples/54498/25a04d7fab09480e886fbc5ebfb15090/ISO-15765-1-2011.pdf
2. **Part 2 (2011)** : https://cdn.standards.iteh.ai/samples/54499/2a977e03a16341ef904152ef97a0d74b/ISO-15765-2-2011.pdf
3. **Part 2 (2004)** : https://cdn.standards.iteh.ai/samples/33616/91e9d8e4e8de4b3d97f8a4ce2ffbb2c9/ISO-15765-2-2004.pdf
4. **Part 4 (2021)** : https://cdn.standards.iteh.ai/samples/iso/iso-15765-4-2021/73ffb7b6247441648184e6da0af17f1f/iso-15765-4-2021.pdf
5. Télécharger chaque preview.
6. **Attention** : ces PDFs sont **chiffrés** (encryption standard PDF). Le script automatisé ne peut pas les lire directement.
7. Ouvrir chaque PDF dans Adobe Reader ou Edge et consulter la table des matières + le scope.
8. Noter manuellement la structure des clauses pour chaque partie.
9. Marquer toutes les exigences comme `Candidate` ou `Not verified`.

#### Option C — Catalogue iteh.ai (nécessite JavaScript)
1. Ouvrir https://standards.iteh.ai/catalog/standards/iso/0187930c-6e83-410a-8c8f-b1534995564b/iso-15765-2-2024
2. La page nécessite JavaScript : utiliser un navigateur normal (pas `Invoke-WebRequest`).
3. Consulter la description et la table des matières affichées.
4. Copier manuellement la liste des clauses dans un fichier texte.

#### Option D — Documentation technique publique
1. Consulter https://www.kernel.org/doc/Documentation/networking/iso15765-2.rst
2. Cette page décrit l'implémentation Linux d'ISO 15765-2 (ISO-TP) et liste les paramètres et flags.
3. Utiliser comme source secondaire pour valider les paramètres techniques.

### Vérification
- ISO 15765-2:2024 remplace ISO 15765-2:2016 qui remplace ISO 15765-2:2011.
- Vérifier la cohérence des parties utilisées dans le livrable.

---

## 4. ISO/PAS 5112:2022

### Source officielle
- **Page ISO** : https://www.iso.org/standard/80840.html

### Étapes manuelles

#### Option A — Achat ou accès institutionnel (recommandé)
1. Ouvrir https://www.iso.org/standard/80840.html.
2. Acheter la version PDF ou utiliser un accès institutionnel.
3. Télécharger et placer dans `projets/normes/exigences/_sources/iso-pas-5112/ISO-PAS-5112-2022.pdf`.
4. Vérifier la page de titre : « ISO/PAS 5112:2022 — Road vehicles — Guidelines for auditing cybersecurity engineering ».

#### Option B — Preview public (PDF chiffré)
1. Ouvrir https://cdn.standards.iteh.ai/samples/80840/6cb26fba8a014babad417fdc0d8c96bc/ISO-PAS-5112-2022.pdf
2. Télécharger le preview.
3. **Attention** : PDF **chiffré**, extraction automatisée impossible.
4. Ouvrir dans Adobe Reader ou Edge, consulter la table des matières et le scope.
5. Noter manuellement la structure des clauses.

#### Option C — Sources secondaires (web)
1. **VxLabs** : https://vxlabs.ai/resources/iso-pas-5112-audit-guide/
   - Guide détaillé sur ISO/PAS 5112, liste les clauses et exigences d'audit.
2. **NEN (Pays-Bas)** : https://www.nen.nl/iso-pas-5112-2022-en-294883
   - Description officielle néerlandaise avec résumé du contenu.
3. Consulter ces pages et extraire manuellement les clauses et exigences listées.
4. Marquer les exigences comme `Candidate` (source secondaire).

### Vérification
- ISO/PAS 5112:2022 est un PAS (Publicly Available Specification), donc théoriquement plus accessible qu'une norme ISO complète, mais le PDF reste payant sur le webstore ISO.

---

## 5. ISO/SAE 21434:2021

### Source officielle
- **Page ISO** : https://www.iso.org/standard/70918.html

### Étapes manuelles

#### Option A — Achat ou accès institutionnel (recommandé)
1. Ouvrir https://www.iso.org/standard/70918.html.
2. Acheter la version PDF ou utiliser un accès institutionnel.
3. Télécharger et placer dans `projets/normes/exigences/_sources/iso-sae-21434/ISO-SAE-21434-2021.pdf`.
4. Vérifier la page de titre : « ISO/SAE 21434:2021 — Road vehicles — Cybersecurity engineering ».

#### Option B — Preview public (PDF chiffré)
1. Ouvrir https://cdn.standards.iteh.ai/samples/70918/aa7103c3560f406c86ccdbfec4a0d8de/ISO-SAE-21434-2021.pdf
2. Télécharger le preview.
3. **Attention** : PDF **chiffré**, extraction automatisée impossible.
4. Ouvrir dans Adobe Reader ou Edge, consulter la table des matières et le scope.
5. Noter manuellement les 15 clauses et leurs sous-clauses.

#### Option C — Preview national (Luxembourg)
1. Ouvrir https://ilnas.services-publics.lu/ecnor/downloadPreview.action?documentReference=263062
2. Ce preview est plus complet que celui d'iteh.ai mais reste **chiffré**.
3. Télécharger et consulter dans un lecteur PDF.

#### Option D — Sources secondaires (web, recommandé pour complétude)
1. **Rappel Cybersecurity** : https://www.rappel-cybersecurity.com/iso-sae-21434
   - Description détaillée des 15 clauses (5 à 15) avec objectifs et exigences.
2. **Emenda** : https://emenda.com/iso-21434-compliance-for-automotive/
   - Résumé des sections et exigences clés (notamment Section 10).
3. **fortiss** : https://www.fortiss.org/fileadmin/user_upload/06_Ergebnisse/Whitepaper/fortiss-whitepaper-security-engineering-ISO-web.pdf
   - Whitepaper technique décrivant la structure des clauses.
4. **EVS (Estonie)** : https://www.evs.ee/en/iso-sae-21434-2021
   - Description officielle estonienne avec résumé.
5. Consulter ces pages et extraire manuellement les clauses et exigences.
6. Marquer les exigences comme `Verified` si le passage est retrouvé dans une source, `Candidate` sinon.

### Vérification
- ISO/SAE 21434:2021 est l'édition courante (publiée en août 2021).
- Vérifier l'absence d'amendement ou de nouvelle édition sur le webstore ISO.

---

## Récapitulatif des sources

| Norme | Source officielle | Preview public | Chiffré ? | Source secondaire recommandée |
|---|---|---|---|---|
| Automotive SPICE v4.0 | PDF VDA QMC (gratuit) | = officiel | Non | — |
| IEC 61508 éd. 2.0 | Webstore IEC (payant) | technickenormy.cz | Non (preview) | — |
| ISO 15765 | Webstore ISO (payant) | iteh.ai | Oui | kernel.org (Part 2) |
| ISO/PAS 5112:2022 | Webstore ISO (payant) | iteh.ai | Oui | vxlabs.ai, nen.nl |
| ISO/SAE 21434:2021 | Webstore ISO (payant) | iteh.ai, ilnas.lu | Oui | rappel-cybersecurity.com, emenda.com |

## Actions manuelles indispensables

Les actions suivantes ne peuvent pas être automatisées et nécessitent une intervention humaine :

1. **Achat des normes ISO/IEC** : les PDFs complets sont payants sur le webstore ISO et le webstore IEC. Aucun script ne peut contourner ce paywall légalement.
2. **Ouverture des PDFs chiffrés** : les previews ISO sont chiffrés (encryption standard PDF). Seul un lecteur PDF interactif (Adobe Reader, Edge) peut les afficher. L'extraction programmatique du texte est bloquée.
3. **Validation des versions** : vérifier sur le site officiel qu'aucune nouvelle édition n'a été publiée depuis la dernière extraction.
4. **Comparaison exigences / source** : pour chaque exigence marquée `Verified`, un humain doit confirmer que le texte correspond bien au passage source.
5. **Désencryption** : si un PDF acheté est chiffré, utiliser Adobe Reader avec les identifiants de l'acheteur pour l'ouvrir, puis « Enregistrer sous » pour générer une version non chiffrée exploitable par le script.

## Après récupération manuelle

Une fois les sources officielles récupérées manuellement :

1. Placer les PDFs dans `projets/normes/exigences/_sources/<norme-id>/`.
2. Relancer le script d'extraction :
   ```powershell
   powershell -ExecutionPolicy Bypass -File exigences/extract-norme.ps1 `
     -NormeId "<norme-id>" `
     -NormeName "<nom complet>" `
     -NormeVersion "<version>" `
     -SourceUrl "<url source officielle>" `
     -LocalSource "exigences/_sources/<norme-id>/<fichier>.txt" `
     -OutDir "exigences"
   ```
3. Vérifier le livrable :
   ```powershell
   powershell -ExecutionPolicy Bypass -File exigences/verify-exigences.ps1 -MdPath exigences/<norme-id>-exigences.md
   ```
4. Comparer chaque exigence `Verified` au PDF source.
5. Mettre à jour le statut dans `projets/normes/README.md`.
