#!/usr/bin/env bash
set -euo pipefail

source_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
assets_dir="$(cd -- "$source_dir/../.." && pwd)"
output="$assets_dir/graphics/menu-simulations/fw-logo.png"
font="$source_dir/Full Automation-Squared.otf"
work_dir="$(mktemp -d)"
trap 'rm -rf -- "$work_dir"' EXIT

common=(
  -gravity center
  -font "$font"
  -pointsize 330
  -kerning -5
)

magick -size 2048x768 xc:black "${common[@]}" \
  -fill white -stroke none -annotate +0-4 FLUXWORKS \
  "$work_dir/mask.png"

magick -seed 1337 -size 2048x768 gradient:'#b86f86-#74394f' \
  -attenuate 0.10 +noise Gaussian -blur 0x0.35 \
  "$work_dir/face.png"

magick -size 2048x768 xc:none "${common[@]}" \
  -fill '#100c0a' -stroke '#050403' -strokewidth 34 -annotate +31+47 FLUXWORKS \
  -fill '#2c1917' -stroke '#0c0807' -strokewidth 24 -annotate +20+31 FLUXWORKS \
  -fill '#4b2928' -stroke '#9b5b28' -strokewidth 16 -annotate +7+10 FLUXWORKS \
  -fill '#00000000' -stroke '#e39a3f' -strokewidth 10 -annotate +0-4 FLUXWORKS \
  "$work_dir/base.png"

magick "$work_dir/base.png" "$work_dir/face.png" "$work_dir/mask.png" \
  -compose over -composite "${common[@]}" \
  -fill none -stroke '#f1b660' -strokewidth 2 -annotate +0-5 FLUXWORKS \
  -depth 8 \
  "$output"
