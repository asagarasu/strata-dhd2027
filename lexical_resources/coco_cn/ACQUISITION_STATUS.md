# COCO-CN Acquisition Status

**Status: COMPLETE — all annotation data directly downloadable; no request gate encountered.**

## What Was Acquired (2026-07-20)

All annotation files are publicly available without a request form or email contact.

| File | Type | Status |
|------|------|--------|
| `coco-cn-version1805v1.1.tar.gz` | Main archive (captions, tags, splits) | Downloaded |
| `conceptscn655.txt` | 655-tag Chinese vocabulary | Downloaded |
| `coco-cn_ext.icap2020.txt` | 2021 iCap extension (4,712 sentences) | Downloaded |
| `detected-typos.txt` | Quality-control list | Downloaded |

## What Was NOT Acquired (deliberate)

| Resource | Reason |
|----------|--------|
| `coco-cn_resnext-101_feat.tar.gz` (145 MB) | Visual features, not text; not needed for lexical-resource use |
| MS-COCO source images | Not redistributed by COCO-CN; use local COCO val2017 pixels |

## Dataset Structure

- **COCO-CN image sources**: MS-COCO **train2014** and **val2014** splits (NOT val2017)
  - 13,593 images from train2014
  - 6,749 images from val2014
  - 20,342 total unique images
- **COCO-CN annotation splits**:
  - Train: 18,341 images, 22,218 human-written Chinese sentences
  - Val: 999 images
  - Test: 1,000 images
  - Extension (iCap 2021): 4,573 images, 4,712 manually written sentences
- **Sentences**: ~27,000 human-written Chinese captions total (22,218 main + 4,712 ext)
- **Tags**: 20,341 images have human-assigned Chinese tags; vocabulary of 655 tags

## Intersection with Local val2017 Pixels

Local pixels: `<LAB>/caesitas_proto/data/coco/val2017/`
- Local val2017 images: 5,000 files

COCO-CN draws from val2014 (6,749 images). COCO val2017 is a subset of val2014, so there is overlap:
- **823 COCO-CN images have local pixels in val2017** (intersection of val2014 COCO-CN IDs with local val2017 IDs)
- These 823 images carry human-written Chinese captions and/or tags in COCO-CN
- The train2014-sourced COCO-CN images (13,593) have zero intersection with local val2017

The 823-image intersection ID list is saved in `intersection_coco_cn_x_local_val2017.txt`.

For the ext (iCap 2020) extension, 184 of its 4,573 images are also in local val2017.

## Historical Note on Access

Prior to 2025-02-12, parts of this dataset were distributed via a request mechanism through the RUC lab. The HuggingFace public release (AIMClab/COCO-CN) made all annotation data freely available. If for any reason that distribution is unavailable, the original contact point was the Renmin University of China lab of Xirong Li (li-xirong on GitHub).
