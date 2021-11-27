# iRozhlas Scraper and Analyser

_The iRozhlas scraping and analusin service._

![main](https://github.com/czech-radio/irozhlas-scraper/workflows/main/badge.svg) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Tested on latest Ubuntu and Windows OS.

### Features

(Here we write notes about our solution. What works and why? Don't hesitate to change the requirements alongside with this section.)

Write a program which downloads and process the content of iRozhlas web page.
The program should be accessible from command line with apropriate interface e.g

    irozhlas --output <output-path> --format <e.g json|text> ...

At this moment we think that the project can be splited into two parts (modules/packages) where every
package can be viwed and used as a standalone application. They are currently executed vis scripts (see `setup.cfg`).

- `scraping` The scraping package (module) is responsible for fetching, parsing and storing the irozhlas.cz pages such as index page and individual articles found on index page.
- `analysis` The analysis package (module) is responsible for posting the stored articles to Geneea service, processing and storing the results in database.
- `website` The web application for managing and viewing the analysed articles.

## Usage

(You need a Geenea API key. Set the value of `GENEEA_KEY` environment variable!)

    irozhlas-scrape ...
    irozhlas-analyse ...

## Setup

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

#### Build

```shell
docker build -f .docker/Dockerfile -t <image-name>:<image-version> .
```
e.g

```shell
docker build -f .docker/Dockerfile -t program:latest .
```

#### Usage

...
