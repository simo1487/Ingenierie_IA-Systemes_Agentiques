# Explication — Audit d'alignement avec la formation

- **Périmètre de l’audit :** Alignement documentaire du fil rouge sur les supports locaux J01–J08 et les synthèses de séance J02–J05 ; pas une mesure d'apprentissage ni une preuve d'implémentation.
- **Autorité des sources :** Cours actuels pour les concepts et consignes ; notes comme propos rapportés à confirmer ; décisions projet et oracles revus humainement pour l'application. J02–J05 : reference-technique est désormais une suite du cours, pas globalement une archive. J06–J08 : l'archive facultative n'ajoute pas ses anciens quotas au parcours guidé.
- **Politique de révision :** Les chemins et lignes désignent les fichiers de travail lus pendant l'audit, potentiellement non commités. Les HEAD antérieurement consignés ne figent pas leurs octets. Ne pas présenter cette lecture comme un enregistrement exhaustif des séances.

Le registre canonique est [`formation-alignment.json`](../formation-alignment.json). Il ne prétend pas couvrir exhaustivement les échanges oraux. Le contrôle structurel vérifie le rendu et les relations déclarées ; il ne constitue ni une revue sémantique des critères, ni une preuve comportementale, ni une acceptation métier.

## AUD-FIL-01

