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
outfpath_temp = outfpath.with_suffix(".temp")
exclude_list = EXCLUDE.split('|')
sdx, edx, printed = None, None, False

assert startpath.exists(), f"{startpath} not found. Aborting"

if not outfpath.parent.exists():
  # folder needs to exist before open() context
  outfpath.parent.mkdir(parents=True, exist_ok=True)
  
# TODO try except dirtree
dirtree = get_tree_output(startpath, exclude_list, CMD_HIGHLIGHT)

# TODO read and write while avoiding copying to memory
# TODO remove redundant line loop if possible
# will replace content between indices of first consecutive START and END
# will only insert between START and END
# will not insert if no match of START and END
with open(outfpath, 'r') as f_in:
  with open(outfpath_temp, 'w') as f_out:
    for index, line in enumerate(f_in):
      if line.startswith(INSERT_HERE_START_STRING):
        sdx = index
      elif line.startswith(INSERT_HERE_END_STRING) and sdx:
        edx = index
        break
    f_in.seek(0)
    print(f"{sdx=}, {edx=}")
    if sdx and edx:
      for index, line in enumerate(f_in):
        print(f"{index=}, {line=}")
        if index <= sdx or index >= edx:
          f_out.write(line)
        elif not printed:
          print(f"{printed=}")
          for o in dirtree:
            f_out.write(o)
          printed = True
          # f_in.seek(edx)

if sdx and edx:
  outfpath.unlink() # missing_ok=True
  outfpath_temp.rename(outfpath)
