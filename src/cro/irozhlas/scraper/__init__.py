# -*- coding: utf-8 -*.

import re
from bs4 import BeautifulSoup
import requests

from typing import Optional
from uuid import UUID, uuid4
from datetime import date
from datetime import datetime


__all__ = tuple(["main"])


# ########################################################################### #
#                                 MODELS                                      #
# ########################################################################### #

URL = str


class Page:
    """
    The fetched HTML page.
    """

    def __init__(self, id: UUID, title: str, content: str, created_at: date):
        self._id = id
        self._title = title
        self._content = content
        self._created_at = created_at

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def content(self) -> str:
        return self._content

    @property
    def created_at(self) -> date:
        return self._created_at

    def __eq__(self, that) -> bool:
        return (that is not None) and (self.id == that.id)

    def __hash__(self) -> int:
        return hash((type(self), self.id))


class Article:
    """
    Article class
    """

    def __init__(
        self,
        id: UUID,
        title: str,
        content: str,
        created_at: date,
        link: str,
        category: str,
    ):
        self._id = id
        self._title = title
        self._content = content
        self._created_at = created_at
        self._link = link
        self._category = category

    @property
    def id(self) -> UUID:
        return self._id

    @property
    def title(self) -> str:
        return self._title

    @property
    def content(self) -> str:
        return self._content

    @property
    def created_at(self) -> date:
        return self._created_at

    def __eq__(self, that) -> bool:
        return (that is not None) and (self.id == that.id)

    def __hash__(self) -> int:
        return hash((type(self), self.id))


# ########################################################################### #
# REPOSITORY
# ########################################################################### #


class PageRepository:
    """
    The repsitory to save and load the HTML iRozhlas index pages.
    """


# #############################################################################
# [1] Fetch and save the index page.
# #############################################################################

class Scraper:
    def __init__(self, *args, **kwargs):
        ...


def fetch_index(url: URL) -> Page:
    """
    Fetch the index page.
    :raise: The `HTTPError` on no-200 status code.
    """
    result = requests.get(url)
    if not result.ok:
        raise requests.HTTPError

    return Page(
        id=uuid4(),
        title=f"irozhlas",
        content=result.content.decode("utf-8"),
        created_at=datetime.now().timestamp(),
    )


def save_index(page: Page, path: str) -> None:

    file_name = f"snapshot-{page.created_at}-{page.id}.html"

    with open(f"{path}/{file_name}", mode="w+", encoding="utf-8") as f:
        f.write(page.content)


def save_article(article: Article, path: str) -> None:
    """Save article in text form
    """

    tmp_title = strip_title(article._link)
    tmp_date = datetime.fromtimestamp(article._created_at).strftime('%Y-%m-%d')
    filename = f"{tmp_date}_{tmp_title}.txt"

    with open(f"{path}/{filename}", mode="w+", encoding="utf-8") as f:
        f.write(article._content)


def filter_links(links: list[URL], exclude: Iterable[URL]) -> list[URL]:
    """
    Filter out non-article URLs.
    """
    result = list(set([link for link in links if link not in exclude])) 
    
    return result


def strip_title(url: str) -> str:
    """
    :param url: The URL.
    """
    return (url[url.rfind("/")+1:len(url)])


def derive_title(html: str) -> str:
    """
    Get  the article machine title.
    """
    soup = BeautifulSoup(html, features="html.parser")
    
    title = soup.find("article").find("h1").get_text()
    title = title.replace("\n", "")
    title = title.replace("  ", "")

    return title


def derive_category(url: str) -> Optional[str]:
    if url.find("ekonomika") > 0:
        return "Ekonomika"

    if url.find("zpravy-domov") > 0:
        return "Domácí zprávy"

    return None


def parse_article_body(html: str):
    """
    Strip HTML to pure text here
    """

    soup = BeautifulSoup(html, features="html.parser")
    paragraphs = soup.find("div", {"class": "b-detail"}).find_all("p")

    fulltext = ""
    for p in paragraphs:
        fulltext = fulltext + p.get_text()

    # .get_text()
    fulltext = fulltext.replace("\n\n", " ")
    fulltext = fulltext.replace("\t", "")
    fulltext = fulltext.replace("  ", "")
    fulltext = fulltext.replace("Sdílet na Facebooku", "")
    fulltext = fulltext.replace("Sdílet na Twitteru", "")
    fulltext = fulltext.replace("Sdílet na LinkedIn", "")
    fulltext = fulltext.replace("Zavřít", "")
    fulltext = fulltext.replace("Tisknout", "")
    fulltext = fulltext.replace("Kopírovat url adresu", "")
    fulltext = fulltext.replace("Zkrácená adresa Kopírovat do schránky", "")
    fulltext = fulltext.replace(" číst článek", "")
    # article_body = article_body[article_body.find("Zavřít")+6:len(article_body)]
    return fulltext


def fetch_article_from_link(url: str) -> Article:
    """
    Calls IO/NET URL and returns Article object
    """

    result = requests.get(url)
    if not result.ok:
        raise requests.HTTPError

    return Article(
        id=uuid4(),
        title=derive_title(result.content.decode("utf-8")),
        content=parse_article_body(result.content.decode("utf-8")),
        created_at=datetime.now().timestamp(),
        link=url,
        category=derive_category(url),
    )