- **Sévérité :** `majeur`
- **Observation :** Le backlog initial ne référençait que J06–J08 et présumait les prérequis J02–J05.
- **Sources :** [`C02`](sources.md#c02), [`C03`](sources.md#c03), [`C04`](sources.md#c04), [`C05`](sources.md#c05)
- **Disposition retenue :** EPIC-FIL-00 et US-FIL-1 à 6 rendent les acquis contrôlables, sans obligation de refaire les travaux existants.
- **User Stories affectées :** [`US-FIL-1`](../epics/EPIC-FIL-00/user-stories/US-FIL-1.md), [`US-FIL-2`](../epics/EPIC-FIL-00/user-stories/US-FIL-2.md), [`US-FIL-3`](../epics/EPIC-FIL-00/user-stories/US-FIL-3.md), [`US-FIL-4`](../epics/EPIC-FIL-00/user-stories/US-FIL-4.md), [`US-FIL-5`](../epics/EPIC-FIL-00/user-stories/US-FIL-5.md), [`US-FIL-6`](../epics/EPIC-FIL-00/user-stories/US-FIL-6.md)
- **Statut :** `Correction documentaire candidate ; réalisation métier non vérifiée`

## AUD-FIL-02

- **Sévérité :** `majeur`
- **Observation :** L'amélioration RAG reposait surtout sur l'extension sémantique ; préparation des passages et support des affirmations n'étaient pas des US autonomes.
- **Sources :** [`C04`](sources.md#c04), [`C04-RETOUR`](sources.md#c04-retour)
- **Disposition retenue :** US-FIL-4 et 5 distinguent corpus, requête directe et réponse ; MES-03/MES-06 séparent leurs oracles.
- **User Stories affectées :** [`US-FIL-4`](../epics/EPIC-FIL-00/user-stories/US-FIL-4.md), [`US-FIL-5`](../epics/EPIC-FIL-00/user-stories/US-FIL-5.md), [`US-FIL-404`](../epics/EPIC-FIL-04/user-stories/US-FIL-404.md)
- **Statut :** `Correction documentaire candidate ; réalisation métier non vérifiée`

## AUD-FIL-03

- **Sévérité :** `majeur`
- **Observation :** MES-05 utilisait un ROI sur coûts bruts différent du ROI incrémental enseigné en J05 ; leur mélange pourrait compter deux fois la revue humaine.
- **Sources :** [`C05-ROI`](sources.md#c05-roi), [`C08`](sources.md#c08)
- **Disposition retenue :** MES-05 reprend N, t0, t1, h, I et R ; temps humain dans t1 et non à nouveau dans R, bénéfice négatif conservé.
- **User Stories affectées :** [`US-FIL-602`](../epics/EPIC-FIL-06/user-stories/US-FIL-602.md)
- **Statut :** `Correction documentaire candidate ; réalisation métier non vérifiée`

## AUD-FIL-04

- **Sévérité :** `majeur`
- **Observation :** Le validateur imposait exactement trois cas et trois tâches ; certains cas de concurrence étaient rangés sous Frontière pour tenir ce format.
- **Sources :** [`C02`](sources.md#c02), [`C03-RETOUR`](sources.md#c03-retour), [`C06`](sources.md#c06)
- **Disposition retenue :** Listes extensibles avec catégories explicites et phases propres à la US ; invariants nominal/frontière/refus contrôlés sans plafond.
- **User Stories affectées :** [`US-FIL-3`](../epics/EPIC-FIL-00/user-stories/US-FIL-3.md), [`US-FIL-4`](../epics/EPIC-FIL-00/user-stories/US-FIL-4.md), [`US-FIL-5`](../epics/EPIC-FIL-00/user-stories/US-FIL-5.md), [`US-FIL-201`](../epics/EPIC-FIL-02/user-stories/US-FIL-201.md)
- **Statut :** `Correction documentaire candidate ; réalisation métier non vérifiée`

## AUD-FIL-05

- **Sévérité :** `important`
- **Observation :** Le contrôle JSON/Markdown prouve un rendu fidèle mais ne prouve ni le sens des critères ni leur réalisation.
- **Sources :** [`C02`](sources.md#c02), [`C03`](sources.md#c03), [`C04`](sources.md#c04)
- **Disposition retenue :** Distinguer contrôle structurel, revue de contenu et preuve métier ; conserver les CA futurs non acceptés.
- **User Stories affectées :** [`US-FIL-2`](../epics/EPIC-FIL-00/user-stories/US-FIL-2.md), [`US-FIL-5`](../epics/EPIC-FIL-00/user-stories/US-FIL-5.md), [`US-FIL-502`](../epics/EPIC-FIL-05/user-stories/US-FIL-502.md), [`US-FIL-601`](../epics/EPIC-FIL-06/user-stories/US-FIL-601.md)
- **Statut :** `Correction documentaire candidate ; réalisation métier non vérifiée`

## AUD-FIL-06

- **Sévérité :** `important`
- **Observation :** Les retours de séance contiennent des chiffres, des outils et des décisions rapportés par synthèse automatique, non une baseline normative approuvée.
- **Sources :** [`N02`](sources.md#n02), [`N03`](sources.md#n03), [`N04`](sources.md#n04), [`N05`](sources.md#n05)
- **Disposition retenue :** Qualifier les sources, conserver leurs limites ; ni seuil 0,70/90 %, ni taux 80 %, ni adoption automatique de Qdrant/Docling/LlamaIndex.
- **User Stories affectées :** [`US-FIL-1`](../epics/EPIC-FIL-00/user-stories/US-FIL-1.md), [`US-FIL-4`](../epics/EPIC-FIL-00/user-stories/US-FIL-4.md), [`US-FIL-6`](../epics/EPIC-FIL-00/user-stories/US-FIL-6.md), [`US-FIL-404`](../epics/EPIC-FIL-04/user-stories/US-FIL-404.md)
- **Statut :** `Correction documentaire candidate ; réalisation métier non vérifiée`

## AUD-FIL-07

- **Sévérité :** `important`
- **Observation :** L'ancienne spécification n'avait pas de contrat de choix du mécanisme ni de capitalisation explicite de l'outil avant la comparaison multi-agent.
- **Sources :** [`C01`](sources.md#c01), [`C05`](sources.md#c05), [`C05-SKILL`](sources.md#c05-skill)
- **Disposition retenue :** US-FIL-1 et 6 précèdent les capacités J06 ; l'IA est utilisée pour interpréter/proposer, pas pour remplacer les politiques déterministes.
- **User Stories affectées :** [`US-FIL-1`](../epics/EPIC-FIL-00/user-stories/US-FIL-1.md), [`US-FIL-6`](../epics/EPIC-FIL-00/user-stories/US-FIL-6.md), [`US-FIL-103`](../epics/EPIC-FIL-01/user-stories/US-FIL-103.md), [`US-FIL-301`](../epics/EPIC-FIL-03/user-stories/US-FIL-301.md)
- **Statut :** `Correction documentaire candidate ; réalisation métier non vérifiée`
