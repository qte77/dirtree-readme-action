# dev-dirtree-action-temp

Copy directory tree into file, e.g. README.md, instead of manual effort.

![Version](https://img.shields.io/badge/version-v0.1.22-dev-8A2BE2)
[![CodeQL](https://github.com/pdq21/dev-dirtree-action-temp/actions/workflows/codeql.yml/badge.svg)](https://github.com/pdq21/dev-dirtree-action-temp/actions/workflows/codeql.yml)
[![CodeFactor](https://www.codefactor.io/repository/github/pdq21/dev-dirtree-action-temp/badge)](https://www.codefactor.io/repository/github/pdq21/dev-dirtree-action-temp)
[![write-dirtree-to-file](https://github.com/pdq21/dev-dirtree-action-temp/actions/workflows/write-dirtree-to-file.yml/badge.svg)](https://github.com/pdq21/dev-dirtree-action-temp/actions/workflows/write-dirtree-to-file.yml)
[![ruff](https://github.com/pdq21/dev-dirtree-action-temp/actions/workflows/ruff.yml/badge.svg)](https://github.com/pdq21/dev-dirtree-action-temp/actions/workflows/ruff.yml)
<!--
[![pytest](https://github.com/pdq21/dev-dirtree-action-temp/actions/workflows/pytest.yaml/badge.svg)](https://github.com/pdq21/dev-dirtree-action-temp/actions/workflows/pytest.yaml)
-->
[![Link Checker](https://github.com/pdq21/dev-dirtree-action-temp/actions/workflows/links-fail-fast.yaml/badge.svg)](https://github.com/pdq21/dev-dirtree-action-temp/actions/workflows/links-fail-fast.yaml)
[![Deploy Docs](https://github.com/pdq21/dev-dirtree-action-temp/actions/workflows/generate-deploy-mkdocs-ghpages.yaml/badge.svg)](https://github.com/pdq21/dev-dirtree-action-temp/actions/workflows/generate-deploy-mkdocs-ghpages.yaml)
[![vscode.dev](https://img.shields.io/static/v1?logo=visualstudiocode&label=&message=vscode.dev&labelColor=2c2c32&color=007acc&logoColor=007acc)](https://vscode.dev/github/pdq21/dev-dirtree-action-temp)

## Status

(DRAFT) (WIP) ----> Not fully implemented yet

For version history have a look at the [CHANGELOG](CHANGELOG.md).

## Sample output using this project

<!-- DIRTREE-README-ACTION-INSERT-HERE-START -->
```sh
2025-01-01 22:11:26.389545+00:00
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
