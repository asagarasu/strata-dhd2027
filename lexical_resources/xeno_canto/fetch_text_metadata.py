#!/usr/bin/env python3
"""Fetch text-bearing xeno-canto metadata without downloading audio."""

from __future__ import annotations

import argparse
import csv
import datetime as dt
import json
import os
from pathlib import Path
import sys
import time
from typing import Any, Iterable
import urllib.error
import urllib.parse
import urllib.request


ENDPOINT = "https://xeno-canto.org/api/3/recordings"
USER_AGENT = "garden-dhd2027-xeno-text/1.0 (metadata-only research client)"
TEXT_COLUMNS = (
    "xc_id",
    "source_field",
    "text",
    "recordist",
    "scientific_name",
    "common_name",
    "group",
    "country",
    "location",
    "stable_url",
    "license",
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Fetch xeno-canto API v3 metadata and emit only text-bearing records; "
            "audio and spectrogram files are never requested."
        )
    )
    parser.add_argument("--query", default="cnt:china", help="API v3 tagged query")
    parser.add_argument("--output-dir", type=Path, default=Path("data"))
    parser.add_argument(
        "--key-file",
        type=Path,
        help="read the API key from a local file instead of XC_API_KEY",
    )
    parser.add_argument(
        "--per-page", type=int, default=500, help="API page size, from 50 to 500"
    )
    parser.add_argument(
        "--delay", type=float, default=1.0, help="seconds between page requests"
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        help="stop after this many pages (useful for a small validation pull)",
    )
    parser.add_argument(
        "--force", action="store_true", help="replace this script's existing outputs"
    )
    return parser.parse_args()


def api_url(query: str, key: str, per_page: int, page: int) -> str:
    params = urllib.parse.urlencode(
        {"query": query, "key": key, "per_page": per_page, "page": page}
    )
    return f"{ENDPOINT}?{params}"


