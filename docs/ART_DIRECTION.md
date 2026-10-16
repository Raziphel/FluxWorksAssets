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
- Legacy standalone Shattered Planet textures stay in the package for compatibility but must not appear as new Razi destinations or Razi's galactic art.

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
