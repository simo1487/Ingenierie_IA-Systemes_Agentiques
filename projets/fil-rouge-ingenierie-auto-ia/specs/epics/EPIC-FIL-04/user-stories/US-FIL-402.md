# US-FIL-402 — Éprouver une protection par sa régression

`Référence — spécification candidate`

- **Projet parent :** [`PROJ-FIL-AUTO-IA-001`](../../../../SPEC.md)
- **Epic parente :** [`EPIC-FIL-04`](../EPIC.md)
- **Feature fille :** [`FEAT-FIL-402`](../features/FEAT-FIL-402/FEATURE.md)
- **Jour :** `J07`
- **Sources de formation :** [`C03`](../../../baseline/sources.md#c03) — `J03` / Reproduction, hypothèses concurrentes, rouge/vert comparable, mutation et documentation / `support_actuel`<br>[`C07-G6`](../../../baseline/sources.md#c07-g6) — `J07` / Outil préparé ou replay, refus avant accès, régression et première divergence ; G6 / `programme_prevu`
- **Relation pédagogique :** Spécialisation sécurité du cycle de preuve général et mutation ciblée.
- **Niveau :** `Socle formation`
- **Priorité :** `P1`
- **Statut documentaire :** `Candidate`
- **Statut de preuve :** `Candidat`
- **Travail :** `À faire`
- **Responsable :** relecteur sécurité — personne à désigner
- **Dépendances :** [`US-FIL-3`](../../EPIC-FIL-00/user-stories/US-FIL-3.md), [`US-FIL-401`](US-FIL-401.md)
- **Ambiguïté :** [`AMB-11`](../../../governance/ambiguities.md#amb-11)

## Besoin

> En tant que relecteur sécurité, je veux constater qu'un test échoue quand le garde est retiré afin d’écarter les tests de refus purement textuels.

## Périmètre

Mutation ciblée défensive en environnement isolé ; aucune désactivation de politique de dépôt.

Les décisions restent humaines ; aucune implémentation métier n'est réalisée par cette spécification.

## Entrées et sorties

- **Entrée :** Cas hostile versionné, copie isolée de test et garde d'autorisation identifié ; mutation défensive contrôlée.
- **Sortie :** Observations rouge/vert et mutation avec versions, code retour et décision de revue.

Les baselines sont référencées dans [`sources.md`](../../../baseline/sources.md) ; leur révision est inconnue lorsqu'elle n'y est pas explicitement donnée. La sortie ne constitue pas, à elle seule, une preuve.

## Règle et critères

<a id="rm-fil-402"></a>
`RM-FIL-402` — La protection n'est démontrée par le cas que si celui-ci échoue lorsque le garde ciblé est retiré et passe lorsque le garde est actif.

<a id="ca-fil-402-01"></a>
- [ ] `CA-FIL-402-01` — Étant donné le garde protège l'accès hors portée, quand le cas est exécuté avec puis sans garde dans une copie de test, alors il passe avec le garde et échoue sans lui.
<a id="ca-fil-402-02"></a>
- [ ] `CA-FIL-402-02` — Étant donné la mutation n'a aucun effet sur le résultat, quand le relecteur évalue le test, alors la sensibilité est Non vérifié et le test doit être corrigé.
<a id="ca-fil-402-03"></a>
- [ ] `CA-FIL-402-03` — Étant donné la mutation serait exécutée sur des sources protégées ou un service réel, quand l'essai est préparé, alors l'essai est refusé et une copie de test est exigée.

## Example Mapping

| Cas | Étant donné | Quand | Alors |
|---|---|---|---|
| Nominal | le garde protège l'accès hors portée | le cas est exécuté avec puis sans garde dans une copie de test | il passe avec le garde et échoue sans lui |
| Frontière | la mutation n'a aucun effet sur le résultat | le relecteur évalue le test | la sensibilité est Non vérifié et le test doit être corrigé |
| Refus | la mutation serait exécutée sur des sources protégées ou un service réel | l'essai est préparé | l'essai est refusé et une copie de test est exigée |

## Scénarios Gherkin

```gherkin
Fonctionnalité: Éprouver une protection par sa régression
  Contexte:
    Étant donné le périmètre et les entrées versionnées de US-FIL-402
    Et les attendus ci-dessous définis avant la future réalisation

  Scénario: Nominal — CA-FIL-402-01
    Étant donné le garde protège l'accès hors portée
    Quand le cas est exécuté avec puis sans garde dans une copie de test
    Alors il passe avec le garde et échoue sans lui

  Scénario: Frontière — CA-FIL-402-02
    Étant donné la mutation n'a aucun effet sur le résultat
    Quand le relecteur évalue le test
    Alors la sensibilité est Non vérifié et le test doit être corrigé

  Scénario: Refus — CA-FIL-402-03
    Étant donné la mutation serait exécutée sur des sources protégées ou un service réel
    Quand l'essai est préparé
    Alors l'essai est refusé et une copie de test est exigée
```

## Oracle indépendant

MES-02 ; attendu fixe zéro accès hors portée ; échec du test fondé sur compteur d'accès, pas sur sa propre chaîne de log.

## Réalisation et preuves

- [`FEAT-FIL-402`](../features/FEAT-FIL-402/FEATURE.md) — Feature candidate
- [`TASK-FIL-402-01`](../features/FEAT-FIL-402/tasks/TASK-FIL-402-01.md) — Choisir le contrôle local à muter et figer le cas qui observe réellement l'accès.
- [`TASK-FIL-402-02`](../features/FEAT-FIL-402/tasks/TASK-FIL-402-02.md) — Réaliser rouge/vert et mutation sur une copie isolée, conserver les résultats sans exposer de données réelles.
- [`TASK-FIL-402-03`](../features/FEAT-FIL-402/tasks/TASK-FIL-402-03.md) — Faire revoir la première cause de l'échec et démontrer que la protection et l'environnement d'origine sont préservés.

Aucune preuve d'acceptation de cette US n'est produite par son rendu. Les artefacts existants peuvent satisfaire un prérequis après revue ; aucune répétition de travaux déjà démontrés n'est imposée.

## Questions ouvertes

Voir [`AMB-11`](../../../governance/ambiguities.md#amb-11).
