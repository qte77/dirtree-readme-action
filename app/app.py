import os
from datetime import datetime, timezone

OUT_FILE = str(os.getenv("OUT_FILE", 'data/dummy-data.md'))
EXCLUDE = str(os.getenv("EXCLUDE", '.git')) # separated by |
CMD_HIGHLIGHT = str(os.getenv("CMD_HIGHLIGHT", 'sh'))

out = []
startpath = '.'

space =  '    '
branch = '│   '
tee =    '├── '
last =   '└── '

if not os.path.exists(OUT_FILE):
  # folder needs to exist before open() context
  os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)

out.append(f"\n{datetime.now(timezone.utc)}")

# https://stackoverflow.com/a/9728478/list-directory-tree-structure-in-python
# https://stackoverflow.com/a/59109706/list-directory-tree-structure-in-python
print(exclude_list)
for root, dirs, files in os.walk(startpath):
    print(root)
    for ex in EXCLUDE.split('|'):
      if ex in root.split('/'):
        continue
    level = root.replace(startpath, '').count(os.sep)
    print(level)
    num_dirs = len(dirs)
    num_files = len(files)
    indent = branch * level
    indent_d = indent if level < 1 else indent + ( tee if num_dirs > 1 else last )
    out.append(f'{indent_d}{os.path.basename(root)}/')
    for i, f in enumerate(files):
      indent_f = indent + space + ( tee if num_files > i else last )
      out.append(f'{indent_f}{f}')

with open(OUT_FILE, 'a+', newline=None, encoding='UTF8') as f:
  f.write("\n```sh")
  for o in out: # reversed(out):
    f.write(f"{o}\n")
  f.write("```\n")
