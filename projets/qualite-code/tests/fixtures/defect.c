#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Fixture avec défaut contrôlé - Code C avec défaut explicite injecté
 * Objectif : Valider que la chaîne détecte le défaut et retourne un code non nul
 * conformément à CA-QUAL-05
 *
 * Défaut injecté : Buffer overflow (dépassement de tampon)
 * Ce défaut doit être détecté par :
 * - Cppcheck (analyse statique)
 * - AddressSanitizer (analyse dynamique)
 */

int main(void)
{
    /* Allocation d'un tampon de 10 caractères */
    char buffer[10];
    
    /* DÉFAIT CONTRÔLÉ : Buffer overflow
     * Copie de 15 caractères dans un tampon de 10
     * Cppcheck devrait détecter cela statiquement
     * ASan devrait détecter cela dynamiquement
     */
    strcpy(buffer, "Ceci est trop long pour le tampon");
    
    printf("Contenu du tampon : %s\n", buffer);
    
    return 0;
}