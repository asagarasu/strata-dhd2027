# COCO-CN Provenance

## Dataset Identity

- **Name**: COCO-CN (version 201805 v1.1)
- **Authors**: Xirong Li, Chaoxi Xu, Xiaoxu Wang, Weiyu Lan, Zhengxiong Jia, Gang Yang, Jieping Xu (Renmin University of China)
- **Paper**: "COCO-CN for Cross-Lingual Image Tagging, Captioning and Retrieval", IEEE Transactions on Multimedia, 2019
- **Official GitHub**: https://github.com/li-xirong/coco-cn
- **HuggingFace**: https://huggingface.co/datasets/AIMClab/COCO-CN

## Retrieval Date

2026-07-20

## Files Downloaded

### 1. `coco-cn-version1805v1.1.tar.gz`
- **Source URL**: https://huggingface.co/datasets/AIMClab/COCO-CN/resolve/main/coco-cn-version1805v1.1.tar.gz
- **Served via**: HuggingFace CDN (us.aws.cdn.hf.co), public ungated access
- **Size**: 15.4 MB (compressed); ~89 MB expanded
- **SHA-256**: `6c126cd8455363a404806e452ec75066a8fc96d73922d9357d993fcdd1d40b8a`
- **Contents** (extracted to `coco-cn-version1805v1.1/`):
  - `coco-cn_train.txt` — 18,341 image IDs (training split)
  - `coco-cn_val.txt` — 999 image IDs (validation split)
  - `coco-cn_test.txt` — 1,000 image IDs (test split)
  - `imageid.human-written-caption.txt` — 22,218 manually written Chinese captions (image_id#n TAB sentence)
  - `imageid.human-written-caption.bosonseg.txt` — same, word-segmented
  - `imageid.human-written-tags.txt` — 20,341 rows of human-assigned Chinese tags (space-separated)
  - `imageid.manually-translated-caption.txt` — 5,000 manually translated captions (test only)
  - `imageid.manually-translated-caption.bosonseg.txt` — same, word-segmented
  - `imageid.machine-translated-caption.bosonseg.txt` — Baidu machine translations, all splits
  - `verify_data.py` — integrity-check script

### 2. `conceptscn655.txt`
- **Source URL**: https://raw.githubusercontent.com/li-xirong/coco-cn/master/data/conceptscn655.txt
- **Size**: 4.7 KB, 655 lines
- **Contents**: Chinese tag vocabulary (655 tags for cross-lingual image tagging)
- **SHA-256**: `e25044d77bd9c97d1907a2ceff45b15566fc9064d493d9ba9860b07c3a114073`

### 3. `coco-cn_ext.icap2020.txt`
- **Source URL**: https://raw.githubusercontent.com/li-xirong/coco-cn/master/data/coco-cn_ext.icap2020.txt
- **Size**: 369 KB, 4,712 lines
- **Contents**: Extension from 2021-02-03 iCap system — 4,573 additional images with 4,712 manually written Chinese sentences (image_id#n TAB sentence)
- **SHA-256**: `6427c1b2f2bc357f26ac7ac37e60965f7574028997dc7aefcad495832359053c`

### 4. `detected-typos.txt`
- **Source URL**: https://raw.githubusercontent.com/li-xirong/coco-cn/master/data/detected-typos.txt
- **Size**: 3.5 KB, 56 lines
- **Contents**: Known typos in the dataset, curated by Xinru Chen
- **SHA-256**: `1d8f1d87f577afaf7227add4ab42296a3ab26789f001e6c22537c2d8aecf7626`

## License (verbatim)

MIT License

Copyright (c) 2018

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Source: https://raw.githubusercontent.com/li-xirong/coco-cn/master/LICENSE

## Access Status

All annotation files were **directly downloadable** without a request gate as of 2026-07-20. HuggingFace dataset page (https://huggingface.co/datasets/AIMClab/COCO-CN) announced public availability 2025-02-12. No request form or email required.

The **precomputed ResNext-101 visual features** (145 MB, `coco-cn_resnext-101_feat.tar.gz`) are hosted at `http://lixirong.net/data/coco-cn/coco-cn_resnext-101_feat.tar.gz` — not downloaded here as they are visual features, not text/caption data, and not needed for the lexical-resource use case.

## Payload Note

Binary blobs (`coco-cn-version1805v1.1.tar.gz` and its expanded contents) stay untracked per the house payload law. Checksums travel in `CHECKSUMS.sha256`.
