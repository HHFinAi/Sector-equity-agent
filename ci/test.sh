#!/bin/sh
set -eu
cd "$(dirname "$0")/.."
python -m unittest discover -s tests -v
tmpdir=$(mktemp -d)
trap 'rm -rf "$tmpdir"' EXIT HUP INT TERM
python -m sector_agent run --brief examples/demo-brief.json --out "$tmpdir/demo"
python -m sector_agent verify --run "$tmpdir/demo"
