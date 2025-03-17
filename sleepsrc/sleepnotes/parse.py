from __future__ import annotations
from pathlib import Path
from typing import Iterable, Dict


def iter_entries(notes_dir: Path):
    for f in sorted(notes_dir.glob("sleep_*.txt")):
        line = f.read_text(encoding="utf-8").strip()
        fields = [seg.strip() for seg in line.split("|")]
        data = {"raw": line}
        for seg in fields[1:]:
            if "=" in seg:
                k, v = seg.split("=", 1)
                data[k.strip()] = v.strip()
        yield data
