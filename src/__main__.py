# -*- cofding: utf-8 -*.

from namespace.package import main
import requests
from bs4 import BeautifulSoup
import urllib
import re

def main():
    page = requests.get("https://irozhlas.cz/")
    soup = BeautifulSoup(page.content, 'html.parser')
    clanky = []

    for link in soup.findAll('a', attrs={'href': re.compile(r"zpravy-domov")}):

        print(link.get('href'))
        clanky.append(link.get('href'))
    # print(soup.body)

if __name__ == "__main__":
    main()
