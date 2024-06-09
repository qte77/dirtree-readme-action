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

exclude_list = EXCLUDE.split('|')

if not os.path.exists(OUT_FILE):
  # folder needs to exist before open() context
  os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)

out.append(f"\n{datetime.now(timezone.utc)}")

# https://stackoverflow.com/a/9728478/list-directory-tree-structure-in-python
# https://stackoverflow.com/a/59109706/list-directory-tree-structure-in-python
for root, dirs, files in os.walk(startpath):
    level = root.replace(startpath, '').count(os.sep)
    if root not in EXCLUDE:
      indent = space * level
      out.append(f'{indent}{os.path.basename(root)}/')
      subindent = space * (level + 1)
      for f in files:
          out.append(f'{subindent}{f}')

with open(OUT_FILE, 'a+', newline=None, encoding='UTF8') as f:
  f.write("\n```sh")
  for o in out: # reversed(out):
    f.write(f"{o}\n")
  f.write("```\n")
