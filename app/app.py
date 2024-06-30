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

dirtree = get_tree_output(startpath, exclude_list, CMD_HIGHLIGHT)

with open(outfpath, 'r+') as f:
    contents = fd.readlines()
    if INSERT_HERE_STRING in contents[-1]:
        contents.append(dirtree)
    else:
        for index, line in enumerate(contents):
            # only insert afet first match
            if INSERT_HERE_STRING in line and dirtree[0] not in contents[index + 1]:
                contents.insert(index + 1, dirtree)
                break
    fd.seek(0)
    fd.writelines(contents)
