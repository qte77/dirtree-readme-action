'''Contains utility functions for Github dirtree-readme-action'''


from datetime import datetime, timezone
from pathlib import Path


def _get_tree_theme(theme: str) -> tuple:
  f'''
  Returns tuple of tree indicator themes: space, branch, tee, last.
  Offers 'cmd', 'slash', 'elli', 'null', 'sh'. Defaults to 'sh'.
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


def _is_path_in_exclude(
  path: Path, exclude_list: list
) -> bool:
  '''Return True if any of exclude_list in path, else False'''
  assert isinstance(path, Path)
  assert isinstance(exclude_list, list)
  for pt in path.parts:
    if pt in exclude_list:
      return True
  return False


# list-directory-tree-structure-in-python:
# https://stackoverflow.com/a/59109706
def _generate_tree(
  path: Path, exclude_list: list,
  space: str, branch: str, tee: str, last: str,
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
  # contents each get pointers that are 'tee' with a final 'last'
  pointers = [tee] * (len(contents) - 1) + [last]
  for pointer, path in zip(pointers, contents):
    if not _is_path_in_exclude(path, exclude_list):
      yield prefix + pointer + path.name
      if path.is_dir():
          extension = branch if pointer == tee else space
          yield from _generate_tree(
            path, exclude_list,
            space, branch, tee, last,
            prefix + extension
          )


def get_tree_output(
  startpath: Path, exclude_list: list,
  cmd_highlight: str, tree_theme: str
) -> list:
  '''Returns a list of startpath and its children'''
  space, branch, tee, last = _get_tree_theme(tree_theme)
  out = []
  out.append(f"```{cmd_highlight}\n")
  out.append(f"{datetime.now(timezone.utc)}\n")
  for line in _generate_tree(
    startpath, exclude_list,
    space, branch, tee, last
  ):
      out.append(f"{line}\n")
  out.append("```\n")
  return out


def get_write_positions_in_file(
  outfpath: Path, start_string: str, end_string: str
) -> tuple:
  '''
  Returns position of first consecutive start_string and
  end_string. 
  if no match of START and END
  '''
  sdx, edx = None, None
  print(f"{start_string=}, {end_string=}")
  with open(outfpath, 'r') as f_in:
    for index, line in enumerate(f_in):
      print(f"{index=}, {line=}")
      if line.startswith(start_string):
        sdx = index
      elif line.startswith(end_string) and sdx:
        edx = index
        break
  return sdx, edx


def write_to_file(
  outfpath: Path, dirtree: list,
  start_index: int, end_index: int
) -> None:
  '''Replaces content between indices start_index and end_index'''
  outfpath_temp = outfpath.with_suffix(".temp_outfile_ghact")
  printed = False
  assert start_index >= 0 and end_index >= 1, \
    f"Can not insert: {start_index=}, {end_index=}"
  with open(outfpath, 'r') as f_in:
    with open(outfpath_temp, 'w') as f_out:
      for index, line in enumerate(f_in):
        if index <= start_index or index >= end_index:
          f_out.write(line)
        elif not printed:
          for o in dirtree:
            f_out.write(o)
          printed = True
  outfpath.unlink() # missing_ok=True
  outfpath_temp.rename(outfpath)
