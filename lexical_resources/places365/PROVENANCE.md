# Places365 — provenance (SCENE-LUMINANCE witness input)

Retrieved 2026-07-21 for the SCENE-LUMINANCE witness
(`caesitas_proto/results/scene_luminance_witness_PROPOSED_54.*`). This resource
is a WORLD-FACT input to a **TRIGGER-only** witness: it may nominate candidate
latent-referent-darkness words; it may **never** grade them (two-truths ruling:
world-facts trigger, published impressions grade).

Dataset: **Places365** (Places365-Standard validation split, 256x256).
Citation: Zhou, B., Lapedriza, A., Khosla, A., Oliva, A., Torralba, A. (2017).
"Places: A 10 million Image Database for Scene Recognition." *IEEE Transactions
on Pattern Analysis and Machine Intelligence*.
Project page: http://places2.csail.mit.edu
Code/repo: https://github.com/CSAILVision/places365

## Artifacts downloaded

Source host `data.csail.mit.edu` served the images. The plain-`http://`
`places2.csail.mit.edu`/`data.csail.mit.edu` URLs 301-redirect to `https://`;
final resolved URLs recorded below. All endpoints advertised `Accept-Ranges:
bytes` (resumable).

### 1. Validation images (256x256) — the SMALLEST SUFFICIENT image artifact

- **File:** `val_256.tar`
- **URL (resolved):** https://data.csail.mit.edu/places/places365/val_256.tar
- **Content-Length (HTTP HEAD, and bytes-on-disk):** 525158400 bytes (~500.8 MiB)
- **Content-Type:** application/x-tar
- **sha256:** `24b4e639ef12a0012af525bc4cb443e4ab4aaea8369a1fb009b70e4a4aad5d48`
- **Contents:** 36500 JPEGs, flat layout `val_256/Places365_val_00000001.jpg` …
  `val_256/Places365_val_00036500.jpg` (36501 tar entries = 1 dir + 36500 images).
- **Sizing note (HEAD-before-download, per instruction):** the brief cited
  "`val_256.tar`, ~2GB". The actual `Content-Length` of `val_256.tar` is ~500 MB;
  the ~2 GB (2270320640 bytes) artifact is `val_large.tar` (the high-resolution
  val split). `val_256.tar` (256x256) is the smaller and sufficient artifact for
  a full-image mean-luminance statistic, so it was chosen. No smaller official
  val split exists (val_256 is already the down-sized val set).

### 2. Filelists devkit (holds the category list + val ground-truth labels)

- **File:** `filelist_places365-standard.tar`
- **URL (resolved):** https://data.csail.mit.edu/places/places365/filelist_places365-standard.tar
- **Content-Length / bytes-on-disk:** 67498496 bytes (~64.4 MiB)
- **sha256:** `520699e00d69b63ddc29fac54645aa00ce1c10ca42e288960aa1cf791d6e9aa9`
- **Contents:** `categories_places365.txt`, `places365_train_standard.txt`,
  `places365_val.txt`, `places365_test.txt`.
- The top-level `.../places365/categories_places365.txt` and
  `.../places365/places365_val.txt` URLs return HTTP 404; the authoritative
  copies are inside this devkit tar. Extracted the two needed files:

  - **`categories_places365.txt`** — 365 lines (`/x/label idx`, idx 0..364).
    sha256: `2affba635eb657e7ca95f4e6cc69bd9fac29ef4c32aeb83cafdfcd06ec6a1ea6`
  - **`places365_val.txt`** — 36500 lines (`Places365_val_NNNNNNNN.jpg idx`).
    sha256: `06d41c7ca5164a789a3dae2e997d8dd1ad2aef8d97ee474d4717a4dcce0a67be`
    Verified: 365 distinct category indices, exactly 100 images per category.

## License / terms (QUOTED VERBATIM)

Two authoritative sources were reachable and are quoted here in full; the legacy
download page is now a v2-transition stub (quoted last).

**(a) Repository `LICENSE`** — https://github.com/CSAILVision/places365/blob/master/LICENSE
(covers the software/code):

> MIT License
>
> Copyright (c) 2017 Bolei Zhou and MIT CSAIL Computer Vision
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.

**(b) `README.md`, section "Acknowledgements and License"** —
https://github.com/CSAILVision/places365 (covers the models and the images):

> The pretrained places-CNN models can be used under the Creative Common License
> (Attribution CC BY). Please give appropriate credit, such as providing a link
> to our paper or to the [Places Project Page](http://places2.csail.mit.edu). The
> copyright of all the images belongs to the image owners.

**(c) Legacy download page** — http://places2.csail.mit.edu/download.html
(as retrieved 2026-07-21, now a v2-transition notice gating legacy access to
research use):

> We are actively working on the version 2 of Places Database. If you need to use
> the legacy dataset (the original Places365 or Places205) urgently for research
> purposes, please sign this form, thank you.

**Reading (not a term; the field owner's to confirm):** Places365 is released for
research/educational use. The repository `LICENSE` (MIT) governs the code; the
`README` places the pretrained models under CC BY and states plainly that **the
copyright of all the images belongs to the image owners** — i.e. the image files
are third-party-owned content distributed by CSAIL for research, not re-licensed
by CSAIL. Use here is non-commercial academic research (a per-image mean-luminance
aggregate; no image is redistributed). Only the official CSAIL mirror was used; no
images were scraped from any other source.
