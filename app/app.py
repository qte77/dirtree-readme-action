from os import getenv
from pathlib import Path
from utils import get_tree_output, write_to_file


CMD_HIGHLIGHT = str(getenv("CMD_HIGHLIGHT", 'sh'))
# EXCLUDE string separated by |
EXCLUDE = str(getenv("EXCLUDE", '.git|__pycache__'))
INSERT_HERE_START_STRING = str(getenv(
  "INSERT_HERE_START_STRING"
  '<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->'
))
INSERT_HERE_END_STRING = str(getenv(
  "INSERT_HERE_END_STRING",
  '<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->'
))
OUT_FILE = str(getenv("OUT_FILE", 'README.md'))
TREE_THEME = str(getenv("TREE_THEME", 'sh'))


exclude_list = EXCLUDE.split('|')
outfpath = Path(OUT_FILE)
startpath = Path('.')


assert startpath.exists(), f"{startpath} not found. Aborting"
if not outfpath.parent.exists():
  # folder needs to exist before open() context
  outfpath.parent.mkdir(parents=True, exist_ok=True)


dirtree = get_tree_output(
  startpath, exclude_list, CMD_HIGHLIGHT, TREE_THEME
)
write_to_file(
  outfpath, dirtree,
  INSERT_HERE_START_STRING, INSERT_HERE_END_STRING
)
