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


def fetch_article_from_link(url: str) -> Article:
    result = requests.get(url)
    if not result.ok:
        raise requests.HTTPError

    return Article(
        id=uuid4(),
        title=f"{url.replace('https://irozhlas.cz/','').replace('_',' ').replace('-',' ').replace('ekonomika/','')}",
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

    articles = []

    soup = BeautifulSoup(page.content, "html.parser")
    for link in soup.findAll("a", attrs={"href": re.compile(r"zpravy-domov")}):
        articles.append(f"https://irozhlas.cz{link.get('href')}")

    for link in soup.findAll("a", attrs={"href": re.compile(r"ekonomika")}):
        articles.append(f"https://irozhlas.cz{link.get('href')}")

    ### make the list unique
    uniq_links = list(set(articles))

    ### fix some typo
    filtered = []
    for article in uniq_links:
        print(article)
        filtered.append(
            article.replace(
                "https://irozhlas.czhttps://www.irozhlas.cz", "https://irozhlas.cz"
            )
        )

    # print(uniq_links)

    all_articles = []

    for link in filtered:
        all_articles.append(fetch_article_from_link(link))

    for article in all_articles:
        print(f"{article.title},{article.content}")
