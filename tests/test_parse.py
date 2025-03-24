from pathlib import Path
from sleepsrc.sleepnotes.parse import iter_entries

def test_iter_no_files(tmp_path: Path):
    list(iter_entries(tmp_path)) == []
