from os import getenv
from pathlib import Path
from utils import get_tree_output, write_to_file


CMD_HIGHLIGHT = str(getenv("CMD_HIGHLIGHT", ''))
TREE_THEME = str(getenv("TREE_THEME", ''))
# EXCLUDE string separated by |
EXCLUDE = str(getenv("EXCLUDE", '.git|__pycache__'))
INSERT_HERE_START_STRING = str(getenv(
  "INSERT_HERE_START_STRING", ''
))
INSERT_HERE_END_STRING = str(getenv(
  "INSERT_HERE_END_STRING", ''
))
OUT_FILE = str(getenv("OUT_FILE", 'README.md'))


startpath = Path('.')
outfpath = Path(OUT_FILE)
outfpath_temp = outfpath.with_suffix(".temp")
exclude_list = EXCLUDE.split('|')
sdx, edx, printed = None, None, False


assert startpath.exists(), f"{startpath} not found. Aborting"
if not outfpath.parent.exists():
  # folder needs to exist before open() context
  outfpath.parent.mkdir(parents=True, exist_ok=True)


dirtree = get_tree_output(
  startpath, exclude_list,
  CMD_HIGHLIGHT, 
)
if isinstance(dirtree, list):
  write_to_file(
    outfpath, outfpath_temp, dirtree,
    INSERT_HERE_START_STRING, INSERT_HERE_END_STRING
  )
