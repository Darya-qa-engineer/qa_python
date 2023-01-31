import pytest

from book_collector import BooksCollector
from test_util import TestConst


@pytest.fixture
def books(collector):
    collector.add_new_book(TestConst.Book1)
    collector.add_new_book(TestConst.Book2)
    collector.add_new_book(TestConst.Book3)
    return collector


@pytest.fixture
def collector():
    collector = BooksCollector()
    return collector
