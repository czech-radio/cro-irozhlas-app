# -*- coding: utf-8 -*-

from uuid import uuid4

from irozhlas_scraper.scraping import Page


def test_create_page():
    # arrange
    # act
    # assert

    page = Page(
        id=uuid4(),
        title="Title",
        content="content",
        created_at="2021",
    )

    assert page.title == "Title"
    assert page.content == "content"


def test_that_pages_with_same_id_are_equal():
    uid = uuid4()
    lhs = Page(
        id=uid,
        title="Title",
        content="content",
        created_at="2021",
    )
    rhs = Page(
        id=uid,
        title="Title",
        content="content",
        created_at="2021",
    )

    assert lhs == rhs


def test_that_same_pages_has_same_hash():
    uid = uuid4()
    lhs = Page(
        id=uid,
        title="Title",
        content="content",
        created_at="2021",
    )
    rhs = Page(
        id=uid,
        title="Title",
        content="content",
        created_at="2021",
    )
    assert hash(lhs) == hash(rhs)
