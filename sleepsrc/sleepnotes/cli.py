#!/usr/bin/env python3
import argparse
from pathlib import Path
from datetime import datetime

NOTES_DIR = Path(__file__).resolve().parent.parent / "notes"


def ensure_notes_dir() -> Path:
    NOTES_DIR.mkdir(parents=True, exist_ok=True)
    return NOTES_DIR


def cmd_add(args: argparse.Namespace) -> None:
    notes = ensure_notes_dir()
    stamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    line = f"{datetime.now().isoformat(timespec='seconds')} | duration={args.duration} | quality={args.quality} | note={args.note}\n"
    (notes / f"sleep_{stamp}.txt").write_text(line, encoding="utf-8")
    print("Saved:", line.strip())


def cmd_summarize(_args: argparse.Namespace) -> None:
    notes = ensure_notes_dir()
    files = sorted(notes.glob("sleep_*.txt"))
    if not files:
        print("No notes yet.")
        return
    total = 0.0
    count = 0
    for f in files:
        text = f.read_text(encoding="utf-8")
        parts = dict(p.split("=", 1) for p in (seg.strip() for seg in text.split("|")[1:]) if "=" in p)
        try:
            total += float(parts.get("duration", 0))
            count += 1
        except ValueError:
            pass
    avg = total / count if count else 0
    print(f"Entries: {count}\nAvg duration: {avg:.2f}h")


def main():
    p = argparse.ArgumentParser(prog="sleepnotes", description="Quick sleep notes")
    sub = p.add_subparsers(dest="cmd", required=True)

    p_add = sub.add_parser("add", help="Add a new sleep note")
    p_add.add_argument("--duration", type=float, required=True, help="Hours slept")
    p_add.add_argument("--quality", type=int, choices=range(1,6), metavar="[1-5]", required=True)
    p_add.add_argument("--note", type=str, default="")
    p_add.set_defaults(func=cmd_add)

    p_sum = sub.add_parser("summarize", help="Summarize notes")
    p_sum.set_defaults(func=cmd_summarize)

    args = p.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
