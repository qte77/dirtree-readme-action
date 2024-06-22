from os import getenv, makedirs 
from os.path import dirname, exists
from datetime import datetime, timezone
from pathlib import Path

OUT_FILE = str(getenv("OUT_FILE", 'data/dummy-data.md'))
EXCLUDE = str(getenv("EXCLUDE", '.git')) # separated by |
CMD_HIGHLIGHT = str(getenv("CMD_HIGHLIGHT", 'sh'))

out = []
startpath = '.'
exclude_list = EXCLUDE.split('|')

space = '    '
branch = '│   '
tee = '├── '
last = '└── '

assert exists(startpath), f"{startpath} not found. Aborting"

def find_exclusion_overlap(path: Path, exclude_list: list) -> bool:
  '''Return True if any of exclude in root split by "/", else False'''
  assert isinstance(path, Path) and isinstance(exclude_list, list)
  for ex in exclude_list:
    if ex in root.split('/'):
      return True
  return False  

# https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python/59109706
def tree(dir_path: Path, prefix: str=''):
    """
    A recursive generator, given a directory Path object
    will yield a visual tree structure line by line
    with each line prefixed by the same characters
    """    
    if find_exclusion_overlap(dir_path, exclude_list):
      pass
    contents = list(dir_path.iterdir())
    # contents each get pointers that are ├── with a final └── :
    pointers = [tee] * (len(contents) - 1) + [last]
    for pointer, path in zip(pointers, contents):
        yield prefix + pointer + path.name
        if path.is_dir():
            extension = branch if pointer == tee else space 
            yield from tree(path, prefix=prefix+extension)

if not exists(OUT_FILE):
  # folder needs to exist before open() context
  makedirs(dirname(OUT_FILE), exist_ok=True)

out.append(f"\n```{CMD_HIGHLIGHT}")
out.append(f"\n{datetime.now(timezone.utc)}")
for line in tree(Path(startpath)):
    out.append(line)
out.append("```\n")

with open(OUT_FILE, 'a+', newline=None, encoding='UTF8') as f:
  for o in out: # reversed(out):
    f.write(f"{o}\n")
