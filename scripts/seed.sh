#!/usr/bin/env bash
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
root="$(cd "$here/.." && pwd)"
notes="$root/sleepsrc/notes"
mkdir -p "$notes"
now="$(date +%Y-%m-%d_%H-%M-%S)"
echo "$(date -u +%Y-%m-%dT%H:%M:%S) | duration=7.2 | quality=4 | note=seed" > "$notes/sleep_${now}.txt"
