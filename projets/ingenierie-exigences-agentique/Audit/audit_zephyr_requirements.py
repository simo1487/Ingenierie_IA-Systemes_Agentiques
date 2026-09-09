#!/usr/bin/env python3
"""
Script d'audit automatisé des exigences Zephyr
Compare le corpus local avec le site officiel reqmgmt
"""

import requests
from bs4 import BeautifulSoup
import re
from datetime import datetime
import json
import sys
import os

# Configuration
CORPUS_LOCAL_PATH = r"C:\Users\mberrada\FormationIaProject\projets\exigences-zephyr\corpus-exigences-zephyr.md"
ZEPHYR_REQMGMT_BASE_URL = "https://zephyrproject-rtos.github.io/reqmgmt/reqmgmt/docs/software_requirements/"
OUTPUT_REPORT_PATH = r"C:\Users\mberrada\FormationIaProject\projets\exigences-zephyr\Audit\rapport-audit.md"

# Catégories de software requirements à auditer
CATEGORIES = [
    "atomic_service",
    "c_library", 
    "condition_variables",
    "device_driver_api",
    "events",
    "exception_and_error_handling",
    "fifos",
    "file_system",
    "hw_arch_interface",
    "interrupts",
    "kernel_timing",
    "lifos",
    "logging",
    "mailboxes",
    "memory_objects",
    "memory_protection",
    "message_queue",
    "mutex",
    "pipe",
    "poll",
    "power_management",
    "queues",
    "semaphore",
    "stacks",
    "system_initialization",
    "thread_communication",
    "thread_scheduling",
    "threads",
    "timers",
    "tracing",
    "work_queues"
]

def parse_local_corpus(filepath):
    """Parse le corpus local depuis le fichier Markdown"""
    print(f"Parsing du corpus local: {filepath}")
    
    requirements = {}
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extraire les lignes du tableau markdown
        lines = content.split('\n')
        in_table = False
        
        for line in lines:
            if '|---' in line:
                in_table = True
                continue
            
            if in_table and line.startswith('|'):
                # Parser la ligne du tableau
                parts = [p.strip() for p in line.split('|')]
                if len(parts) >= 10 and parts[1] and parts[1] != 'requirement_id':
                    req_id = parts[1]
                    req_text = parts[2]
                    category = parts[6]
                    status = parts[9]
                    
                    requirements[req_id] = {
                        'requirement_id': req_id,
                        'requirement_text': req_text,
                        'category': category,
                        'status': status,
                        'source': 'local'
                    }
    
    except Exception as e:
        print(f"Erreur lors du parsing du corpus local: {e}")
    
    print(f"  -> {len(requirements)} exigences trouvées dans le corpus local")
    return requirements

def fetch_official_requirements(category):
    """Récupère les exigences d'une catégorie depuis le site officiel"""
    url = f"{ZEPHYR_REQMGMT_BASE_URL}{category}.html"
    print(f"  Récupération: {url}")
    
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        soup = BeautifulSoup(response.content, 'html.parser')
        requirements = {}
        
        # Approche alternative : chercher les patterns d'IDs ZEP-SRS dans tout le contenu
        content = soup.get_text()
        
        # Trouver tous les IDs d'exigences
        uid_pattern = re.compile(r'ZEP-SRS-\d+-\d+')
        uids = uid_pattern.findall(content)
        
        # Pour chaque UID trouvé, essayer de trouver le texte associé
        for uid in uids:
            if uid not in requirements:  # Éviter les doublons
                # Chercher le texte après l'ID
                # Utiliser une approche plus robuste : chercher dans le HTML structuré
                uid_elements = soup.find_all(string=lambda text: uid in text)
                
                for element in uid_elements:
                    parent = element.parent
                    # Chercher le texte statement proche
                    # Les statements sont souvent dans des divs ou sections
                    statement_candidates = []
                    
                    # Chercher dans les parents et frères
                    current = parent
                    for _ in range(5):  # Limiter la recherche
                        if current:
                            # Chercher le texte dans cette section
                            section_text = current.get_text(strip=True)
                            if uid in section_text and len(section_text) > len(uid) + 10:
                                # Extraire le texte après l'ID
                                uid_index = section_text.find(uid)
                                potential_statement = section_text[uid_index + len(uid):].strip()
                                if potential_statement and len(potential_statement) > 20:
                                    statement_candidates.append(potential_statement)
                                    break
                            current = current.parent if current.parent else None
                    
                    if statement_candidates:
                        req_text = statement_candidates[0][:200]  # Limiter la longueur
                        
                        requirements[uid] = {
                            'requirement_id': uid,
                            'requirement_text': req_text,
                            'category': category.replace('_', ' ').title(),
                            'status': "Draft",  # Statut par défaut
                            'source': 'official'
                        }
                        break  # Prendre la première correspondance
        
        print(f"    -> {len(requirements)} exigences trouvées")
        return requirements
        
    except Exception as e:
        print(f"    Erreur lors de la récupération: {e}")
        return {}

