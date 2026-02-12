# Chest X-ray Dataset Setup (Module 5)

Module 5 uses a real clinical image dataset with a small, CPU-friendly subset.

## Recommended dataset
- Name: Chest X-Ray Images (Pneumonia)
- Original source: Kermany et al. pediatric CXR dataset
- Google Drive link provided for this course:
  - https://drive.google.com/file/d/1tJtH-BHsqncTnh9bJovB6ap-IZc-tVW3/view?usp=sharing

## One-step setup (no Kaggle API)
From repo root:

```bash
python scripts/setup_chest_xray_from_gdrive.py
```

If the folder already exists and you want to replace it:

```bash
python scripts/setup_chest_xray_from_gdrive.py --force
```

If automatic download is blocked by network policy, manually download the zip
from the Drive link and place it at `data/chest_xray_small.zip`, then rerun the
setup command above.

## Expected folder structure
Place the extracted dataset under `data/chest_xray_small/`:

```
data/chest_xray_small/
  train/
    NORMAL/
    PNEUMONIA/
  val/
    NORMAL/
    PNEUMONIA/
  test/
    NORMAL/
    PNEUMONIA/
```

## Suggested small subset target (for laptops)
- train: up to 600 images per class
- val: up to 150 images per class
- test: up to 150 images per class

The Module 5 notebooks automatically downsample to this subset if more files are present.

## Notes
- Keep original labels (`NORMAL`, `PNEUMONIA`) for the binary baseline.
- This is an educational workflow, not a clinical-grade model.
- The setup script expects an archive that contains `train/`, `val/`, and `test/`
  folders with `NORMAL/` and `PNEUMONIA/` subfolders.
