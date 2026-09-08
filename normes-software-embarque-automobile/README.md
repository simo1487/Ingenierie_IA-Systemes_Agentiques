# Référentiel des normes du logiciel embarqué automobile

Ce dossier rassemble un **référentiel de travail structuré** des normes, règlements, standards ouverts et référentiels de bonnes pratiques qui encadrent le logiciel embarqué automobile.

## Important

- Ce n'est pas une copie des normes : la plupart des textes sont protégés par le droit d'auteur et/ou accessibles sous licence payante.
- Les liens pointent vers les pages officielles des organismes émetteurs. Ils permettent de vérifier l'édition, le statut et les modalités d'achat ou de téléchargement.
- Le catalogue est une base de cadrage et n'est pas une preuve de conformité. L'applicabilité dépend du véhicule, du marché, de la fonction, du contrat client et de l'édition applicable.
- Les versions et statuts doivent être revalidés avant chaque projet. La date de constitution de cette base est indiquée dans `normes.yml`.

## Fichiers

| Fichier | Rôle |
|---|---|
| `rapport-organisation.md` | Rapport de synthèse : familles de textes, articulation, cycle de vie et méthode d'utilisation. |
| `normes.yml` | Catalogue structuré et exploitable par un script ou une base documentaire. |
| `sources.csv` | Registre des sources officielles, avec organisme, type d'accès et usage conseillé. |
| `telecharger_sources.py` | Télécharge les ressources accessibles dans `sources-downloads/` et produit un `manifest.json`. |

## Télécharger les sources accessibles

Depuis ce dossier :

```bash
python3 telecharger_sources.py
```

Le script suit les URL de `sources.csv`, conserve chaque ressource sous son `source_id`, et ne contourne pas les paywalls. Les ressources déjà présentes sont conservées ; utiliser `--overwrite` pour les remplacer. Le détail des téléchargements et des éventuels échecs est enregistré dans `sources-downloads/manifest.json`.

## Organisation retenue

Le catalogue sépare cinq niveaux qui ne doivent pas être confondus :

1. **Réglementation** : obligations légales et homologation, notamment UNECE R155/R156.
2. **Normes internationales** : ISO, ISO/SAE, IEC et IEEE ; elles définissent des exigences ou des cadres reconnus.
3. **Référentiels de processus** : Automotive SPICE, IATF 16949 et ISO/IEC 330xx.
4. **Standards d'architecture et d'interopérabilité** : AUTOSAR, CAN, LIN, UDS, DoIP, SOME/IP.
5. **Guides et règles de codage** : MISRA, SAE J3061, CERT C/C++, guides fournisseurs.

## Parcours de lecture conseillé

- **Développer une fonction de sécurité** : ISO 26262 → ISO 21448 si la fonction dépend de la perception ou d'insuffisances fonctionnelles → ISO/TS 5083 pour un système de conduite automatisée.
- **Développer une fonction connectée** : ISO/SAE 21434 → UNECE R155 → ISO 24089 et UNECE R156 pour les mises à jour.
- **Structurer une équipe logicielle** : Automotive SPICE → ISO/IEC 330xx → règles de codage MISRA → preuves de tests et de traçabilité.
- **Choisir une plateforme** : AUTOSAR Classic pour les ECU contraints et temps réel ; AUTOSAR Adaptive pour les calculateurs haute performance ; compléter avec les protocoles de communication applicables.
- **Préparer une homologation** : partir des règlements du marché visé, puis établir la matrice de correspondance vers les normes et les preuves projet.
