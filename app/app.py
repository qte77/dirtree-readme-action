from os import getenv
from pathlib import Path
from utils import get_tree_output, write_to_file


CMD_HIGHLIGHT = str(getenv("CMD_HIGHLIGHT"))
# EXCLUDE string separated by |
EXCLUDE = str(getenv("EXCLUDE"))
INSERT_HERE_START_STRING = str(getenv(
  "INSERT_HERE_START_STRING"
))
INSERT_HERE_END_STRING = str(getenv(
  "INSERT_HERE_END_STRING"
))
OUT_FILE = str(getenv("OUT_FILE", 'README.md'))
TREE_THEME = str(getenv("TREE_THEME"))


startpath = Path('.')
outfpath = Path(OUT_FILE)


assert startpath.exists(), f"{startpath} not found. Aborting"
if not outfpath.parent.exists():
  # folder needs to exist before open() context
  outfpath.parent.mkdir(parents=True, exist_ok=True)


dirtree = get_tree_output(
  startpath, exclude_list, CMD_HIGHLIGHT, 
)
write_to_file(
  outfpath, dirtree,
  INSERT_HERE_START_STRING, INSERT_HERE_END_STRING
)
