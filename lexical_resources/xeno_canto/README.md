# xeno-canto text metadata

This fetcher retrieves metadata from xeno-canto API v3 for the tagged query
`cnt:china`. It never requests the `file` or sonogram URLs and therefore downloads
no audio or images.

## Local corpus status

Complete metadata-only pull finished 2026-07-17:

- 24,020 unique recordings across all 49 API pages
- 32,491 text units: 23,790 `type`, 8,699 `rmk`, and 2 annotation-set remarks
- 0 text rows missing recordist, XC ID, stable URL, or license
- approximately 13 MiB JSONL + 7 MiB TSV
- checksums in `CHECKSUMS.sha256`; API counts and timestamp in
  `data/provenance.json`

## Setup and validation pull

Register or log in at <https://xeno-canto.org/account>, verify the account email,
and retrieve the API key. Keep it out of files and Git:

```sh
export XC_API_KEY='paste-key-here'
cd <LAB>/lexical_resources/xeno_canto
python3 fetch_text_metadata.py --max-pages 1 --output-dir validation
```

To let Codex perform the pull without putting the key in chat or shell history,
save the key as a single line in `.xc-api-key` (this filename is ignored by Git),
then say that it is ready. Codex can run:

```sh
python3 fetch_text_metadata.py --key-file .xc-api-key --max-pages 1 --output-dir validation
```

Inspect `validation/provenance.json`, `validation/records.jsonl`, and
`validation/text_units.tsv`. For the complete query, use a new output directory:

```sh
python3 fetch_text_metadata.py --output-dir data
```

If using the file method, add `--key-file .xc-api-key` to that command as well.

The default page size is 500 (the documented v3 maximum) with a one-second delay
between pages. `--query` accepts a different precise, tagged v3 query if the
research scope changes.

## Outputs

- `records.jsonl`: one slim metadata record per XC recording. It retains the
  fields needed to interpret and cite text, but omits audio/download and image
  URLs.
- `text_units.tsv`: one analysis-ready row for each nonempty `type`, `rmk`,
  annotation sound type, or annotation remark. Newlines inside authored text are
  normalized to spaces for TSV safety; the JSONL retains the API value.
- `provenance.json`: query, retrieval time, counts, and whether the query was
  fetched completely.

## Rights and citation caution

The locally saved terms require acknowledgement and say to retain the recordist,
XC catalogue number, and stable URL when citing recordings. They also discourage
indiscriminate automated requests. This client uses the API, precise queries, large
pages, and a delay.

The terms clearly discuss Creative Commons licenses for the **sound recordings**.
They do not clearly say that recordist-authored `rmk` text or annotation remarks
inherit the sound's license. Treat the extracted text as a local research corpus;
preserve the provenance columns, quote sparingly, and do not redistribute the
remarks corpus without clarifying its status with xeno-canto.

Saved source documentation is in `../html/API_xeno-canto.stripped.txt` and
`../html/Terms of Use_xeno-canto.stripped.txt`.
