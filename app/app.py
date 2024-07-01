from os import getenv
from pathlib import Path
from utils import get_tree_output

OUT_FILE = str(getenv("OUT_FILE", 'README.md'))
EXCLUDE = str(getenv("EXCLUDE", '.git|__pycache__')) # string separated by |
CMD_HIGHLIGHT = str(getenv("CMD_HIGHLIGHT", 'sh'))
INSERT_HERE_START_STRING = str(getenv(
  "INSERT_HERE_START_STRING", '<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->'
))
INSERT_HERE_END_STRING = str(getenv(
  "INSERT_HERE_END_STRING", '<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->'
))

startpath = Path('.')
outfpath = Path(OUT_FILE)
exclude_list = EXCLUDE.split('|')

assert startpath.exists(), f"{startpath} not found. Aborting"

if not outfpath.parent.exists():
  # folder needs to exist before open() context
  outfpath.parent.mkdir(parents=True, exist_ok=True)

# try except
dirtree = get_tree_output(startpath, exclude_list, CMD_HIGHLIGHT)

with open(outfpath, 'r+') as f:
  # TODO remove redundant line loop if possible
  # will replace content between indices of first consecutive START and END
  # will only insert between START and END
  # will not insert if no match of START and END
  sdx, edx, printed = None, None, False
  for index, line in enumerate(f):
    if line.startswith(INSERT_HERE_START_STRING):
      sdx = index
    elif line.startswith(INSERT_HERE_END_STRING) and sdx:
      edx = index
      break
  f.seek(0)
  if sdx and edx:
    print(f"{sdx=}, {edx=}")
    for index, line in enumerate(f):
      if index <= sdx or index >= edx:
        f.write(line)
      elif not printed:
        print(f"{printed=}")
        for o in dirtree:
          f.write(o)
        printed = True
    f.truncate()
