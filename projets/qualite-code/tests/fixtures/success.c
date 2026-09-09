#include <stdio.h>
#include <stdlib.h>

/* Fixture de succès - Code C propre sans défauts connus
 * Objectif : Valider que la chaîne de contrôles ne produit pas de faux positifs
 * sur du code correct conformément à CA-QUAL-05
 */

int main(void)
{
    /* Allocation correcte avec vérification */
    int *numbers = (int *)malloc(5 * sizeof(int));
    if (numbers == NULL) {
        fprintf(stderr, "Erreur d'allocation mémoire\n");
        return 1;
    }

    /* Initialisation correcte */
    for (int i = 0; i < 5; i++) {
        numbers[i] = i * 10;
    }

    /* Utilisation correcte des bornes */
    for (int i = 0; i < 5; i++) {
        printf("numbers[%d] = %d\n", i, numbers[i]);
    }

    /* Libération correcte */
    free(numbers);
    numbers = NULL; /* Bonne pratique : éviter dangling pointer */

    return 0;
}