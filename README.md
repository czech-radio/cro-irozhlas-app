# irozhlas_scraper

**The iRozhlas scraping service.**

![main](https://github.com/czech-radio/irozhlas-scraper/workflows/main/badge.svg) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[Ubuntu | macOS | Windows]

## Requirements

Write a program which downloads and process the content of iRozhlas web page.

The program should be accessible from command line with apropriate interface e.g

    irozhlas --output <output-path> --format <e.g json|text> ...

At this moment we think that the project can be splited into two parts (modules/packages).

1. Scraper
2. Analyzer

#### Usage

You need an Geenea API key. Set the value of `GENEEA_KEY` environment variable!

    irozhlas-analyse

## Documentation

Here we write notes about our solution. What works and why? Don't hesitate to change the requirements alongside with this section.

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
