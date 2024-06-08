import os
import csv
from datetime import datetime, timezone

OUT_FILE = str(os.getenv("OUT_FILE", 'data/dummy-data.md'))
EXCLUDE = str(os.getenv("EXCLUDE"))
k = 0
out = []

if EXCLUDE is not None:
  EXCLUDE = EXCLUDE.split('|')
if not os.path.exists(OUT_FILE):
  # folder needs to exist before open() context
  os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
  out.append([f"{datetime.now(timezone.utc)}\n"])

print(os.walk('.'))

for dirname, dirnames, filenames in os.walk('.'):
  indent = " " * (k+1)
  indent_f = " " * (k+2)
  for ex in EXCLUDE:
    if ex in dirnames:
      dirnames.remove(ex)
  for subdirname in dirnames:
    dir = os.path.join(dirname, subdirname)
    out.append([f"{indent}{dir}\n"])
  for filename in filenames:
    file = os.path.join(dirname, filename)
    out.append([f"{indent_f}{file}\n"])

with open(OUT_FILE, 'a+', newline=None, encoding='UTF8') as f:
  writer = csv.writer(f)
  for o in out:
    writer.writerow(o)
