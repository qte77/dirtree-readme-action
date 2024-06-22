from os import getenv
from datetime import datetime, timezone
from pathlib import Path
import .utils

OUT_FILE = str(getenv("OUT_FILE", 'data/dummy-data.md'))
EXCLUDE = str(getenv("EXCLUDE", '.git')) # separated by |
CMD_HIGHLIGHT = str(getenv("CMD_HIGHLIGHT", 'sh'))

startpath = Path('.')
outfpath = Path(OUT_FILE)
exclude_list = EXCLUDE.split('|')

space = '    '
branch = '│   '
tee = '├── '
last = '└── '

assert startpath.exists(), f"{startpath} not found. Aborting"

if not outfpath.parent.exists():
  # folder needs to exist before open() context
  outfpath.parent.mkdir(parents=True, exist_ok=True)

with open(outfpath, 'a+', newline=None, encoding='UTF8') as f:
  for o in get_tree(startpath):
    f.write(f"{o}\n")
