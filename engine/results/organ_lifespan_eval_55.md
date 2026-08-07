**REPORT-ONLY** -- registered look (evening_addons_registration_55 sec.2). No credential language; "magnitude-verified (species subset)" is her adoption's phrase, entered at adoption, not asserted here.

# Temporal-referent organs -- lifespan magnitude eval (Duration-ruler pattern, class-wise)

_Organs emit CLASSES not scalars: this is separation of MEASURED lifespans by assigned class, not rank correlation. 'magnitude-verified (species subset)' is her adoption's phrase, not asserted here._

Organ = CLASSES, not a ruler. Metric = **AUC(enduring > (tight-)ephemeral by MEASURED maximum longevity)** + per-class lifespan distributions. Expectation (registration): the two classes sit orders of magnitude apart.

> **Finding.** Coverage-limited. AnAge Build 15 is vertebrate-centric: the ENDURING members that map land at 10^1.6-10^3.7 yr (tortoise 177, crane 45, bristlecone pine 5062); the EPHEMERAL/tight-ephemeral referents are insects/fungi/short-lived plants (mayfly, epiphyllum, morning-mushroom) and the EN members are botanical/entomological (ferns, wallflowers, magnolia, yew) -- essentially none are in AnAge, so those classes yield 0 measurable species. AUC needs both classes populated -> not computable here; the enduring distribution alone is directionally consistent with the 'orders of magnitude' expectation. A full AUC awaits a longevity DB covering short-lived invertebrates/plants (a separate ledgered acquisition).

## Acquisition (ledgered)
- **AnAge Build 15 (HAGR)**, 2023-07-03 (fetched 2026-07-22)
- sha256(zip) `e3ddb66e32e973a79932859ba53013e8f60d957c6ec01c6eb573e3ea3018d630`
- sha256(anage_data.txt) `98867969fbd4d0bed6bab415c2715bb19079dbd7f92bdc26e5961856aa1c1519`
- license: AnAge / HAGR -- Creative Commons Attribution 3.0 Unported; "free for all purposes, including ... research ... provided you mention the use of HAGR". Cite: de Magalhaes et al. (2024) NAR 52(D1):D900-D908.

## EN (WordNet taxonomic lemmas)
### Coverage (species matched / class members)
| class | members | species matched | sit-out |
|---|---|---|---|
| ephemeral | 73 | **0** | 73 |
| enduring | 29 | **0** | 29 |

**AUC(enduring > ephemeral):** n/a (insufficient coverage: a class has 0 matched species)

### Lifespan distribution (measured max longevity, yrs)
| class | n | median | IQR | min | max |
|---|---|---|---|---|---|
| ephemeral | - | - | - | - | - |
| enduring | - | - | - | - | - |

Order-of-magnitude gap (log10 median enduring - ephemeral): **n/a**

### Sit-outs (listed, never dropped)
- ephemeral: matched_no_lifespan=0, non_species=59, species_unmatched=14
- enduring: matched_no_lifespan=0, non_species=21, species_unmatched=8

## ZH (HowNet W_E glosses, one receipt/mapping)
### Coverage (species matched / class members)
| class | members | species matched | sit-out |
|---|---|---|---|
| tight_ephemeral | 206 | **0** | 206 |
| enduring | 370 | **3** | 367 |

**AUC(enduring > tight_ephemeral):** n/a (insufficient coverage: a class has 0 matched species)

### Lifespan distribution (measured max longevity, yrs)
| class | n | median | IQR | min | max |
|---|---|---|---|---|---|
| tight_ephemeral | - | - | - | - | - |
| enduring | 3 | 177 | 111-2.62e+03 | 45 | 5.06e+03 |

Order-of-magnitude gap (log10 median enduring - ephemeral): **n/a**

### Sit-outs (listed, never dropped)
- tight_ephemeral: no_hownet_entry=123, not_organism_sense=77, species_unmatched=6
- enduring: no_hownet_entry=249, not_organism_sense=115, species_unmatched=3

## Severable classes SIT OUT (counted, no lifespan semantics)
- EN seasonal synsets: 805 ; EN bygone synsets: 765
- ZH tempo-only (severable, instantaneity): 592

_Full matched receipts + sit-out member lists: organ_lifespan_eval_55.json._
