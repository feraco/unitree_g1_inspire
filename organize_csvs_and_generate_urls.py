from __future__ import annotations

import csv
import shutil
from pathlib import Path
from urllib.parse import quote

REPO_OWNER = "feraco"
REPO_NAME = "motiondata"
BRANCH = "main"
RAW_BASE = f"https://raw.githubusercontent.com/{REPO_OWNER}/{REPO_NAME}/{BRANCH}"

ROOT = Path(".")
MAPPING_FILE = ROOT / "movement_categories.csv"
URL_LIST_FILE = ROOT / "raw_csv_urls.txt"


def slugify_category(name: str) -> str:
    return (
        name.strip()
        .lower()
        .replace("&", "and")
        .replace("/", "_")
        .replace(" ", "_")
        .replace("-", "_")
    )


def read_mapping(path: Path) -> dict[str, str]:
    mapping: dict[str, str] = {}
    if not path.exists():
        return mapping

    with path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            file_name = (row.get("file") or "").strip()
            category = (row.get("category") or "Uncategorized").strip()
            if file_name:
                mapping[file_name] = category or "Uncategorized"
    return mapping


def main() -> None:
    mapping = read_mapping(MAPPING_FILE)

    csv_files = sorted(
        p
        for p in ROOT.glob("*.csv")
        if p.name not in {"raw_csv_urls.txt"}
    )

    moved_count = 0
    uncategorized_count = 0

    for csv_file in csv_files:
        if csv_file.name == "movement_categories.csv":
            target_dir = ROOT / "metadata"
        else:
            category = mapping.get(csv_file.name, "Uncategorized")
            if category == "Uncategorized":
                uncategorized_count += 1
            target_dir = ROOT / slugify_category(category)

        target_dir.mkdir(parents=True, exist_ok=True)
        target_path = target_dir / csv_file.name
        if target_path.exists():
            target_path.unlink()
        shutil.move(str(csv_file), str(target_path))
        moved_count += 1

    all_csvs = sorted(
        p for p in ROOT.rglob("*.csv") if ".git" not in p.parts
    )

    with URL_LIST_FILE.open("w", encoding="utf-8", newline="") as file:
        for path in all_csvs:
            rel = path.as_posix().lstrip("./")
            encoded_rel = quote(rel, safe="/")
            file.write(f"{RAW_BASE}/{encoded_rel}\n")

    print(f"moved_csv_files={moved_count}")
    print(f"total_csv_files_now={len(all_csvs)}")
    print(f"uncategorized_assigned={uncategorized_count}")
    print(f"url_list={URL_LIST_FILE}")


if __name__ == "__main__":
    main()
