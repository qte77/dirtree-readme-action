# dirtree-readme-action

Copy directory tree into file, e.g. README.md, instead of manual effort.

![Version](https://img.shields.io/badge/version-0.2.1-8A2BE2)
[![CodeQL](https://github.com/qte77/dirtree-readme-action/actions/workflows/codeql.yaml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/codeql.yaml)
[![CodeFactor](https://www.codefactor.io/repository/github/qte77/dirtree-readme-action/badge)](https://www.codefactor.io/repository/github/qte77/dirtree-readme-action)
[![test-dirtree-readme-action](https://github.com/qte77/dirtree-readme-action/actions/workflows/test-dirtree-readme-action.yaml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/test-dirtree-readme-action.yaml)
[![ruff](https://github.com/qte77/dirtree-readme-action/actions/workflows/ruff.yaml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/ruff.yaml)
<!--
[![pytest](https://github.com/qte77/dirtree-readme-action/actions/workflows/pytest.yaml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/pytest.yaml)
-->
[![Link Checker](https://github.com/qte77/dirtree-readme-action/actions/workflows/links-fail-fast.yaml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/links-fail-fast.yaml)
[![Deploy Docs](https://github.com/qte77/dirtree-readme-action/actions/workflows/generate-deploy-mkdocs-ghpages.yaml/badge.svg)](https://github.com/qte77/dirtree-readme-action/actions/workflows/generate-deploy-mkdocs-ghpages.yaml)
[![vscode.dev](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=vscode.dev&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://vscode.dev/github/qte77/dirtree-readme-action)

## Status

(DRAFT) (WIP) ----> Not fully implemented yet

For version history have a look at the [CHANGELOG](CHANGELOG.md).

## Sample output using this project

<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->
```sh
2025-01-01 23:27:29.737265+00:00
├── src
│ ├── app.py
│ └── utils.py
├── action.yaml
├── CHANGELOG.md
├── Dockerfile
├── LICENSE.md
├── mkdocs.yaml
├── pyproject.toml
├── README.md
└── uv.lock
```
<!-- DIRTREE-README-ACTION-INSERT-HERE-END -->

## Action environment variables

| Name | Default |
| - | - |
| `APP` | `app/app.py` |
| `CMD_HIGHLIGHT` | `sh` |
| `EXCLUDE` | `.git\|.github\|.gitignore\|.gitmessage # separated by \|` |
| `GH_EMAIL` | `action@github.com` |
| `GH_NAME` | `GitHub Action` |
| `INSERT_HERE_START_STRING` | `<!-- <!-- DIRTREE-README-ACTION-INSERT-HERE-START -->` |
| `INSERT_HERE_END_STRING` | `<!-- <!-- DIRTREE-README-ACTION-INSERT-HEREEND -->` |
| `OUT_FILE` | `README.md` |
| `PY_VER` | `3.12` |

