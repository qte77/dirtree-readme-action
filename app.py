import os
from datetime import datetime, timezone

OUT_FILE = str(os.getenv("OUT_FILE", 'data/dummy-data.md'))
EXCLUDE = str(os.getenv("EXCLUDE"))
CMD_HIGHLIGHT = str(os.getenv("CMD_HIGHLIGHT", 'sh'))

k = 0
out = []

if EXCLUDE is not None:
  EXCLUDE = EXCLUDE.split('|')

if not os.path.exists(OUT_FILE):
  # folder needs to exist before open() context
  os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
  out.append(str(datetime.now(timezone.utc)))

for dirname, dirnames, filenames in os.walk('.'):
  indent = "\t" * (k+1)
  indent_f = "\t" * (k+2)
  for ex in EXCLUDE:
    if ex in dirnames:
      dirnames.remove(ex)
  for subdirname in dirnames:
    dir = os.path.join(dirname, subdirname)
    out.append(f"{indent}{dir}")
  for filename in filenames:
    file = os.path.join(dirname, filename)
    out.append(f"{indent_f}{file}")

with open(OUT_FILE, 'a+', newline=None, encoding='UTF8') as f:
  f.write("\n```sh")
  for o in reversed(out):
    f.write(f"{o}\n")
  f.write("```\n")
