from os import getenv
from pathlib import Path
from utils import get_tree_output

OUT_FILE = str(getenv("OUT_FILE", 'data/dummy-readme.md'))
EXCLUDE = str(getenv("EXCLUDE", '.git|__pycache__')) # string separated by |
CMD_HIGHLIGHT = str(getenv("CMD_HIGHLIGHT", 'sh'))
INSERT_HERE_STRING = str(getenv("INSERT_HERE_STRING", '<!-- DIRTREE-README-ACTION-INSERT-HERE -->'))

startpath = Path('.')
outfpath = Path(OUT_FILE)
exclude_list = EXCLUDE.split('|')

assert startpath.exists(), f"{startpath} not found. Aborting"

if not outfpath.parent.exists():
  # folder needs to exist before open() context
  outfpath.parent.mkdir(parents=True, exist_ok=True)

with open(outfpath, "r") as f:
    contents = f.readlines()

contents.insert(
  INSERT_HERE_STRING,
  get_tree_output(startpath, exclude_list, CMD_HIGHLIGHT)
)

with open(outfpath, 'a+', newline=None, encoding='UTF8') as f:
  # contents = "".join(contents)
  f.write(contents)
