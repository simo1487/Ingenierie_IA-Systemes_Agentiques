# Exigences Logicielles Zephyr RTOS — Sémaphores

**Baseline :** `reqmgmt-2026-08-31`
**Document source :** `docs/software_requirements/semaphore.sdoc`
**Statut global :** `Draft`

## ZEP-SRS-5-1 — Définition statique de sémaphore
Le système Zephyr RTOS doit permettre la définition statique d'un sémaphore au moment de la compilation via la macro `K_SEM_DEFINE`.
- **Identifiant officiel :** `ZEP-SRS-5-1`
- **Parent :** `ZEP-SYRS-14`
- **Statut :** `Draft`
- **Conditions :** La valeur initiale du compteur ne doit pas excéder la valeur maximale autorisée.

## ZEP-SRS-5-14 — Priorité des threads en attente
Lorsqu'un sémaphore est libéré (`k_sem_give`) et que plusieurs threads sont en attente, le thread ayant la priorité statique ou dynamique la plus élevée doit être réveillé en premier. À priorité égale, l'ordre d'ancienneté (FIFO) dans la file d'attente s'applique.
- **Identifiant officiel :** `ZEP-SRS-5-14`
- **Parent :** `ZEP-SYRS-14`
- **Statut :** `Draft`

## ZEP-SRS-5-17 — Réinitialisation de sémaphore
L'appel à la fonction de réinitialisation `k_sem_reset` doit remettre le compteur du sémaphore à zéro et réveiller tous les threads en attente avec le code retour `-EAGAIN`.
- **Identifiant officiel :** `ZEP-SRS-5-17`
- **Parent :** `ZEP-SYRS-14`
- **Statut :** `Draft`

## ZEP-SRS-5-19 — Libération au plafond maximal
Lorsqu'un sémaphore est libéré (`k_sem_give`) alors que son compteur a déjà atteint la limite maximale (`limit`), le RTOS Zephyr doit laisser le compteur inchangé sans générer d'erreur fatale.
- **Identifiant officiel :** `ZEP-SRS-5-19`
- **Parent :** `ZEP-SYRS-14`
- **Statut :** `Draft`
- **Statement :** When a semaphore is released while its count is already at the maximum permitted count, the Zephyr RTOS shall leave the count unchanged.

## ZEP-SRS-5-20 — Opérations depuis un contexte d'interruption (ISR)
L'opération de libération `k_sem_give` doit être autorisée depuis une routine de service d'interruption (ISR). L'opération de prise `k_sem_take` n'est autorisée depuis une ISR que si le délai spécifié est strictement égal à `K_NO_WAIT`.
- **Identifiant officiel :** `ZEP-SRS-5-20`
- **Parent :** `ZEP-SYRS-14`
- **Statut :** `Draft`
