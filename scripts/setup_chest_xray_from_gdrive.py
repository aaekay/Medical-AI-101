#!/usr/bin/env python3
"""
One-step setup for the Module 5 chest X-ray dataset from Google Drive.

This script downloads the archive, extracts it, detects the folder that
contains train/val/test with NORMAL and PNEUMONIA subfolders, and copies
those folders into data/chest_xray_small/.
"""

from __future__ import annotations

import argparse
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path


FILE_ID = "1tJtH-BHsqncTnh9bJovB6ap-IZc-tVW3"
SHARE_URL = "https://drive.google.com/file/d/1tJtH-BHsqncTnh9bJovB6ap-IZc-tVW3/view?usp=sharing"
REQUIRED_SPLITS = ("train", "val", "test")
REQUIRED_LABELS = ("NORMAL", "PNEUMONIA")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download and prepare chest X-ray dataset for Module 5.")
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("data/chest_xray_small"),
        help="Output dataset directory (default: data/chest_xray_small).",
    )
    parser.add_argument(
        "--zip-path",
        type=Path,
        default=Path("data/chest_xray_small.zip"),
        help="Path to store downloaded zip (default: data/chest_xray_small.zip).",
    )
    parser.add_argument(
        "--file-id",
        type=str,
        default=FILE_ID,
        help="Google Drive file ID.",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing train/val/test folders in output-dir.",
    )
    return parser.parse_args()


def ensure_parent(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)


def download_zip(file_id: str, zip_path: Path) -> None:
    ensure_parent(zip_path)
    try:
        import gdown
    except ImportError:
        print("gdown is required for automatic download.")
        print("Install with: pip install gdown")
        print(f"Or manually download from: {SHARE_URL}")
        raise SystemExit(1)

    url = f"https://drive.google.com/uc?id={file_id}"
    print(f"Downloading archive from Google Drive file id: {file_id}")
    out = gdown.download(url=url, output=str(zip_path), quiet=False, fuzzy=True)
    if out is None or not zip_path.exists():
        print("Download failed. Please verify Drive link permissions.")
        raise SystemExit(1)


def is_dataset_root(path: Path) -> bool:
    if not path.is_dir():
        return False
    for split in REQUIRED_SPLITS:
        split_dir = path / split
        if not split_dir.is_dir():
            return False
        for label in REQUIRED_LABELS:
            if not (split_dir / label).is_dir():
                return False
    return True


def find_dataset_root(extract_root: Path) -> Path | None:
    if is_dataset_root(extract_root):
        return extract_root

    candidates = [p for p in extract_root.rglob("*") if p.is_dir()]
    for p in candidates:
        if is_dataset_root(p):
            return p
    return None


def count_images(folder: Path) -> int:
    valid = {".jpg", ".jpeg", ".png"}
    return sum(1 for p in folder.rglob("*") if p.suffix.lower() in valid and p.is_file())


def copy_dataset(src_root: Path, output_dir: Path, force: bool = False) -> None:
    output_dir.mkdir(parents=True, exist_ok=True)

    if not force:
        for split in REQUIRED_SPLITS:
            if (output_dir / split).exists():
                print(
                    f"{output_dir / split} already exists. "
                    "Use --force to overwrite existing split folders."
                )
                raise SystemExit(1)
    else:
        for split in REQUIRED_SPLITS:
            split_dir = output_dir / split
            if split_dir.exists():
                shutil.rmtree(split_dir)

    for split in REQUIRED_SPLITS:
        for label in REQUIRED_LABELS:
            src = src_root / split / label
            dst = output_dir / split / label
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copytree(src, dst, dirs_exist_ok=False)


def print_summary(output_dir: Path) -> None:
    print("\nDataset prepared at:", output_dir)
    total = 0
    for split in REQUIRED_SPLITS:
        for label in REQUIRED_LABELS:
            folder = output_dir / split / label
            n = count_images(folder)
            total += n
            print(f"  {split:>5} / {label:<9}: {n}")
    print(f"  {'TOTAL':>5} / {'ALL':<9}: {total}")


def main() -> None:
    args = parse_args()

    if not args.zip_path.exists():
        download_zip(args.file_id, args.zip_path)
    else:
        print(f"Using existing zip: {args.zip_path}")

    with tempfile.TemporaryDirectory(prefix="cxr_extract_") as tmpdir:
        tmp_root = Path(tmpdir)
        print(f"Extracting archive to temporary dir: {tmp_root}")
        with zipfile.ZipFile(args.zip_path, "r") as zf:
            zf.extractall(tmp_root)

        dataset_root = find_dataset_root(tmp_root)
        if dataset_root is None:
            print("Could not find expected dataset structure after extraction.")
            print("Expected: train/val/test each containing NORMAL and PNEUMONIA.")
            print("Drive link:", SHARE_URL)
            raise SystemExit(1)

        print(f"Detected dataset root: {dataset_root}")
        copy_dataset(dataset_root, args.output_dir, force=args.force)
        print_summary(args.output_dir)

    print("\nSetup complete. You can now run Module 5 notebooks.")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nInterrupted.")
        sys.exit(1)
