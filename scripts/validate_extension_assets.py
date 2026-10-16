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
    projects = manifest.get("project_badges", [])
    expected_machines = {
        "fw-industrial-harvester",
        "fw-precision-synthesis-plant",
        "fw-chromatic-arc-foundry",
        "fw-convergence-synthesis-plant",
    }
    assert len(projects) == 4
    assert {entry["machine"] for entry in projects} == expected_machines
    assert {entry["icon"] for entry in projects}.issubset(set(expected))
    for entry in projects:
        path = (ROOT / entry["source"]).resolve()
        if not path.is_relative_to(ROOT) or not path.is_file():
            raise FileNotFoundError(f"Missing editable SVG master: {entry['source']}")
        source = path.read_text(encoding="utf-8")
        if '<svg ' not in source or '</svg>' not in source:
            raise ValueError(f"Malformed SVG art source: {entry['source']}")
    systems = manifest.get("system_badges", [])
    expected_systems = {
        "calidus", "solaris", "nyxaris", "vibrant",
        "vespera", "beetlejuice", "umbra", "deep-space"
    }
    assert len(systems) == 8, "Expected eight separate system emblems"
    assert {badge["system"] for badge in systems} == expected_systems
    for badge in systems:
        assert badge["icon"] in expected
        assert badge["icon_size"] == 128
        source = (ROOT / badge["source"]).resolve()
        if not source.is_relative_to(ROOT) or not source.is_file():
            raise FileNotFoundError(f"Missing system vector master: {badge['source']}")
        svg = source.read_text(encoding="utf-8")
        if "<svg " not in svg or "</svg>" not in svg:
            raise ValueError(f"Malformed system vector master: {badge['source']}")
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
