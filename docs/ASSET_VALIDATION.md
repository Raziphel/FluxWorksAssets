# FluxWorks Assets development checks

This branch includes **four newly authored machine-upgrade PNG badges**, plus all original Flux icons and graphics. The offline validator checks the existing six named assets and four upgrade badges, and verifies editable SVG masters.

```sh
python3 scripts/validate_extension_assets.py
```

The checker validates `docs/ASSET_CONTRACT.json`, confirms each expected path is safely relative, checks each file exists, verifies the PNG signature, IHDR dimensions and sane bounds, and detects duplicate palette IDs/paths. It is dependency-free, deterministic, and read-only.

## Limitations

Passing does **not** mean the mod fully loads. Runtime sprite compatibility (tile dimensions, sprite sheet slicing, texture decompression, scale, shift, mipmap and animation frame declarations), usability at 32 px, art quality and consistency require a full Factorio 2.1 load with Razi Protocol and FluxWorks, followed by manual visual inspection. Asset location and technology compatibility also require verification against every referenced FX prototype.

Do not enable push-triggered CI: tests run on demand to minimize GitHub Actions usage.

## Galactic badges 1.0.6

Eight new 128×128 RGBA PNG emblems and corresponding editable SVGs cover all seven Razi systems and Deep Space. The offline checker verifies every PNG header/IHDR, unique recorded path, full source master and system ID. FluxWorks 0.3.2+ references the icons as optional small layered recipe and technology markers. Full Factorio 2.1 icon scale, atlas and contrast testing remains a release gate.

## Retired artwork (Assets 1.0.7)

The contract rejects five old standalone-only files that cannot be used by FluxWorks' current Razi-hosted loader. Do not delete other legacy sprites simply because their names look old: verify all active Lua prototype references and an existing-save Factorio test first.

## Spectrum manufacturing sprites in Assets 1.0.8

This repository now contracts **23 known active PNG assets**, including five newly authored 128x128 item graphics for Reborn's chemistry, heat, phase, biology, and convergence outputs. The offline validator verifies their paths, PNG signature, dimensions, SVG design references, and five distinct identities. PNG signature and dimensions do **not** verify sprite atlas behavior; a real Factorio 2.1 load remains necessary.
