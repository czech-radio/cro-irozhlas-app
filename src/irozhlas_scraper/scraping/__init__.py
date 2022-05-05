# -*- coding: utf-8 -*.

import re
from bs4 import BeautifulSoup
import requests

from uuid import UUID, uuid4
from datetime import date
from datetime import datetime


__all__ = tuple(["main"])


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


# #############################################################################
# [1] Fetch and save the index page.
# #############################################################################


def fetch_index(url: str) -> Page:
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


def derive_title(text: str) -> str:
    """Replace common patterns to create title of an Article"""
    text.replace("https://irozhlas.czhttps://www.irozhlas.cz", "https://irozhlas.cz")
    text.replace("https://irozhlas.cz/", "")
    text.replace("_", " ")
    text.replace("-", " ")
    text.replace("ekonomika/", "")
    return text


def parse_article_body(text: str):
    return text


def fetch_article_from_link(url: str) -> Article:
    """
    Calls IO/NET URL and returns Article object
    """

    result = requests.get(url)
    if not result.ok:
        raise requests.HTTPError

    return Article(
        id=uuid4(),
        title=derive_title(url),
        content=result.content.decode("utf-8"),
        created_at=datetime.now().timestamp(),
        link=url,
        category="testcategory",
    )


class IndexContentStore:
    """
    The repsitory class to save and load the HTML irozhlas index pages.
    """

    def __init__(self):
        ...

    def save(self, meta) -> None:
        ...

    def load(self) -> str:
        ...


# #############################################################################
# [2] Parse the index page content.
# #############################################################################


def main():
    try:
        config = {"url": "https://irozhlas.cz/"}

        page = fetch_index(url=config["url"])

        save_index(page, ".")

    except Exception as ex:
        print(ex)

    ### agregate links ###

    links = []

    soup = BeautifulSoup(page.content, "html.parser")

    for link in soup.findAll("a", attrs={"href": re.compile(r"zpravy-domov")}):
        links.append(f"https://irozhlas.cz{link.get('href')}")

    for link in soup.findAll("a", attrs={"href": re.compile(r"ekonomika")}):
        links.append(f"https://irozhlas.cz{link.get('href')}")

    all_articles = []

    for link in links:
        try:
            all_articles.append(fetch_article_from_link(link))
        except Exception as ex:
            print(f"Error getting article: {ex}")

    print(all_articles)
