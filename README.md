# dirtree-readme-action

Copy directory tree into file, e.g. README.md, instead of manual effort.

[![write-dirtree-to-file](https://github.com/qte77/dirtree-readme-action/actions/workflows/write-dirtree-to-file.yml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/write-dirtree-to-file.yml)
[![Ruff](https://github.com/qte77/dirtree-readme-action/actions/workflows/ruff.yml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/ruff.yml)
[![CodeQL](https://github.com/qte77/dirtree-readme-action/actions/workflows/codeql.yml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/codeql.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/qte77/dirtree-readme-action/badge)](https://www.codefactor.io/repository/github/qte77/dirtree-readme-action)

## Sample output using this project

<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->
<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->

## Action environment variables

App environment variables can be set in the action but not vice-versa.

### App

| Name | Default |
| - | - |
| CMD_HIGHLIGHT | 'sh' |
| EXCLUDE | '.git\|\_\_pycache\_\_' # separated by \| |
| INSERT_HERE_START_STRING | '<\!-- DIRTREE-README-ACTION-INSERT-HERE-START -->' |
| INSERT_HERE_END_STRING | '<\!-- DIRTREE-README-ACTION-INSERT-HERE-END -->' |
| OUT_FILE | 'data/dummy-readme.md' |

### Action

| Name | Default |
| - | - |
| APP | 'app/app.py' |
| GH_EMAIL | 'action@github.com' |
| GH_NAME | 'GitHub Action' |
| PY_VER | '3.10' |