def compare_requirements(local_reqs, official_reqs):
    """Compare les exigences locales et officielles"""
    print("Comparaison des exigences...")
    
    comparison = {
        'local_only': [],
        'official_only': [],
        'text_mismatches': [],
        'status_mismatches': [],
        'matches': []
    }
    
    # Exigences seulement dans le corpus local
    for req_id, req_data in local_reqs.items():
        if req_id not in official_reqs:
            comparison['local_only'].append(req_id)
        else:
            official_data = official_reqs[req_id]
            
            # Comparer les textes
            if req_data['requirement_text'] != official_data['requirement_text']:
                comparison['text_mismatches'].append({
                    'req_id': req_id,
                    'local_text': req_data['requirement_text'],
                    'official_text': official_data['requirement_text']
                })
            
            # Comparer les statuts
            if req_data['status'] != official_data['status']:
                comparison['status_mismatches'].append({
                    'req_id': req_id,
                    'local_status': req_data['status'],
                    'official_status': official_data['status']
                })
            
            comparison['matches'].append(req_id)
    
    # Exigences seulement sur le site officiel
    for req_id in official_reqs:
        if req_id not in local_reqs:
            comparison['official_only'].append(req_id)
    
    return comparison

def generate_audit_report(local_reqs, official_reqs, comparison):
    """Génère le rapport d'audit en Markdown"""
    print("Génération du rapport d'audit...")
    
    total_local = len(local_reqs)
    total_official = len(official_reqs)
    coverage_rate = (len(comparison['matches']) / total_official * 100) if total_official > 0 else 0
    
    report = f"""# Rapport d'audit - Exigences Zephyr

## Méta-données
- **Date d'audit** : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
- **Source corpus local** : `projets/exigences-zephyr/corpus-exigences-zephyr.md`
- **Source site officiel** : https://zephyrproject-rtos.github.io/reqmgmt/
- **Révision corpus** : b9e702780b6dff096bebb151ab724e6c35fe3cd3
- **Portée** : Software requirements uniquement

## Statistiques globales
- **Total exigences site officiel** : {total_official}
- **Total exigences corpus local** : {total_local}
- **Exigences correspondantes** : {len(comparison['matches'])}
- **Taux de couverture** : {coverage_rate:.1f}%

## Écarts identifiés

### Exigences manquantes dans le corpus ({len(comparison['official_only'])})
Exigences présentes sur le site officiel mais absentes du corpus local :

"""
    
    for req_id in sorted(comparison['official_only']):
        req_data = official_reqs[req_id]
        report += f"- **{req_id}** ({req_data['category']}) : {req_data['requirement_text'][:100]}...\n"
    
    report += f"""
### Exigences en trop dans le corpus ({len(comparison['local_only'])})
Exigences présentes dans le corpus local mais absentes du site officiel :

"""
    
    for req_id in sorted(comparison['local_only']):
        req_data = local_reqs[req_id]
        report += f"- **{req_id}** ({req_data['category']}) : {req_data['requirement_text'][:100]}...\n"
    
    report += f"""
### Incohérences de texte ({len(comparison['text_mismatches'])})
Exigences avec des différences de texte entre corpus et site officiel :

"""
    
    for mismatch in comparison['text_mismatches']:
        report += f"- **{mismatch['req_id']}** :\n"
        report += f"  - Corpus local : {mismatch['local_text'][:80]}...\n"
        report += f"  - Site officiel : {mismatch['official_text'][:80]}...\n"
    
    report += f"""
### Incohérences de statut ({len(comparison['status_mismatches'])})
Exigences avec des différences de statut entre corpus et site officiel :

"""
    
    for mismatch in comparison['status_mismatches']:
        report += f"- **{mismatch['req_id']}** :\n"
        report += f"  - Corpus local : {mismatch['local_status']}\n"
        report += f"  - Site officiel : {mismatch['official_status']}\n"
    
    report += """
## Analyse détaillée par catégorie

### Répartition par catégorie (site officiel)
"""
    
    # Compter par catégorie
    category_counts = {}
    for req_id, req_data in official_reqs.items():
        category = req_data['category']
        category_counts[category] = category_counts.get(category, 0) + 1
    
    for category, count in sorted(category_counts.items()):
        report += f"- **{category}** : {count} exigences\n"
    
    report += """
## Recommandations

### Actions immédiates
"""
    
    if comparison['official_only']:
        report += "1. **Ajouter les exigences manquantes** : Intégrer les " + str(len(comparison['official_only'])) + " exigences présentes sur le site officiel mais absentes du corpus local.\n"
    
    if comparison['local_only']:
        report += "2. **Vérifier les exigences en trop** : Confirmer si les " + str(len(comparison['local_only'])) + " exigences supplémentaires du corpus sont valides ou obsolètes.\n"
    
    if comparison['text_mismatches']:
        report += "3. **Aligner les textes** : Corriger les " + str(len(comparison['text_mismatches'])) + " incohérences de texte pour correspondre à la version officielle.\n"
    
    if comparison['status_mismatches']:
        report += "4. **Synchroniser les statuts** : Mettre à jour les " + str(len(comparison['status_mismatches'])) + " statuts pour correspondre à la version officielle.\n"
    
    report += """
### Actions de suivi
1. Planifier des audits réguliers pour maintenir l'alignement
2. Documenter la procédure de mise à jour du corpus
3. Établir un processus de validation avant toute modification du corpus

## Limites et considérations
- L'audit compare le corpus local avec le site officiel à un instant donné
- Le site officiel peut évoluer entre la révision figée du corpus et cet audit
- Certaines différences de statut peuvent être dues à des mises à jour récentes
- La révision du site consulté lors de cet audit n'est pas figée

## Conclusion
"""
    
    if len(comparison['official_only']) == 0 and len(comparison['local_only']) == 0 and len(comparison['text_mismatches']) == 0:
        report += "✅ Le corpus local est parfaitement aligné avec le site officiel. Aucune action corrective nécessaire.\n"
    else:
        total_issues = len(comparison['official_only']) + len(comparison['local_only']) + len(comparison['text_mismatches']) + len(comparison['status_mismatches'])
        report += f"⚠️ {total_issues} écarts identifiés nécessitent une attention. Voir les sections détaillées ci-dessus pour les actions recommandées.\n"
    
    report += f"""
---
*Rapport généré automatiquement par le script audit_zephyr_requirements.py*
*Date : {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
"""
    
    return report

