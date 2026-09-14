# Preuves de vérification — 2026-09-13

## Baseline

- **Branche :** `feat/fil-rouge-ingenierie-auto-ia`
- **Commit de départ :** `335199ef45164d5c6f81ac97aa601ec2e87f56b4`
- **Périmètre :** `projets/fil-rouge-ingenierie-auto-ia/` et son entrée dans `projets/README.md`

## Résultats vérifiés

| Contrôle | Commande | Résultat |
|---|---|---|
| Tests unitaires hors ligne | `PYTHONPATH=src python3 -m unittest discover -s tests -v` | `6 tests`, code `0` |
| Démonstration | `PYTHONPATH=src python3 -m auto_ai_flow.cli --input data/demo_baseline.json --output evidence/demo-run.json` | `ready-for-human-review`, code `0` |
| Compilation Python | `python3 -m compileall -q src tests` | code `0` |
| Whitespace du diff | `git diff --check` | code `0` |
| Contrôle ciblé du dépôt | `tools/check_repo.py::check_path` sur les fichiers modifiés et non suivis | code `0` avant ajout de ce rapport |

## Contrôle global

`make check` a été exécuté depuis la racine et a retourné le code `2`. Les défauts signalés sont antérieurs et hors périmètre du lot : fins de fichiers absentes, espaces finaux et marqueurs de conflit dans `projets/ingenierie-exigences-agentique/`, `projets/logiciel-automobile-open-source/`, `projets/normes/`, `projets/qualite-code/` et `zephyr-os-requirements-traceability.md`.

Ces fichiers n’ont pas été modifiés afin de respecter les frontières des branches d’équipe. Le résultat global reste donc `Bloqué` jusqu’à correction séparée sur les branches responsables.

## Contrôles non réalisés

- Synchronisation distante GitHub : bloquée par l’authentification ; les références du rapport de branches sont locales.
- Appel Mistral réel : aucune clé n’a été utilisée ; seul le refus sans clé est testé.
- Compilation Mermaid : aucun moteur Mermaid n’a été exécuté ; le diagramme a seulement été comparé au code.
- Qdrant, Cppcheck/MISRA et recherche web : prévus comme adaptateurs futurs, non intégrés dans ce MVP.

## Conclusion

Le périmètre du nouveau projet est vérifié hors ligne et produit une proposition prête pour revue humaine. Cette conclusion ne vaut ni validation de Gate G2, ni conformité, ni certification.
