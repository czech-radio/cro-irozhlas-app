# -*- cofding: utf-8 -*.

import re
import urllib
from bs4 import BeautifulSoup

from irozhlas_scraper import main
import requests

def main():
    page = requests.get("https://irozhlas.cz/")
    soup = BeautifulSoup(page.content, 'html.parser')
    clanky = []

    for link in soup.findAll('a', attrs={'href': re.compile(r"zpravy-domov")}):

        print(link.get('href'))
        clanky.append(link.get('href'))


if __name__ == "__main__":
    main()
