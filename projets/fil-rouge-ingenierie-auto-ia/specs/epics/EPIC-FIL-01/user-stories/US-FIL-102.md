# US-FIL-102 — Lire un journal complet de run

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-01`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-102`](../features/FEAT-FIL-102/FEATURE.md)
- **Jour :** `J06`
- **Sources de formation :** [`C03-RETOUR`](../../../baseline/sources.md#c03-retour) — `J03` / Plan préalable, bornes et comparaisons des tests générés, concurrence, doubles, contrôles dans la chaîne / `retour_rapporte`<br>[`C06-G5`](../../../baseline/sources.md#c06-g5) — `J06` / Comparaison, journal complet, interruption et mémoire ; revue G5 / `programme_prevu`
- **Relation pédagogique :** Journal de run lisible et attribuable, annoncé puis exercé en J06.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** opérateur — personne à désigner
- **Dépendances :** [`US-FIL-101`](US-FIL-101.md)
- **Ambiguïté :** [`AMB-02`](../../../governance/ambiguities.md#amb-02)

## Besoin

> En tant qu’opérateur, je veux retrouver chaque transition et sa provenance dans un journal afin d’expliquer un arrêt sans information orale.

## Périmètre

Journal d'un run séquentiel ; le stockage distribué est exclu.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Run autorisé, versions de code/configuration, mode réel ou fixture ou replay, horloge contrôlée pour les tests.
- **Sortie :** Observation : événements ordonnés avec run_id, event_id, séquence, étape, transition, auteur, décision, références d'entrée/sortie, durée, erreur et versions ; pas de contenu brut sensible.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-102"></a>
`RM-FIL-102` — Chaque transition exécutée laisse un événement attribuable au même run, y compris l'arrêt sur erreur.

<a id="ca-fil-102-01"></a>
- [ ] `CA-FIL-102-01` — Étant donné le run R1 franchit trois étapes, quand un tiers lit le journal, alors il retrouve les trois transitions ordonnées et leurs références de versions.
<a id="ca-fil-102-02"></a>
- [ ] `CA-FIL-102-02` — Étant donné R1 est interrompu après une seule étape, quand le tiers lit le journal partiel, alors la dernière étape terminée reste identifiable sans événement de réussite inventé.
<a id="ca-fil-102-03"></a>
- [ ] `CA-FIL-102-03` — Étant donné un fournisseur lève une erreur, quand le workflow journalise l'arrêt, alors un événement d'erreur assaini est présent sans prompt complet ni donnée personnelle.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | le run R1 franchit trois étapes | un tiers lit le journal | il retrouve les trois transitions ordonnées et leurs références de versions |
| Frontière | R1 est interrompu après une seule étape | le tiers lit le journal partiel | la dernière étape terminée reste identifiable sans événement de réussite inventé |
| Refus | un fournisseur lève une erreur | le workflow journalise l'arrêt | un événement d'erreur assaini est présent sans prompt complet ni donnée personnelle |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Lire un journal complet de run
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-102
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-102-01
    Étant donné le run R1 franchit trois étapes
    Quand un tiers lit le journal
    Alors il retrouve les trois transitions ordonnées et leurs références de versions

  Scénario: Frontière — CA-FIL-102-02
    Étant donné R1 est interrompu après une seule étape
    Quand le tiers lit le journal partiel
    Alors la dernière étape terminée reste identifiable sans événement de réussite inventé

  Scénario: Refus — CA-FIL-102-03
    Étant donné un fournisseur lève une erreur
    Quand le workflow journalise l'arrêt
    Alors un événement d'erreur assaini est présent sans prompt complet ni donnée personnelle
```

## Oracle indépendant

Séquence d'événements attendue écrite avant exécution ; horloge et fournisseur factices ; comparaison champ par champ avec la séquence observée, pas avec un second export du même journal.

## Réalisation et preuves

- [`FEAT-FIL-102`](../features/FEAT-FIL-102/FEATURE.md) — Feature candidate
- [`TASK-FIL-102-01`](../features/FEAT-FIL-102/tasks/TASK-FIL-102-01.md) — Définir les champs du journal et une séquence R1 succès/interruption/erreur avec durées factices.
- [`TASK-FIL-102-02`](../features/FEAT-FIL-102/tasks/TASK-FIL-102-02.md) — Instrumenter les transitions de l'orchestrateur et la sérialisation des événements sans changer les décisions métier.
- [`TASK-FIL-102-03`](../features/FEAT-FIL-102/tasks/TASK-FIL-102-03.md) — Faire expliquer le journal par un pair, tester l'événement manquant et vérifier l'absence de contenu sensible.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-02`](../../../governance/ambiguities.md#amb-02).
