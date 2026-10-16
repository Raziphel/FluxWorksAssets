# FluxWorks Assets development checks

This branch includes **four newly authored machine-upgrade PNG badges**, plus all original Flux icons and graphics. The offline validator checks the existing six named assets and four upgrade badges, and verifies editable SVG masters.

```sh
python3 scripts/validate_extension_assets.py
```

The checker validates `docs/ASSET_CONTRACT.json`, confirms each expected path is safely relative, checks each file exists, verifies the PNG signature, IHDR dimensions and sane bounds, and detects duplicate palette IDs/paths. It is dependency-free, deterministic, and read-only.

## Limitations

Passing does **not** mean the mod fully loads. Runtime sprite compatibility (tile dimensions, sprite sheet slicing, texture decompression, scale, shift, mipmap and animation frame declarations), usability at 32 px, art quality and consistency require a full Factorio 2.1 load with Razi Protocol and FluxWorks, followed by manual visual inspection. Asset location and technology compatibility also require verification against every referenced FX prototype.

Do not enable push-triggered CI: tests run on demand to minimize GitHub Actions usage.
