from django.test import (
    Client,
)
import pytest

from books.models import (
    Book,
)


@pytest.fixture
def book():
    book = Book.objects.create(
        title='Eryk',
        author='Terry Pratchett',
    )
    return book


@pytest.fixture
def books():
    Book.objects.create(
        title='Wiedźmin',
        author='Andrzej Sapkowksi',
        published_date='2020-10-10',
        language='pl',
        isbn_number='2463452753'
    )
    Book.objects.create(
        title='Wiedźmikołaj',
        author='Terry Pratchett',
        language='pl',
    )
    b = Book.objects.create(
        title='Wiedźmin',
        author='Andrzej Sapkowksi',
        published_date='2020-10-10',
        language='pl',
        isbn_number='2463452753',
    )
    Book.objects.create(
        title='Złodziej czasu',
        author='Terry Pratchett',
        published_date='2020-10-10',
        language='en',
        isbn_number='9788374695763',
        page_count=318,
        image_link='http://books.google.com/books/'
                   'content?id=2LjcIAAACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api'
    )

    return Book.objects.all()


@pytest.fixture
def client():
    return Client()