def main():
    print("=" * 60)
    print("AUDIT AUTOMATISÉ DES EXIGENCES ZEPHYR")
    print("=" * 60)
    
    # Étape 1 : Parser le corpus local
    local_requirements = parse_local_corpus(CORPUS_LOCAL_PATH)
    
    # Étape 2 : Récupérer les exigences officielles
    print("\nRécupération des exigences officielles...")
    official_requirements = {}
    
    for category in CATEGORIES:
        category_reqs = fetch_official_requirements(category)
        official_requirements.update(category_reqs)
    
    print(f"\nTotal exigences officielles récupérées : {len(official_requirements)}")
    
    # Étape 3 : Comparer
    comparison = compare_requirements(local_requirements, official_requirements)
    
    # Étape 4 : Générer le rapport
    report = generate_audit_report(local_requirements, official_requirements, comparison)
    
    # Étape 5 : Sauvegarder le rapport
    print(f"\nSauvegarde du rapport : {OUTPUT_REPORT_PATH}")
    with open(OUTPUT_REPORT_PATH, 'w', encoding='utf-8') as f:
        f.write(report)
    
    print("\n" + "=" * 60)
    print("AUDIT TERMINÉ AVEC SUCCÈS")
    print("=" * 60)
    print(f"Rapport disponible : {OUTPUT_REPORT_PATH}")
    print(f"Exigences analysées : {len(local_requirements)} (local) vs {len(official_requirements)} (officiel)")
    if len(official_requirements) > 0:
        print(f"Taux de couverture : {len(comparison['matches']) / len(official_requirements) * 100:.1f}%")
    else:
        print("Taux de couverture : N/A (aucune exigence officielle récupérée)")

if __name__ == "__main__":
    main()
