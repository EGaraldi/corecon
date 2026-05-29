# Repository Guidelines

## Project Structure & Module Organization
`corecon/` contains the Python package, with public classes such as `FieldClass.py` and `DataEntryClass.py`, helpers in `loaders.py` and `InternalFunctions.py`, and bundled datasets under `corecon/data/`. New constraint entries are usually added as one file per paper inside the matching field directory, for example `corecon/data/HII_fraction/`. Tests live in `tests/`. Documentation is built from `docs/`, with generated field pages in `docs/datarst/` and plotting scripts in `docs/plots/`.

## Build, Test, and Development Commands
Use a local virtual environment and install from the repository root:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e .
pip install -r requirements.txt pytest
```

Run the test suite with `pytest --disable-pytest-warnings tests`. Build documentation with `make -C docs html`. Refresh generated docs content with `make -C docs datarst`, and regenerate interactive plots with `make -C docs plots`.

## Coding Style & Naming Conventions
Follow the existing Python style: 4-space indentation, module-level imports, and descriptive snake_case for functions and variables. Class files use the repository’s established CamelCase filenames such as `FieldClass.py`. Data-entry modules follow the paper naming pattern `Author_et_al_YYYY.py`. Keep new dataset files aligned with `corecon/data/data_entry_template.py`, including metadata fields, axes, values, and error arrays.

## Testing Guidelines
Tests use `pytest` and are named `test_*.py` under `tests/`. Add focused tests alongside the affected API, especially when changing field loading, aliases, or `DataEntry` behavior. Prefer assertions that tolerate dataset growth where appropriate, as seen in `tests/test_corecon.py`, instead of hard-coding the full catalog.

## Commit & Pull Request Guidelines
Recent history uses short, imperative commit subjects such as `update docs`, `new constraints`, and `modernize package deployment`. Keep commit titles concise and action-oriented. Pull requests should explain the scientific or code change, list affected fields or files, and note any documentation or test updates. Include screenshots only when documentation plots or rendered pages change.

## Documentation & Data Updates
If you add or revise constraints, update the corresponding docs pages and regenerate derived artifacts before opening a PR. Keep generated content in sync with the package data so docs, tests, and shipped datasets remain consistent.
