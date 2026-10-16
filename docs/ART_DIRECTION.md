# FluxWorks Visual Identity · Razi Protocol Extension

## Artistic goal

Industrial, engineered, physically plausible, unambiguously Factorio. Razi tells the science fiction story; FluxWorks shows the tools required to build it. Avoid pseudo-3D floating icons, giant bloom halos, neon gradients on every edge, random circuitry, or overlay clutter that stops an icon being recognizable at 32 px. Small custom machines should read beside vanilla and K2SO entities.

| Discipline | Accent | Metallic/secondary | Form language | Primary materials |
| --- | --- | --- | --- | --- |
| Matter / Purple | `#A57AD8` | `#6B527F` | hexagonal alignment, segmented prisms, fixed points | ceramic, dark alloy, quantum crystals |
| Chemical / Yellow | `#D4B34A` | `#927A39` | cylindrical columns, filtration mesh, clear vessels | glass, brass, polymer |
| Fuel / Red | `#D66A58` | `#933F33` | furnace mouths, reinforced heat sinks, heavy ducts | iron, refractory brick, bright slag |
| Biological / Green | `#68B78A` | `#377458` | growth chambers, lattice membranes, translucent nutrient conduits | coated metal, wet polymer, biomass |

Colors are a starting palette, not a substitute for non-color visual differentiation. Aim for consistent physical scale and perspective, contact shadows, and modest emission only while operating.

## Machine families

| Stage | Examples | Required differentiation |
| --- | --- | --- |
| First extraction | Flux Quarry, Flux Harvester | drilling and intake silhouette, loose material flow |
| Synthesis | Synthesis Plant, Precision Synthesis Plant | visible mixing columns, deliberate manifold layout |
| High energy | Arc Foundry, Chromatic Arc Foundry | high-temperature vessel, slag handling, deep thermal glow |
| Convergence | Convergence Synthesis Plant | multiple controlled streams converging into one core |
| Logistics | Spectral Reservoir, Phase Vault, Rift Exchange | different function-first silhouettes and readable port directions |

The four Industrial Project machines already retain original collision dimensions, fluid box positions and upgrade planner compatibility. Any eventual sprite remake **must** keep the engine dimensions in FluxWorks machine prototypes and not change the machine's footprint or pipes.

## Technology art and icons

- Technology illustrations: square, cropped for Factorio, intentional central silhouette, a single visual story per tech. Do not stack stock sprites or generic colored circles.
- Inventory icons: easily differentiated at 32 and 64 px, consistent material light direction, no tiny text, no large glow. Keep clear margins.
- Spectrum overlay emblems: retain exact published paths below so all 22 industry recipes and the existing project machine upgrades resolve. Keep their orientation, alpha and distinctive visual marks.
- Four-spectrum crossovers: maximum **two small spectrum emblems** around the bottom edge, never cover the output icon's primary shape.
- Legacy landable Shattered Planet terrain and the custom menu logo are retired; other save-referenced industrial textures remain until tested.

## Performance and consistency

- Preserve existing sprite atlases and file paths; avoid giant uncompressed frames or unnecessary idle animation layers.
- Prefer native crafting tint/working visualisations rather than frequent scripted visual updates.
- Test working, idle, unpowered, frozen and module-upgraded machine states, including standard- and high-resolution display scales.
- Check contrast on Factorio's dark UI and recipe icons in Factoriopedia, with Razi's violet Industrial Atlas page.

## Handoff checklist

1. Export each new machine sprite at dimensions matching its prototype.
2. Preview idle, working, shadow, and light masks together in a Factorio test save.
3. Check 32 px recognizable silhouette, 64 px inventory icon, 256 px technology illustration.
4. Confirm no missing asset references and no alpha halos.
5. Update asset contract with every new path before enabling it in FluxWorks; bump Assets version if new binaries are required.
6. Keep binary changes separate from gameplay logic, with source and compression details in any artwork PR.

## Art delivered in Assets 1.0.5

The four project upgrade emblems are not palette-swapped circles: the Harvester uses an extraction drill, the Precision Synthesis Plant uses a triad reaction diagram, the Chromatic Foundry uses a crucible, and the Convergence Plant combines four spectra into one controlled core. Four 128px RGBA game-ready PNGs and matching editable SVG masters are stored in `graphics/icons/upgrade-badges/` and `art/source/`. These are designed as small layered icons and deliberately do **not** replace the original machines' footprint, pipes, idle and working sprite sheets, or lights.

## Seven-system navigation icon set

The Calidus hub uses a concentric mechanical ring; Solaris a glowing solar turbine; Nyxaris a green growth leaf; Vibrant a lightning bolt; Vespera a snowflake; Beetlejuice an engineered crystal cube; Umbra a crescent eclipse; and Deep Space a navigation star. All eight are actual 128px game-ready PNG emblems with editable source SVGs. They are rendered as small corner marks alongside each native factory product, never used as full-size substitute icons for an item. Existing four-spectrum overlays remain the primary manufacturing cue.

## 0.4 Reborn intermediate families

Five independent industrial material silhouettes represent concrete industrial tasks, not interchangeable Flux circles: the chemical separation membrane, refractory thermal core, phase-alignment wafer, living biotech fiber and four-part convergence chassis. Their item prototypes are registered by FluxWorks, and the graphics remain here. Existing full-world machine sprite sheets are still used. They must be replaced intentionally as a separate animation/sprite-sheet art project rather than claimed as complete now.

## Industrial identity and the Atlas

The Four Works emblem is a single central fabrication joint connected to four engineering disciplines, distinct from any Razi planet icon. The Atlas is seven calibrated field nodes oriented toward one shared industrial axis. The first must read well without Razi installed; the second exists only for Razi-integrated field research. Neither should replace existing machine or planet artwork. SVG sources remain editable while PNGs are the runtime artifacts.
