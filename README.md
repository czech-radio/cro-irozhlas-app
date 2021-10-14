# Python Package Template

**This is a basic template repository for your Python projects.**

![main](https://github.com/groundf/Template-Python-Package/workflows/main/badge.svg) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[Ubuntu | macOS | Windows]

## Description

Python packaging is not easy for newcomers so I wrote this template and example for you!

### Features

- [x] Use GitHub Actions.
- [ ] Lint with flake8 on push or pull request to main branch
- [x] Test with pytest on push or pull request to main branch
- [x] Test for multiple Python versions
- [x] Test for multiple operation systems.
- [ ] Use argparse and proper help system.
- [x] Use container (Docker) for console app.
- [x] Run tests and lints on every push or pull request to `main`.
- [x] Contains the `README.md` file.
- [x] Contains the build status icon (badge) in README.
- [x] Contains the `LICENSE.txt` file.
- [x] Contains the `.gitignore` file.
- [x] Contains the `.dockerignore` file.
- [x] Contains the `.editorconfig` file.
- [x] Configure the `pytest` in `setup.cfg`.
- [ ] Contains the precommit-hooks.
- [ ] Build container on every tag on `main`.
- [x] Use the `setup.cfg` instead of `setup.py`
- [x] Place the source files in `src` folder.
- [x] Place the test files in `tests` folder.

## Installation

Go to project directory `cd path/to/project` and create a virtual environment (Always use virtual environment!). You can create a virtual environment anywhere, but I prefer to keep it inside the project folder.

Windows
```powershell
py -3.9 -m venv .venv
```
Unix
```bash
python -m venv .venv
```

Activate the virtual environment.

Windows
```powertshell
.venv\Scripts\activate
```

Unix
```bash
source venv/bin/activate
```

Install all dependecies in editable mode.

```shell
pip install ".[lint, test, docs]"
pytest
```

### Docker

```shell
docker build -f .docker/Dockerfile -t <image-name>:<image-version> .
```
e.g

```shell
docker build -f .docker/Dockerfile -t program:latest .
```

## Usage

```shell
program 100
100%|█████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████████| 100/100 [00:10<00:00,  9.11it/s]
It works!
```

or

```shell
docker run --rm program 100
100%|██████████| 100/100 [00:10<00:00,  9.91it/s]
It works!
```

## Question/Answers

- __Q__: Is this README finsihed?

  __A__: No, I will write more precise instructions as soon as possible.

- __Q__: Why this is not a coockicutter template?

  __A__: The coockicutter template cannot be properly build with actions, because the jinja `{{...}}` templating is not valid name for namespace or package. The solution shoudl be to create a coockicutter template and generated projetc as a separate repositories but I still prefer to quickly clone and use the template repository and change some names here and there. But it can change in the furure (BTW Horrible long name (coockicutter) for use from command line.)

- __Q__: How to remove namespace when I don't want to use it.

  __A__: Remove namespace folder and in `setup.cfg`, replace `packages = find_namespace` by `packages = find` and remove `namespace.` when used somewhere.

- __Q__: Why there are all these `setup.py`, `setup.cfg`, `pyproject.toml`?

  __A__: OK, this is little bit complicated. In the future I hope that `pyproject.toml` will only be here but at this moment, this solution is not full faetured and so I use declarative `setup.cfg` with companion `setup.py` which is only needed for editable mode e.g. see https://snarky.ca/what-the-heck-is-pyproject-toml. The `pyproject.toml` is actually commented out and not used.


## Resources

- https://packaging.python.org
- https://setuptools.readthedocs.io
- https://python-packaging.readthedocs.io