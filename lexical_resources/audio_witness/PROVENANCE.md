# audio_witness — vendored 2026-07-17 (#49), on the PI's ruling
*Ruling (07-17, in session): "we have an abundance of them. Your plan
is sound and I agree" — AudioCaps×AudioSet as the sound-ruler probe
pool + Clotho×FSD50K's 582 shared clips as the clean held-out witness
set. Survey: caesitas_proto/audio_witness_survey.md (scout report +
chair intersection check). Checksums: CHECKSUMS.sha256 (17 files).*

## What's here, licenses, pulls
- **audiocaps/** — train/val/test.csv (57,188 caption rows; columns
  audiocap_id,youtube_id,start_time,caption) + LICENSE_upstream (MIT
  file — NOTE upstream README says "academic purposes only"; conflict
  unresolved at source, we operate under the stricter reading).
  Pull: raw.githubusercontent.com/cdjkim/audiocaps/master/dataset/.
- **clotho/** — captions + metadata CSVs, v2.1 (3 splits; 5 blind
  human captions/clip; metadata sound_id = Freesound ID) + LICENSE
  (Tampere non-commercial + attribution, captions-only). Pull:
  zenodo.org/records/4783391.
- **fsd50k/** — FSD50K.ground_truth.zip (dev 40,966 + eval 10,231
  fname→labels; vocabulary.csv). License: CC BY 4.0 (ground truth).
  Pull: zenodo.org/records/4060432. (metadata.zip with uploader text
  ~6.7MB NOT vendored — not in the ruled plan; pull on need.)
- **audioset/** — class_labels_indices.csv + balanced_train_segments
  .csv + eval_segments.csv + ontology.json (tracked) +
  **unbalanced_train_segments.csv 101,468,408 B (PAYLOAD — untracked,
  exceeds GitHub 100MB; checksum travels, re-pull below)**. Licenses:
  CC BY 4.0 (label CSVs) / CC BY-SA 4.0 (ontology). Pull:
  storage.googleapis.com/us_audioset/youtube_corpus/v1/csv/<name>.csv
  — **reachability from this machine VERIFIED 07-17** (the survey's
  open caveat; resolved). Ontology:
  raw.githubusercontent.com/audioset/ontology/master/ontology.json.

## Verified on THESE copies (not inherited from the survey)
- AudioCaps→AudioSet join: **51,308/51,308 (100.00%)** on
  (youtube_id, start_time) vs (YTID, start_seconds), all three
  segment files pooled (2,084,320 segments).
- Clotho×FSD50K intersection: **582 shared Freesound IDs** (chair
  check 07-17, method in audio_witness_survey.md §FOLLOW-UP).
- Row counts match the scout's independent measurements exactly
  (22,160 / 20,371 / 2,041,789 segments + headers).

## Standing constraints
Captions are probe MATERIAL under the derivation laws: word-lists
select, humans wrote the text, labels witness — no team authorship
anywhere in the chain. AudioCaps captions are hint-primed (annotators
saw AudioSet tags) — disclosed; Clotho captions are blind — reserve
the 582-clip Clotho×FSD50K set as held-out witness, do not spend it
in construction. Machine-caption corpora (WavCaps class) BARRED.
