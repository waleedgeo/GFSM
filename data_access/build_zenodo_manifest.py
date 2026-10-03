"""Validate the GFSM tile index against a Zenodo release and refresh app sizes.

Run from the repository root, optionally passing --record-json with a saved
response from https://zenodo.org/api/records/20568218 for offline use.
"""

import argparse
import csv
import hashlib
import json
import re
import sqlite3
from pathlib import Path
from urllib.parse import quote
from urllib.request import urlopen


RECORD_ID = "20568218"
START = "// BEGIN GENERATED ZENODO ARCHIVE MANIFEST"
END = "// END GENERATED ZENODO ARCHIVE MANIFEST"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record-json", type=Path, help="Saved Zenodo record API response")
    parser.add_argument("--index", type=Path, default=Path(".unpublished/GFSM_Tile_Index_v1.gpkg"))
    parser.add_argument("--index-zip", type=Path, default=Path(".unpublished/GFSM_Tile_Index.zip"))
    parser.add_argument("--app", type=Path, default=Path(".unpublished/gee_gfsm_app_codes.js"))
    parser.add_argument("--csv", type=Path, default=Path("data_access/zenodo_v2_archives.csv"))
    args = parser.parse_args()

    if args.record_json:
        record = json.loads(args.record_json.read_text(encoding="utf-8"))
    else:
        with urlopen(f"https://zenodo.org/api/records/{RECORD_ID}", timeout=30) as response:
            record = json.load(response)
    if str(record.get("id")) != RECORD_ID:
        raise ValueError("Zenodo response is for a different record")

    files = {item["key"]: item for item in record["files"]}
    if len(files) != len(record["files"]):
        raise ValueError("Zenodo response contains duplicate filenames")

    with sqlite3.connect(args.index) as connection:
        rows = connection.execute(
            "SELECT DISTINCT zip_filename FROM GFSM_Tile_Index_v1"
        ).fetchall()
    index_names = {row[0] for row in rows}
    if None in index_names or "" in index_names:
        raise ValueError("Tile index has a blank archive filename")

    archive_names = {
        name for name in files if re.fullmatch(r"GFSM_[NS]\d{2}[EW]\d{3}\.zip", name)
    }
    missing = sorted(index_names - archive_names)
    extra = sorted(archive_names - index_names)
    if missing or extra:
        raise ValueError(f"Index/record ZIP mismatch: missing={missing}, extra={extra}")

    index_file = files["GFSM_Tile_Index.zip"]
    if args.index_zip.exists():
        digest = hashlib.md5(args.index_zip.read_bytes()).hexdigest()
        if index_file["checksum"] != f"md5:{digest}":
            raise ValueError("Local index ZIP differs from the chosen Zenodo record")

    app = args.app.read_text(encoding="utf-8")
    if f"recordId: '{RECORD_ID}'" not in app:
        raise ValueError("App CONFIG does not match the Zenodo record ID")
    if app.count(START) != 1 or app.count(END) != 1:
        raise ValueError("App needs one pair of manifest markers")

    ordered = sorted(archive_names)
    manifest_lines = [START, "var ZENODO_ARCHIVE_BYTES = {"]
    for position, name in enumerate(ordered):
        suffix = "," if position < len(ordered) - 1 else ""
        manifest_lines.append(f"  '{name}': {files[name]['size']}{suffix}")
    manifest_lines.extend(["};", END])
    replacement = "\n".join(manifest_lines)
    app = re.sub(re.escape(START) + r".*?" + re.escape(END), replacement, app, flags=re.S)

    args.csv.parent.mkdir(parents=True, exist_ok=True)
    with args.csv.open("w", newline="", encoding="utf-8") as output:
        writer = csv.writer(output)
        writer.writerow(["record_id", "filename", "size_bytes", "checksum", "download_url"])
        for name in ordered:
            writer.writerow([
                RECORD_ID,
                name,
                files[name]["size"],
                files[name]["checksum"],
                f"https://zenodo.org/records/{RECORD_ID}/files/{quote(name)}?download=1",
            ])
    args.app.write_text(app, encoding="utf-8", newline="\n")
    print(f"Validated {len(ordered)} regional ZIPs; updated {args.csv} and {args.app}")


if __name__ == "__main__":
    main()
