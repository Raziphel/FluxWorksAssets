#!/usr/bin/env python3
"""Offline PNG contract check for the Razi Protocol / FluxWorks extension.

No external Python packages or GitHub CI are required.
"""
from __future__ import annotations

import json
from pathlib import Path
import struct

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs" / "ASSET_CONTRACT.json"
PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


def main() -> int:
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    spectra = manifest["spectra"]
    expected = manifest["required_existing_paths"]
    assert len(spectra) == 4
    assert {entry["id"] for entry in spectra} == {
        "purple", "yellow", "red", "green"
    }
    assert len(expected) == len(set(expected))
    assert {entry["overlay"] for entry in spectra}.issubset(set(expected))
    for relpath in expected:
        path = (ROOT / relpath).resolve()
        if not path.is_relative_to(ROOT) or path.suffix.lower() != ".png":
            raise ValueError(f"Unsafe or non-PNG asset path: {relpath}")
        if not path.is_file():
            raise FileNotFoundError(f"Missing FluxWorks sprite: {relpath}")
        with path.open("rb") as stream:
            header = stream.read(24)
        if len(header) != 24 or header[:8] != PNG_SIGNATURE:
            raise ValueError(f"Invalid PNG signature: {relpath}")
        if header[12:16] != b"IHDR":
            raise ValueError(f"Missing PNG IHDR header: {relpath}")
        width, height = struct.unpack(">II", header[16:24])
        if not (1 <= width <= 8192 and 1 <= height <= 8192):
            raise ValueError(f"Invalid sprite dimensions {width}x{height}: {relpath}")
        print(f"OK {width:4}x{height:<4} {relpath}")
    print(f"Validated {len(expected)} existing extension assets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
