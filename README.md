# dirtree-readme-action

Copy directory tree into file, e.g. README.md, instead of manual effort.

[![write-dirtree-to-file](https://github.com/qte77/dirtree-readme-action/actions/workflows/write-dirtree-to-file.yml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/write-dirtree-to-file.yml)
[![Ruff](https://github.com/qte77/dirtree-readme-action/actions/workflows/ruff.yml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/ruff.yml)
[![CodeQL](https://github.com/qte77/dirtree-readme-action/actions/workflows/codeql.yml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/codeql.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/qte77/dirtree-readme-action/badge)](https://www.codefactor.io/repository/github/qte77/dirtree-readme-action)

## Action Environment Variables 

| Name | Default |
| - | - |
| APP | 'app/app.py' |
| PY_VER | '3.10' |
| OUT_FILE | 'data/dummy-readme.md' |
| EXCLUDE | '.git\|\_\_pycache\_\_' # separated by \| |
| CMD_HIGHLIGHT | 'sh' |
| INSERT_HERE_START_STRING | '<\!-- DIRTREE-README-ACTION-INSERT-HERE-START -->' |
| INSERT_HERE_END_STRING | '<\!-- DIRTREE-README-ACTION-INSERT-HERE-END -->' |
