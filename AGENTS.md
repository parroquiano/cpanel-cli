# Repository Guidelines

## Project Structure & Module Organization

Application code lives in `cpanel/`. `cli.py` parses options and configuration, `core.py` wraps the cPanel API client, and `dispatcher.py` routes commands to modules under `cpanel/caller/`. Shared helpers belong in `util.py`. Keep command help in `cpanel/USAGE` and `cpanel/REFERENCE`.

Tests are under `test/`: `test_core.py` contains isolated unit tests, while `test_uapi.py` exercises a live cPanel server. Sphinx sources live in `doc/`, images in `doc/_static/`, and Spanish catalogs in `doc/locale/es/`. Do not hand-edit `doc/reference.rst` or `doc/reference/*.rst`; `doc/reference.sh` generates them.

## Build, Test, and Development Commands

- `make venv` creates `venv/` and installs development dependencies.
- `make typecheck` runs Pyright across application and test code.
- `PYTHONPATH=. ./venv/bin/python -m unittest discover -v -s test -p 'test_core.py'` runs isolated tests without server credentials.
- `make test` builds the package and runs the full tox suite. It requires `test/cpanelrc.test`.
- `make package` creates wheel and source distributions in `dist/`.
- `make doc` builds English and translated Sphinx documentation.
- `make clean` removes generated environments, builds, caches, and distributions.

## Coding Style & Naming Conventions

Target Python 3.11 or later. Follow `.editorconfig`: UTF-8, LF endings, final newlines, and tabs displayed at four columns. Preserve the existing typed style and run `make typecheck` before submission. Use `snake_case` for functions, variables, and modules; `PascalCase` for classes; and `UPPER_CASE` for constants. Name test methods `test_<behavior>`.

## Testing Guidelines

Tests use Python's `unittest` framework through tox on Python 3.11 and 3.12. Add focused unit tests for local logic and live tests only when API interaction is essential. No formal coverage threshold is configured. Copy `test/cpanelrc.test.example` locally for integration tests; never commit hostnames, usernames, or API tokens.

## Commit & Pull Request Guidelines

Use short, imperative commit subjects consistent with history, such as `Fix upload response error handling` or `Update contributing guide`. Keep commits focused. Every commit must end with a blank line followed by `Co-authored-by: Codex <noreply@openai.com>`.

Pull requests should explain the behavior change, identify affected commands, link relevant issues, and list verification performed. Update help text, generated command references, tests, and translations when applicable.
