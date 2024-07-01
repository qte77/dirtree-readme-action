# dirtree-readme-action

Copy directory tree into file, e.g. README.md, instead of manual effort.

[![write-dirtree-to-file](https://github.com/qte77/dirtree-readme-action/actions/workflows/write-dirtree-to-file.yml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/write-dirtree-to-file.yml)
[![Ruff](https://github.com/qte77/dirtree-readme-action/actions/workflows/ruff.yml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/ruff.yml)
[![CodeQL](https://github.com/qte77/dirtree-readme-action/actions/workflows/codeql.yml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/codeql.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/qte77/dirtree-readme-action/badge)](https://www.codefactor.io/repository/github/qte77/dirtree-readme-action)

## Sample output using this project

<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->
```sh
2024-07-01 02:27:11.968021+00:00
├── app
│   ├── utils.py
│   └── app.py
├── data
│   ├── dummy-dirtree-python.md
│   └── dummy-readme.md
├── README.md
├── .gitignore
├── LICENSE
└── .github
    ├── dependabot.yml
    └── workflows
        ├── ruff.yml
        ├── write-dirtree-to-file.yml
        └── codeql.yml
```
<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->

## Action environment variables

| Name | Default |
| - | - |
| APP | 'app/app.py' |
| CMD_HIGHLIGHT | 'sh' |
| EXCLUDE | '.git\|\_\_pycache\_\_' # separated by \| |
| GH_EMAIL | 'action@github.com' |
| GH_NAME | 'GitHub Action' |
| INSERT_HERE_START_STRING | '<\!-- DIRTREE-README-ACTION-INSERT-HERE-START -->' |
| INSERT_HERE_END_STRING | '<\!-- DIRTREE-README-ACTION-INSERT-HERE-END -->' |
| OUT_FILE | 'data/dummy-readme.md' |
| PY_VER | '3.10' |
| TREE_THEME | 'sh' |