def fetch_page(url: str, retries: int = 4) -> dict[str, Any]:
    request = urllib.request.Request(
        url, headers={"Accept": "application/json", "User-Agent": USER_AGENT}
    )
    for attempt in range(retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return json.load(response)
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", "replace")
            if exc.code not in {429, 500, 502, 503, 504} or attempt == retries:
                raise RuntimeError(f"xeno-canto API HTTP {exc.code}: {body}") from exc
            retry_after = exc.headers.get("Retry-After")
            wait = float(retry_after) if retry_after else 2**attempt
        except (urllib.error.URLError, TimeoutError) as exc:
            if attempt == retries:
                raise RuntimeError(f"xeno-canto API request failed: {exc}") from exc
            wait = 2**attempt
        print(f"temporary request failure; retrying in {wait:g}s", file=sys.stderr)
        time.sleep(wait)
    raise AssertionError("unreachable")


def text(value: Any) -> str:
    return value if isinstance(value, str) else ""


def scientific_name(record: dict[str, Any]) -> str:
    return " ".join(
        part for part in (text(record.get("gen")), text(record.get("sp")), text(record.get("ssp"))) if part
    )


def stable_url(record: dict[str, Any]) -> str:
    value = text(record.get("url"))
    if value.startswith("//"):
        return "https:" + value
    if value:
        return value
    xc_id = text(record.get("id"))
    return f"https://xeno-canto.org/{xc_id}" if xc_id else ""


def slim_record(record: dict[str, Any]) -> dict[str, Any]:
    annotation_set = record.get("annotation-set")
    annotations = []
    set_metadata: dict[str, Any] = {}
    if isinstance(annotation_set, dict):
        set_metadata = {
            key: annotation_set.get(key)
            for key in (
                "set_name",
                "set_creator",
                "set_creation_date",
                "set_remarks",
            )
            if annotation_set.get(key) not in (None, "")
        }
        for annotation in annotation_set.get("annotations") or []:
            if not isinstance(annotation, dict):
                continue
            annotations.append(
                {
                    key: annotation.get(key)
                    for key in (
                        "annotation_xc_id",
                        "annotator",
                        "sound_type",
                        "sex",
                        "life_stage",
                        "annotation_remarks",
                    )
                    if annotation.get(key) not in (None, "")
                }
            )

    result = {
        "xc_id": text(record.get("id")),
        "scientific_name": scientific_name(record),
        "common_name": text(record.get("en")),
        "group": text(record.get("grp")),
        "recordist": text(record.get("rec")),
        "country": text(record.get("cnt")),
        "location": text(record.get("loc")),
        "sound_type": record.get("type"),
        "sex": record.get("sex"),
        "life_stage": record.get("stage"),
        "date": record.get("date"),
        "time": record.get("time"),
        "remarks": record.get("rmk"),
        "background_species": record.get("also") or [],
        "animal_seen": record.get("animal-seen"),
        "playback_used": record.get("playback-used"),
        "stable_url": stable_url(record),
        "license": text(record.get("lic")),
    }
    if set_metadata or annotations:
        result["annotation_set"] = {**set_metadata, "annotations": annotations}
    return result


def one_line(value: Any) -> str:
    if isinstance(value, list):
        value = "; ".join(str(item) for item in value if item not in (None, ""))
    if not isinstance(value, str):
        return ""
    return " ".join(value.split())


def text_units(record: dict[str, Any]) -> Iterable[dict[str, str]]:
    common = {
        "xc_id": text(record.get("id")),
        "recordist": text(record.get("rec")),
        "scientific_name": scientific_name(record),
        "common_name": text(record.get("en")),
        "group": text(record.get("grp")),
        "country": text(record.get("cnt")),
        "location": text(record.get("loc")),
        "stable_url": stable_url(record),
        "license": text(record.get("lic")),
    }
    for field, value in (("type", record.get("type")), ("rmk", record.get("rmk"))):
        value = one_line(value)
        if value:
            yield {**common, "source_field": field, "text": value}

    annotation_set = record.get("annotation-set")
    if isinstance(annotation_set, dict):
        set_remarks = one_line(annotation_set.get("set_remarks"))
        if set_remarks:
            yield {**common, "source_field": "annotation_set_remarks", "text": set_remarks}
        for annotation in annotation_set.get("annotations") or []:
            if not isinstance(annotation, dict):
                continue
            for field in ("sound_type", "annotation_remarks"):
                value = one_line(annotation.get(field))
                if value:
                    yield {
                        **common,
                        "source_field": (
                            "annotation_remarks"
                            if field == "annotation_remarks"
                            else "annotation_sound_type"
                        ),
                        "text": value,
                    }


def main() -> int:
    args = parse_args()
    key = os.environ.get("XC_API_KEY")
    if args.key_file:
        try:
            key = args.key_file.read_text(encoding="utf-8").strip()
        except OSError as exc:
            print(f"could not read --key-file: {exc}", file=sys.stderr)
            return 2
    if not key:
        print(
            "No API key found. Retrieve yours from https://xeno-canto.org/account, "
            "then set XC_API_KEY or pass --key-file.",
            file=sys.stderr,
        )
        return 2
    if args.delay < 0:
        print("--delay must be non-negative", file=sys.stderr)
        return 2
    if not 50 <= args.per_page <= 500:
        print("--per-page must be between 50 and 500", file=sys.stderr)
        return 2
    if args.max_pages is not None and args.max_pages < 1:
        print("--max-pages must be positive", file=sys.stderr)
        return 2

    args.output_dir.mkdir(parents=True, exist_ok=True)
    records_path = args.output_dir / "records.jsonl"
    units_path = args.output_dir / "text_units.tsv"
    provenance_path = args.output_dir / "provenance.json"
    outputs = (records_path, units_path, provenance_path)
    existing = [path for path in outputs if path.exists()]
    if existing and not args.force:
        print(
            "refusing to replace existing output(s): "
            + ", ".join(str(path) for path in existing)
            + " (pass --force to replace them)",
            file=sys.stderr,
        )
        return 2

    records_tmp = records_path.with_suffix(records_path.suffix + ".partial")
    units_tmp = units_path.with_suffix(units_path.suffix + ".partial")
    for path in (records_tmp, units_tmp):
        if path.exists():
            print(f"remove or move incomplete prior output first: {path}", file=sys.stderr)
            return 2

    started = dt.datetime.now(dt.timezone.utc)
    pages_fetched = 0
    records_written = 0
    units_written = 0
    reported_recordings: int | None = None
    reported_pages: int | None = None

    try:
        with records_tmp.open("x", encoding="utf-8") as records_file, units_tmp.open(
            "x", encoding="utf-8", newline=""
        ) as units_file:
            writer = csv.DictWriter(units_file, fieldnames=TEXT_COLUMNS, delimiter="\t")
            writer.writeheader()
            page = 1
            while True:
                payload = fetch_page(api_url(args.query, key, args.per_page, page))
                if "error" in payload:
                    raise RuntimeError(f"xeno-canto API error: {payload['error']}")
                if reported_recordings is None:
                    reported_recordings = int(payload.get("numRecordings", 0))
                    reported_pages = int(payload.get("numPages", 1))
                    print(
                        f"API reports {reported_recordings} recordings across "
                        f"{reported_pages} page(s)",
                        file=sys.stderr,
                    )
                recordings = payload.get("recordings") or []
                for record in recordings:
                    if not isinstance(record, dict):
                        continue
                    json.dump(slim_record(record), records_file, ensure_ascii=False)
                    records_file.write("\n")
                    records_written += 1
                    for unit in text_units(record):
                        writer.writerow(unit)
                        units_written += 1
                pages_fetched += 1
                print(
                    f"page {page}/{reported_pages}: {len(recordings)} records",
                    file=sys.stderr,
                )
                if page >= (reported_pages or 1):
                    break
                if args.max_pages is not None and pages_fetched >= args.max_pages:
                    break
                page += 1
                if args.delay:
                    time.sleep(args.delay)
        os.replace(records_tmp, records_path)
        os.replace(units_tmp, units_path)
    except Exception as exc:
        print(f"fetch failed; partial files were retained: {exc}", file=sys.stderr)
        return 1

    finished = dt.datetime.now(dt.timezone.utc)
    provenance = {
        "source": "xeno-canto API v3",
        "endpoint": ENDPOINT,
        "query": args.query,
        "retrieved_at_utc": finished.isoformat(),
        "elapsed_seconds": (finished - started).total_seconds(),
        "per_page": args.per_page,
        "pages_fetched": pages_fetched,
        "complete_query_result": reported_pages == pages_fetched,
        "api_reported_recordings": reported_recordings,
        "records_written": records_written,
        "text_units_written": units_written,
        "audio_downloaded": False,
        "notes": (
            "Metadata only. Keep XC ID, stable URL, recordist, and license with quoted "
            "material. The saved xeno-canto terms explicitly license recordings, but do "
            "not clearly state that recordist remarks inherit the recording license."
        ),
    }
    provenance_path.write_text(
        json.dumps(provenance, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(
        f"wrote {records_written} records and {units_written} text units to "
        f"{args.output_dir}",
        file=sys.stderr,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
