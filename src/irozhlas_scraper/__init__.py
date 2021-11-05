# -*- cofding: utf-8 -*.

from os import PathLike
import re
from bs4 import BeautifulSoup
import requests

from uuid import UUID, uuid4
from datetime import date
from datetime import datetime
from pathlib import Path


__version__ = "0.2.0"

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

    def __init__(self,id: UUID, title: str, content: str, created_at: date, link: str, category: str):
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
        created_at=datetime.now().timestamp(),  # Chceme timestamp?
    )


def save_index(page: Page, path: str) -> None:

    file_name = f"snapshot-{page.created_at}-{page.id}.html"

    with open(f"{path}/{file_name}", mode="w+", encoding="utf-8") as f:
        f.write(page.content)


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

    soup = BeautifulSoup(page.content, 'html.parser')
    for link in soup.findAll('a', attrs={'href': re.compile(r"zpravy-domov")}):
         articles.append(f"https://irozhlas.cz/{link.get('href')}" )

    for link in soup.findAll('a', attrs={'href': re.compile(r"ekonomika")}):
         articles.append(f"https://irozhlas.cz{link.get('href')}")

    uniq_links = list(set(articles))
    print(uniq_links)
