import os
from datetime import datetime, timezone

OUT_FILE = str(os.getenv("OUT_FILE", 'data/dummy-data.md'))
EXCLUDE = str(os.getenv("EXCLUDE", '.git')) # separated by |
CMD_HIGHLIGHT = str(os.getenv("CMD_HIGHLIGHT", 'sh'))

out = []
startpath = '.'
exclude_list = EXCLUDE.split('|')

space = '    '
branch = '│   '
tee = '├── '
last = '└── '

if not os.path.exists(OUT_FILE):
  # folder needs to exist before open() context
  os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)

out.append(f"\n{datetime.now(timezone.utc)}")

def find_exclusion_overlap(root: str, exclude_list: list) -> bool:
  '''Return True if any of exclude in root split by "/", else False'''
  assert isinstance(root, str) and isinstance(exclude_list, list)
  for ex in exclude_list:
    if ex in root.split('/'):
      return True
  return False  

# https://stackoverflow.com/a/9728478/list-directory-tree-structure-in-python
# https://stackoverflow.com/a/59109706/list-directory-tree-structure-in-python
for root, dirs, files in os.walk(startpath):
    if find_exclusion_overlap(root, exclude_list):
      continue
    level = root.replace(startpath, '').count(os.sep)
    num_dirs = len(dirs)
    num_files = len(files)
    indent = branch * (level-1)
    indent_d = indent if level < 1 else indent + ( tee if num_dirs > 1 else last )
    out.append(f'{indent_d}{os.path.basename(root)}/ # DEBUG::{level=},{num_dirs=},{num_files=}')
    for i, f in enumerate(files):
      indent_f = indent_d + ( "" if level < 1 else space ) + ( tee if (num_files-1 > i and num_dirs < 1) else last )
      out.append(f'{indent_f}{f}')

with open(OUT_FILE, 'a+', newline=None, encoding='UTF8') as f:
  f.write("\n```sh")
  for o in out: # reversed(out):
    f.write(f"{o}\n")
  f.write("```\n")
