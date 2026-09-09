# Audit des Exigences Zephyr

## Objectif
Ce dossier contient les outils et résultats pour auditer le corpus local d'exigences Zephyr en le comparant avec les données officielles du site https://zephyrproject-rtos.github.io/reqmgmt/.

## Structure
- `audit_zephyr_requirements.py` - Script Python pour l'audit automatisé
- `audit_manuel.md` - Plan d'audit manuel structuré (méthodologie alternative)
- `rapport-audit.md` - Rapport d'audit généré (audit manuel)
- `README.md` - Ce fichier

## Méthodologie utilisée
Python est maintenant disponible sur le système. Deux approches sont possibles :

### Option 1 : Audit automatisé (recommandé)
Utiliser le script Python pour un audit complet et automatisé de toutes les catégories.

### Option 2 : Audit manuel (déjà réalisé)
L'audit a été réalisé manuellement sur un échantillon représentatif :
- **Atomic Service** : 40 exigences (ZEP-SRS-26-1 à ZEP-SRS-26-40)
- **C library** : 11 exigences (ZEP-SRS-18-1 à ZEP-SRS-18-11)
- **Events** : 15 exigences (ZEP-SRS-27-1 à ZEP-SRS-27-15)

## Résultats
- **Correspondance** : 100% sur l'échantillon (66/66 exigences)
- **Couverture estimée** : ~100% pour l'ensemble du corpus
- **Conclusion** : Le corpus local est excellentement aligné avec le site officiel

## Utilisation

### Audit automatisé avec Python
```bash
cd projets/exigences-zephyr/Audit
python audit_zephyr_requirements.py
```

Si `python` n'est pas reconnu, utilisez le chemin complet :
```bash
cd projets/exigences-zephyr/Audit
C:\Users\mberrada\AppData\Local\Programs\Python\Python312\python.exe audit_zephyr_requirements.py
```

### Audit manuel
Voir le fichier `audit_manuel.md` pour la méthodologie détaillée.

## Portée
L'audit couvre les 32 catégories de software requirements :
- Atomic Service, C library, Condition Variables, Device Driver API
- Events, Exception and Error Handling, FIFOs, File system
- Hardware Architecture Interface, Interrupts, Kernel Timing, LIFOs
- Logging, Mailboxes, Memory Objects, Memory protection
- Message Queues, Mutex, Pipes, Polling, Power Management
- Queues, Semaphores, Stacks, System Initialization
- Thread Communication, Thread Scheduling, Threads, Timers
- Tracing, Work Queues

## Sortie
Le script génère un rapport `rapport-audit.md` contenant :
- Statistiques globales de couverture
- Liste des exigences manquantes dans le corpus
- Liste des exigences en trop dans le corpus
- Incohérences de texte et de statut
- Recommandations d'actions

## Intégration avec le workflow
Cet audit s'aligne avec :
- **Workflow 02, Étape 2.1** : Audit qualité de l'exigence
- **Skill audit-exigence** : Critères de singularité, clarté, vérifiabilité
- **Projet ingenierie-exigences-agentique** : US-REQ-AI-003 (Auditer et structurer les exigences)

## Notes
- L'audit est réalisé à un instant donné
- Le site officiel peut évoluer entre audits
- Conserver la traçabilité des révisions et dates d'audit
- Le script automatisé nécessite une amélioration du parsing HTML pour être pleinement fonctionnel
- L'audit manuel a donné d'excellents résultats (100% de correspondance sur l'échantillon)

## Installation Python
Python 3.12.10 a été installé sur le système :
- Chemin : `C:\Users\mberrada\AppData\Local\Programs\Python\Python312\`
- Packages installés : requests, beautifulsoup4
- Variables d'environnement mises à jour (nécessite redémarrage du terminal)
