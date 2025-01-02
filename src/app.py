"""
This module contains the main script for the dirtree-readme-action, which generates
and writes a directory tree to a specified file, typically README.md. It uses GitHub
API to push changes back to the repository if not running from a local action.

Key functionalities:
- Reads environment variables for configuration.
- Generates a formatted directory tree.
- Writes the tree to a file between specified markers.
- Optionally pushes changes to GitHub if not running locally.

Environment Variables:
- CMD_HIGHLIGHT: Syntax highlighting language for the tree output.
- EXCLUDE: Directories or files to exclude from the tree.
- INSERT_HERE_START_STRING: Start marker for tree insertion in the file.
- INSERT_HERE_END_STRING: End marker for tree insertion in the file.
- OUT_FILE: The file to write the directory tree to.
- TREE_THEME: Theme for the tree structure.
- USE_FROM_LOCAL_ACTION: Flag to determine if the action is running locally.
- GH_TOKEN: GitHub token for authentication.
- REPOSITORY: GitHub repository name.
- COMMITTER_NAME: Name of the committer for the commit.
- COMMITTER_EMAIL: Email of the committer for the commit.

Functions:
- push_file_to_github(files: str) -> None: Pushes the updated file to GitHub.

Main Execution:
- Checks for the existence of the output file and start path.
- Generates and writes the directory tree to the specified file.
- Pushes changes to GitHub if not running locally.
"""

from logging import (
    basicConfig,
    getLogger,
    INFO,
    error,
    exception
)
from os import getenv
from pathlib import Path
from typing import Optional
from utils import (
    get_formatted_tree_output,
    get_write_positions_in_file,
    write_to_file
)

basicConfig(level=INFO)
logger = getLogger(__name__)

CMD_HIGHLIGHT: str = str(getenv("CMD_HIGHLIGHT", 'sh'))
EXCLUDE: str = str(getenv("EXCLUDE", '.git|.github|.gitignore|.gitmessage'))
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
USE_FROM_LOCAL_ACTION: str = str(getenv("USE_FROM_LOCAL_ACTION", "NO"))
GH_TOKEN: Optional[str] = str(getenv("INPUT_GH_TOKEN"))
REPOSITORY: Optional[str] = str(getenv("INPUT_REPOSITORY"))
COMMITTER_NAME: str = str(getenv("INPUT_COMMITTER_NAME", "NOT_SET"))
COMMITTER_EMAIL: str = str(getenv("INPUT_COMMITTER_EMAIL", "NOT_SET"))
COMMIT_MESSAGE: str = f"Added dirtree to {OUT_FILE}"

exclude_list: list[str] = EXCLUDE.split('|')
outfpath: Path = Path(OUT_FILE)
startpath: Path = Path('.')


if __name__ == "__main__":
    """
    Main execution block to generate and write directory tree to README.md.
    
    This block:
    - Checks if the output file and start path exist.
    - Generates the directory tree.
    - Writes the tree to the specified file.
    - Optionally pushes the updated file to GitHub.
    """

    try:
        assert outfpath.exists(), f"{outfpath} not found. Aborting"
        assert startpath.exists(), f"{startpath} not found. Aborting"

        start_index, end_index = get_write_positions_in_file(
            outfpath, INSERT_HERE_START_STRING, INSERT_HERE_END_STRING
        )
        if isinstance(start_index, int) \
           and isinstance(end_index, int) \
           and start_index >= 0 and end_index >= 1:
            dirtree = get_formatted_tree_output(
                startpath, exclude_list, CMD_HIGHLIGHT, TREE_THEME
            )
            write_to_file(
                outfpath, dirtree, start_index, end_index
            )
        else:
            error(
            	f"Could not write file. Index error: {start_index=}, {end_index=}"
            )
    except Exception as e:
        exception(f"An error occurred: {e}")
