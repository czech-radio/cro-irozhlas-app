# -*- coding: utf-8 -*-

from irozhlas.scraper import * # FIXME
from irozhlas.analyser import *  # FIXME


def main():
    """
    Parse the index page content.
    """
    
    try:
        config = {"url": "https://irozhlas.cz/"}

        page = fetch_index(url=config["url"])

        save_index(page, ".")

    except Exception as ex:
        print(ex)

    # Agregate links

    links = []

    soup = BeautifulSoup(page.content, "html.parser")

    for link in soup.findAll("a", attrs={"href": re.compile(r"zpravy-domov")}):
        links.append(f"https://irozhlas.cz{link.get('href')}")

    for link in soup.findAll("a", attrs={"href": re.compile(r"ekonomika")}):
        links.append(f"https://irozhlas.cz{link.get('href')}")

    # Fetch and cast articles from links.

    exlude = ("https://irozhlas.cz/zpravy-domov", "https://irozhlas.cz/ekonomika")
    links = filter_links(links, exclude)

    all_articles = []

    for link in links:
        try:
            all_articles.append(fetch_article_from_link(link))
        except Exception as ex:
            print(f"Error getting article: {ex}")

    for article in all_articles:
        save_article(article,"output")
        print(
            f"Title: {article._title}\nLink: {article._link}\nCategory: {article._category}\nDate: {article._created_at}\nText: {article._content}"
        )
