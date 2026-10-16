# FluxWorks Assets

Asset library for **FluxWorks 0.3.5**, the industrial engineering extension to Razi Protocol.

This package ships sprites and graphical resources used by the four Flux spectra, extractor and fabrication machines, Flux recovery icons, and compatibility-sensitive legacy manufacturing content. It contains **no gameplay rules, technologies, quests, or campaign logic**. Install it as a dependency of FluxWorks; FluxWorks requires Razi Protocol for gameplay.

## Art direction

The four Flux disciplines must be recognizable at inventory-icon size as well as in large industrial machines:

- **Matter (purple):** prismatic edges, stable geometric lattices and controlled phase distortion.
- **Chemical (yellow):** precise glasswork, chromatography lines, catalysts and amber illumination.
- **Fuel (red):** heat ceramics, slag, turbine housings and molten orange-red channels.
- **Biological (green):** fibrous membranes, tissue-like channels, condensation and deep chlorophyll tones.

Prefer silhouettes, material finishes and symbol language rather than recoloring an identical sprite four times. Preserve existing asset paths: item and technology prototypes in established saves refer to them.

The extension's eight new foundry processes deliberately use **existing product icons with native Flux overlays**. Their new names and crafting ratios belong to the FluxWorks repository, not this assets-only package.

See [Art direction](docs/ART_DIRECTION.md), [Asset contract](docs/ASSET_CONTRACT.json), and [Validation](docs/ASSET_VALIDATION.md).

## Maintainer workflow

Run the offline reference checker:

```bash
python3 scripts/validate_extension_assets.py
```

This tool checks known extension icon paths and valid PNG dimensions without third-party dependencies. It does not replace in-game Factorio sprite/prototype loading, atlas packing, tint rendering, animations, collision footprints or a visual QA review. No automatic GitHub Action is enabled.

**0.3 development:** This branch retains existing full machine sprite animations and adds four new 128px PNG machine-upgrade badges with editable vector masters. A complete machine sprite-sheet replacement remains a separate art deliverable.

## New Industrial Project emblems (1.0.5)

Four new PNG icons are now bundled at `graphics/icons/upgrade-badges/`: a gold drilling head (Industrial Harvester), violet triangular reaction graph (Precision Synthesis), red crucible (Chromatic Foundry), and four-color central convergence (Convergence Plant). Editable SVG sources live in `art/source/`. These are real new inventory-icon assets, not full replacement sprite-sheet animations. The existing large machine renderings and tile footprints are preserved.


## Eight system emblems · 1.0.6

Added a separate 128px PNG (plus editable SVG master) for each of Calidus, Solaris, Nyxaris, Vibrant, Vespera, Beetlejuice, Umbra, and Deep Space. FluxWorks uses these as small overlays on its optional planet/K2SO/freight technologies and recipes, while keeping the product's native icon and the recognizable Flux emblem. All existing asset paths and machine animation frames remain unchanged.

## 1.0.7 lean graphics package

Removed one obsolete FluxWorks custom-menu logo and four terrain textures used exclusively by its deleted landable Shattered Planet code. Razi owns planetary terrain and menu scenes. Other machine sprite atlases, used rocket recovery graphics, 18 contracted active icons, and legacy manufacturing textures remain until safe save-prototype migration is proven. The validator now rejects the five retired paths as well as verifying retained core assets.

## New spectrum production art (1.0.8)
Five new authored 128px industrial item icons and editable SVG design references: Yellow Separation Membrane, Red Thermal Core, Purple Phase Wafer, Green Living Fiber and four-spectrum Convergence Chassis. These are new manufactured items, not replacements of original machine animation sprite sheets.
