from github import (
  ContentFile,
  Github,
  GithubException,
  InputGitAuthor,
  Repository
)
from os import getenv
from pathlib import Path
from utils import (
  get_formatted_tree_output,
  get_write_positions_in_file,
  write_to_file
)
#TODO export to utils using @dataclass(slots=True)
CMD_HIGHLIGHT: str = str(getenv("CMD_HIGHLIGHT", 'sh'))
# EXCLUDE string separated by |
EXCLUDE: str = str(getenv("EXCLUDE", '.git|__pycache__'))
INSERT_HERE_START_STRING: str = str(getenv(
  "INSERT_HERE_START_STRING",
  '<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->'
))
INSERT_HERE_END_STRING: str = str(getenv(
  "INSERT_HERE_END_STRING",
  '<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->'
))
OUT_FILE: str = str(getenv("OUT_FILE", 'README.md'))
TREE_THEME: str = str(getenv("TREE_THEME", 'sh'))
USE_FROM_LOCAL_ACTION: str = str(getenv(USE_FROM_LOCAL_ACTION, "NO"))

GH_TOKEN: str | None = str(getenv("INPUT_GH_TOKEN"))
REPOSITORY: str | None = str(getenv("INPUT_REPOSITORY"))
COMMITTER_NAME: str = str(getenv("INPUT_COMMITTER_NAME", "NOT_SET"))
COMMITTER_EMAIL: str = str(getenv("INPUT_COMMITTER_EMAIL", "NOT_SET"))
#TODO add commit message to action.yml
COMMIT_MESSAGE: str = f"Added dirtree to {OUT_FILE}"

exclude_list: str = EXCLUDE.split('|')
outfpath = Path(OUT_FILE) # : Path
startpath = Path('.') # : Path

#TODO export to utils
def push_file_to_github(files: str):
    gh_connect = Github(GH_TOKEN)
    gh_repo = gh_connect.get_repo(REPOSITORY)
    gh_tree = repo.get_git_tree(sha)
      
    if COMMITTER_NAME != "NOT_SET" and COMMITTER_EMAIL != "NOT_SET":
      committer = InputGitAuthor(name=COMMITTER_NAME, email=COMMITTER_EMAIL)
    else:
      committer = None

    # https://pygithub.readthedocs.io/en/stable/github_objects/Repository.html
    # https://docs.github.com/en/rest/git#trees
    repo.create_git_commit(COMMIT_MESSAGE, gh_tree, [], committer=committer)
    repo.push()

if __name__ == "__main__":
  assert outfpath.exists(), f"{outfpath} not found. Aborting"
  assert startpath.exists(), f"{startpath} not found. Aborting"
  start_index, end_index = get_write_positions_in_file(
    outfpath, INSERT_HERE_START_STRING, INSERT_HERE_END_STRING
  )
  if isinstance(start_index, int) \
    and isinstance(end_index, int) \
    and start_index>= 0 and end_index >= 1:
    dirtree = get_formatted_tree_output(
      startpath, exclude_list, CMD_HIGHLIGHT, TREE_THEME
    )
    write_to_file(
      outfpath, dirtree, start_index, end_index
    )
    if USE_FROM_LOCAL_ACTION == "NO": 
      push_file_to_github(outfpath)
  else:
    print(
      f"Could not write file. Index error: {start_index=}, {end_index=}"
    )
