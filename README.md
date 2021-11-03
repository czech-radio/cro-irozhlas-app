# irozhlas_scraper

**Simple projects one-line description.**

![main](https://github.com/groundf/Template-Python-Package/workflows/main/badge.svg) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[Ubuntu | macOS | Windows]

## Description

[TODO]

### Features

[TODO]

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
