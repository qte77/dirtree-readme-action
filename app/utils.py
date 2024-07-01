'''Contains utility functions for Github dirtree-readme-action'''

from datetime import datetime, timezone
from pathlib import Path


CMD_HIGHLIGHT = 'sh'


def get_tree_theme(theme: str = CMD_HIGHLIGHT) -> tuple:
  f'''
  Returns tuple of tree indicator themes: space, branch, tee, last.
  Offers 'cmd', 'slash', 'elli', 'null', 'sh'. Defaults to {CMD_HIGHLIGHT}
  '''
  if theme == 'cmd':
    return '   ', '│  ', '├──', '└──'
  if theme == 'slash':
    return '    ', '│   ', '\── ', '\── '
  if theme == 'elli':
    return '    ', '⋮   ', '⋱⋯⋯ ', '∵⋯⋯ '
  if theme == 'null':
    return '    ', '    ', '    ', '    '
  else: 
    return '    ', '│   ', '├── ', '└── '


def is_path_in_exclude(path: Path, exclude_list: list) -> bool:
  '''Return True if any of exclude_list in path, else False'''
  assert isinstance(path, Path)
  assert isinstance(exclude_list, list)
  for pt in path.parts:
    if pt in exclude_list:
      return True
  return False


# https://stackoverflow.com/questions/9727673/list-directory-tree-structure-in-python/59109706
def generate_tree(
  path: Path, exclude_list: list,
  cmd_highlight: str = CMD_HIGHLIGHT,
  prefix: str = ''
) -> str:
  '''
  A recursive generator, given a directory Path object
  will yield a visual tree structure line by line
  with each line prefixed by the same characters.
  Returns a string of the current folder or file
  and hierarchical indicators.
  '''
  contents = list(path.iterdir())
  space, branch, tee, last = get_tree_theme(cmd_highlight)
  # contents each get pointers that are 'tee' with a final 'last'
  pointers = [tee] * (len(contents) - 1) + [last]
  for pointer, path in zip(pointers, contents):
    if not is_path_in_exclude(path, exclude_list):
      yield prefix + pointer + path.name
      if path.is_dir():
          extension = branch if pointer == tee else space
          yield from generate_tree(
            path, exclude_list, prefix + extension
          )


def get_tree_output(
  startpath: Path, exclude_list: list,
  cmd_highlight: str = CMD_HIGHLIGHT
) -> list:
  '''Returns a list of startpath and its children'''
  out = []
  out.append(f"```{cmd_highlight}\n")
  out.append(f"{datetime.now(timezone.utc)}\n")
  for line in generate_tree(startpath, exclude_list, cmd_highlight):
      out.append(f"{line}\n")
  out.append("```\n")
  return out
