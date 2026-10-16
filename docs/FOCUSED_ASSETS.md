# Assets after the Focused Industry reset

FluxWorks 0.7 retires its standalone mineral patches, alternative metals, oversized chemical/atomic branches and legacy storage gates from **new gameplay**. Their graphics are intentionally **not deleted from FluxWorksAssets yet** because the corresponding item, entity and resource prototypes remain registered invisibly for saved-world compatibility. Deleting those PNGs while the prototypes still reference them would produce missing-sprite load errors.

## Current active identities

The four Flux spectra, the five manufactured signature components, the core processing machines, the Four Works charter, and optional Razi Foundries constitute the visible Focused identity. Their artwork stays maintained and on disk.

The additional regional badges, heritage crusher/metal sprites, Phase Vault/Reservoir/Rift Exchange assets, and historical Shattered scenes are now **legacy assets**. Their presence in the package is not a claim that they are still part of normal play.

## When it becomes safe to delete them

1. Remove the last references to each sprite from FluxWorks' prototype declarations and compatibility shims.
2. Decide whether existing save inventories, blueprints, entities and research must still be supported.
3. Migrate saved prototypes first, or announce a deliberate breaking major release.
4. Update ASSET_CONTRACT.json and scripts/validate_extension_assets.py *together*, then delete confirmed unreferenced PNGs.
5. Verify all Factorio prototypes with the full Space Age + K2SO + Razi combinations.

The Focused pass did not add a new artwork generation pipeline or remove original machine animation sheets. A future art overhaul should spend time on a handful of distinctive **industrial machines**, not repaint a hundred unused ores.
