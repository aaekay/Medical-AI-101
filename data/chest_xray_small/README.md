# Chest X-ray Dataset Setup (Module 5)

Module 5 uses a real clinical image dataset with a small, CPU-friendly subset.

## Recommended dataset
- Name: Chest X-Ray Images (Pneumonia)
- Original source: Kermany et al. pediatric CXR dataset
- Common mirrors: Kaggle / Mendeley

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
