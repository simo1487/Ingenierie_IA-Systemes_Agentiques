#!/usr/bin/env python3
"""
Script de vérification des fiches candidat JSON
Vérifie l'existence des URLs canoniques des dépôts et l'activité des projets
"""

import json
import os
import sys
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Tuple
import requests
from urllib.parse import urlparse


class FicheVerifier:
    """Vérificateur de fiches candidat"""
    
    def __init__(self, base_dir: str):
        self.base_dir = Path(base_dir)
        self.results = []
        
    def find_fiche_files(self) -> List[Path]:
        """Trouve tous les fichiers fiche_cand_*.json"""
        pattern = "fiche_cand_*.json"
        files = list(self.base_dir.rglob(pattern))
        return sorted(files)
    
    def check_url_exists(self, url: str) -> Tuple[bool, str]:
        """Vérifie si une URL existe et est accessible"""
        try:
            response = requests.head(url, timeout=10, allow_redirects=True)
            exists = response.status_code in [200, 301, 302, 307, 308]
            status_code = response.status_code
            return exists, f"HTTP {status_code}"
        except requests.RequestException as e:
            return False, f"Erreur: {str(e)}"
    
    def is_project_active(self, fiche_data: Dict) -> Tuple[bool, str]:
        """Vérifie si le projet est actif selon les critères définis"""
        try:
            activite = fiche_data.get('activite_projet', {})
            statut = activite.get('statut', '')
            dernier_commit_str = activite.get('dernier_commit', '')
            
            # Si le statut est déjà défini à "Actif", on considère le projet actif
            if statut.lower() == 'actif':
                return True, f"Statut déclaré: {statut}"
            
            # Si la date du dernier commit est disponible, vérifier si < 30 jours
            if dernier_commit_str:
                try:
                    # Extraire la date (format: "2026-09-04 (pushed_at)")
                    date_str = dernier_commit_str.split('(')[0].strip()
                    dernier_commit = datetime.strptime(date_str, "%Y-%m-%d")
                    seuil_inactivite = datetime.now() - timedelta(days=30)
                    
                    if dernier_commit >= seuil_inactivite:
                        jours_avec_dernier_commit = (datetime.now() - dernier_commit).days
                        return True, f"Dernier commit il y a {jours_avec_dernier_commit} jours"
                    else:
                        jours_avec_dernier_commit = (datetime.now() - dernier_commit).days
                        return False, f"Dernier commit il y a {jours_avec_dernier_commit} jours (seuil: 30 jours)"
                except (ValueError, IndexError) as e:
                    return False, f"Impossible de parser la date: {str(e)}"
            
            # Si aucune information n'est disponible, marquer comme inconnu
            return False, "Informations d'activité insuffisantes"
            
        except Exception as e:
            return False, f"Erreur lors de la vérification: {str(e)}"
    
    def verify_fiche(self, fiche_path: Path) -> Dict:
        """Vérifie une fiche candidat individuelle"""
        result = {
            'fichier': str(fiche_path.relative_to(self.base_dir)),
            'url_canonique': None,
            'url_accessible': False,
            'url_status': '',
            'projet_actif': False,
            'activite_status': '',
            'statut_global': 'OK',
            'erreurs': []
        }
        
        try:
            # Lire le fichier JSON
            with open(fiche_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # Extraire l'URL canonique
            infos_id = data.get('informations_identification', {})
            url_canonique = infos_id.get('url_canonique_depot', '')
            
            if not url_canonique:
                result['erreurs'].append("URL canonique manquante")
                result['statut_global'] = 'ERREUR'
                return result
            
            result['url_canonique'] = url_canonique
            
            # Vérifier l'accessibilité de l'URL
            url_exists, url_status = self.check_url_exists(url_canonique)
            result['url_accessible'] = url_exists
            result['url_status'] = url_status
            
            if not url_exists:
                result['erreurs'].append(f"URL non accessible: {url_status}")
                result['statut_global'] = 'ERREUR'
            
            # Vérifier l'activité du projet
            projet_actif, activite_status = self.is_project_active(data)
            result['projet_actif'] = projet_actif
            result['activite_status'] = activite_status
            
            if not projet_actif:
                result['erreurs'].append(f"Projet inactif: {activite_status}")
                if result['statut_global'] != 'ERREUR':
                    result['statut_global'] = 'ATTENTION'
            
        except json.JSONDecodeError as e:
            result['erreurs'].append(f"Erreur JSON: {str(e)}")
            result['statut_global'] = 'ERREUR'
        except Exception as e:
            result['erreurs'].append(f"Erreur inattendue: {str(e)}")
            result['statut_global'] = 'ERREUR'
        
        return result
    
    def verify_all_fiches(self) -> List[Dict]:
        """Vérifie toutes les fiches candidat"""
        fiches = self.find_fiche_files()
        
        if not fiches:
            print("Aucun fichier fiche_cand_*.json trouvé")
            return []
        
        print(f"Trouvé {len(fiches)} fichier(s) fiche_cand_*.json")
        
        for fiche in fiches:
            print(f"Vérification de {fiche.name}...")
            result = self.verify_fiche(fiche)
            self.results.append(result)
        
        return self.results
    
    def generate_report(self) -> str:
        """Génère un rapport de vérification"""
        if not self.results:
            return "Aucun résultat à rapporter"
        
        report_lines = [
            "=" * 80,
            "RAPPORT DE VÉRIFICATION DES FICHES CANDIDAT",
            "=" * 80,
            f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            f"Total fiches vérifiées: {len(self.results)}",
            ""
        ]
        
        # Statistiques
        ok_count = sum(1 for r in self.results if r['statut_global'] == 'OK')
        attention_count = sum(1 for r in self.results if r['statut_global'] == 'ATTENTION')
        erreur_count = sum(1 for r in self.results if r['statut_global'] == 'ERREUR')
        
        report_lines.extend([
            "STATISTIQUES:",
            f"  ✓ OK: {ok_count}",
            f"  ⚠ ATTENTION: {attention_count}",
            f"  ✗ ERREUR: {erreur_count}",
            ""
        ])
        
        # Détails par fiche
        report_lines.append("DÉTAILS PAR FICHE:")
        report_lines.append("-" * 80)
        
        for result in self.results:
            status_symbol = "✓" if result['statut_global'] == 'OK' else ("⚠" if result['statut_global'] == 'ATTENTION' else "✗")
            
            report_lines.extend([
                f"{status_symbol} {result['fichier']}",
                f"  URL canonique: {result['url_canonique']}",
                f"  Accessibilité: {'OUI' if result['url_accessible'] else 'NON'} ({result['url_status']})",
                f"  Activité: {'ACTIF' if result['projet_actif'] else 'INACTIF'} ({result['activite_status']})",
                f"  Statut global: {result['statut_global']}"
            ])
            
            if result['erreurs']:
                report_lines.append("  Erreurs:")
                for erreur in result['erreurs']:
                    report_lines.append(f"    - {erreur}")
            
            report_lines.append("")
        
        # Résumé des problèmes
        if erreur_count > 0 or attention_count > 0:
            report_lines.extend([
                "RÉSUMÉ DES PROBLÈMES:",
                "-" * 80
            ])
            
            for result in self.results:
                if result['erreurs']:
                    report_lines.append(f"{result['fichier']}:")
                    for erreur in result['erreurs']:
                        report_lines.append(f"  - {erreur}")
                    report_lines.append("")
        
        report_lines.append("=" * 80)
        
        return "\n".join(report_lines)
    
    def save_report(self, output_path: str):
        """Sauvegarde le rapport dans un fichier"""
        report = self.generate_report()
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report)
        print(f"Rapport sauvegardé dans: {output_path}")


def main():
    """Fonction principale"""
    # Répertoire de base du projet
    base_dir = r"C:\temp\GitHub\FormationIaProject"
    
    # Créer le vérificateur
    verifier = FicheVerifier(base_dir)
    
    # Exécuter les vérifications
    verifier.verify_all_fiches()
    
    # Générer et afficher le rapport
    report = verifier.generate_report()
    print(report)
    
    # Sauvegarder le rapport
    output_path = os.path.join(base_dir, "rapport_verification_fiches.txt")
    verifier.save_report(output_path)
    
    # Code de retour basé sur les résultats
    erreur_count = sum(1 for r in verifier.results if r['statut_global'] == 'ERREUR')
    sys.exit(1 if erreur_count > 0 else 0)


if __name__ == "__main__":
    main()