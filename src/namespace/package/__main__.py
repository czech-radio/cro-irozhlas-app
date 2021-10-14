# -*- cofding: utf-8 -*.

from namespace.package import main
import requests
from bs4 import BeatifulSoup

def main():
    page = requests.get("https://irozhlas.cz/")
    # soup = BeatifulSoup(page.content, 'html.parser')
    print(page.text)

if __name__ == "__main__":
    main()
