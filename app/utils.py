'''Contains utility functions for Github dirtree-readme-action'''

from datetime import datetime, timezone
from pathlib import Path

def is_exclusion_in_path(path: Path, exclude_list: list) -> bool:
  '''Return True if any of exclude_list in path, else False'''
  assert isinstance(path, Path)
  assert isinstance(exclude_list, list)
  for pt in path.parts:
    if pt in exclude_list:
      return True
  return False

# https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python/59109706
def generate_tree(path: Path, exclude_list: list, prefix: str = ''):
  '''
  A recursive generator, given a directory Path object
  will yield a visual tree structure line by line
  with each line prefixed by the same characters
  '''
  if is_exclusion_in_path(path, exclude_list):
    return None
  contents = list(path.iterdir())
  # contents each get pointers that are ├── with a final └── :
  pointers = [tee] * (len(contents) - 1) + [last]
  for pointer, path in zip(pointers, contents):
      yield prefix + pointer + path.name
      if path.is_dir():
          extension = branch if pointer == tee else space
          prefix += extension
          yield from generate_tree(path, exclude_list, prefix)

def get_tree_output(startpath: Path, exclude_list: list, cmd_highlight: str) -> list:
  '''Returns a list of startpath and its children'''
  out = []
  out.append(f"\n```{cmd_highlight}")
  out.append(f"\n{datetime.now(timezone.utc)}")
  for line in generate_tree(startpath, exclude_list):
      out.append(line)
  out.append("```\n")
  return out
