# Registre d'ambiguïtés

| ID | Type | Description | Décision attendue | Responsable | Statut |
|---|---|---|---|---|---|
| `AMB-AUD-001` | Ambiguïté | Le seuil de similarité pour la duplication (défaut 0.85) n'est pas approuvé par le responsable qualité. | Figer le seuil avant exécution réelle. | Responsable qualité | `Ouvert` |
| `AMB-AUD-002` | Risque | La détection de duplication lexicale ne détecte pas les reformulations sémantiques. | Définir si un modèle sémantique est requis après le premier lot. | Ingénieur exigences | `Ouvert` |
| `AMB-AUD-003` | Ambiguïté | Le dictionnaire orthographique de référence (français/anglais) n'est pas sélectionné. | Choisir la langue du dataset et le dictionnaire. | Responsable audit | `Ouvert` |
| `AMB-AUD-004` | Risque | La détection de contradiction par patterns peut produire des faux positifs sur les exigences conditionnelles. | Qualifier les faux positifs lors de la revue. | Responsable qualité | `Ouvert` |
| `AMB-AUD-005` | Dépendance | Le dataset réel d'exigences automobiles n'est pas encore fourni. | Fournir le dataset et sa version. | Responsable audit | `Ouvert` |
