from os import getenv
from pathlib import Path
from utils import get_tree_output

OUT_FILE = str(getenv("OUT_FILE", 'README.md'))
EXCLUDE = str(getenv("EXCLUDE", '.git|__pycache__')) # string separated by |
CMD_HIGHLIGHT = str(getenv("CMD_HIGHLIGHT", 'sh'))
INSERT_START_HERE_STRING = str(getenv(
  "INSERT_START_HERE_STRING", '<!-- DIRTREE-README-ACTION-INSERT-START-HERE -->'
))
INSERT_END_HERE_STRING = str(getenv(
  "INSERT_END_HERE_STRING", '<!-- DIRTREE-README-ACTION-INSERT-END-HERE -->'
))

startpath = Path('.')
outfpath = Path(OUT_FILE)
exclude_list = EXCLUDE.split('|')

assert startpath.exists(), f"{startpath} not found. Aborting"

if not outfpath.parent.exists():
  # folder needs to exist before open() context
  outfpath.parent.mkdir(parents=True, exist_ok=True)

dirtree = get_tree_output(startpath, exclude_list, CMD_HIGHLIGHT)

with open(outfpath, 'r+') as f:
  # TODO remove redundant line loop
  # TODO 
  # will not insert, if no match and will only insert after first match
  # will delete content between START and END
  sdx, edx = None, None
  for index, line in enumerate(f):
    print(f"{index=}, {line=}")
    if INSERT_START_HERE_STRING in line and sdx is None:
      sdx = index
      print(f"{sdx}, {dirtree[0]=}, {contents[index + 1]=}")
    elif INSERT_END_HERE_STRING in line and sdx and edx is None:
      edx = index
      print(f"{edx=}, {dirtree[0]=}, {contents[index + 1]=}")
      break
  for index, line in enumerate(f):
    if index <= sdx or index >= edx:
      f.write(line)
    else:
      for o in dirtree:
        f.write(o)
