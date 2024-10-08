# dirtree-readme-action

Copy directory tree into file, e.g. README.md, instead of manual effort.

[![write-dirtree-to-file](https://github.com/qte77/dirtree-readme-action/actions/workflows/write-dirtree-to-file.yml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/write-dirtree-to-file.yml)
[![Ruff](https://github.com/qte77/dirtree-readme-action/actions/workflows/ruff.yml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/ruff.yml)
[![CodeQL](https://github.com/qte77/dirtree-readme-action/actions/workflows/codeql.yml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/codeql.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/qte77/dirtree-readme-action/badge)](https://www.codefactor.io/repository/github/qte77/dirtree-readme-action)

## Sample output using this project

<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->
```sh
2024-09-01 20:21:39.843036+00:00
├── LICENSE
├── README.md
├── data
│   ├── dummy-dirtree-python.md
│   └── dummy-readme.md
├── .gitignore
├── app
│   ├── utils.py
│   └── app.py
└── .github
    ├── dependabot.yml
    └── workflows
        ├── write-dirtree-to-file.yml
        ├── codeql.yml
        └── ruff.yml
```
<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->

## Action environment variables

| Name | Default |
| - | - |
| `APP` | `app/app.py` |
| `CMD_HIGHLIGHT` | `sh` |
| `EXCLUDE` | `.git\|__pycache__ # separated by \|` |
| `GH_EMAIL` | `action@github.com` |
| `GH_NAME` | `GitHub Action` |
| `INSERT_HERE_START_STRING` | `<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->` |
| `INSERT_HERE_END_STRING` | `<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->` |
| `OUT_FILE` | `data/dummy-readme.md` |
| `PY_VER` | `3.10` |