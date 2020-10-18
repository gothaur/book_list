from django.test import (
    Client,
)
import pytest

from books.models import (
    Author,
    Book,
)


@pytest.fixture
def terry_pratchett():
    new_author = Author.objects.create(
        name='Terry Pratchett'
    )
    return new_author


@pytest.fixture
def andrzej_sapkowski():
    new_author = Author.objects.create(
        name='Andrzej Sapkowski'
    )
    return new_author


@pytest.fixture
def book(terry_pratchett):
    book = Book.objects.create(
        title='Eryk',
    )
    book.author.add(terry_pratchett)
    return book


@pytest.fixture
def books(andrzej_sapkowski, terry_pratchett):
    b1 = Book.objects.create(
        title='Wiedźmin',
        published_date='2020-10-10',
        language='pl',
        isbn_number='2463452753'
    )
    b1.author.set([terry_pratchett])
    b1.save()

    b2 = Book.objects.create(
        title='Wiedźmikołaj',
        language='pl',
    )
    b2.author.set([terry_pratchett])
    b2.save()

    b3 = Book.objects.create(
        title='Wiedźmin',
        published_date='2020-10-10',
        language='pl',
        isbn_number='2463452753',
    )

    b3.author.set([andrzej_sapkowski])
    b3.save()

    b4 = Book.objects.create(
        title='Złodziej czasu',
        published_date='2020-10-10',
        language='en',
        isbn_number='9788374695763',
        page_count=318,
        image_link='http://books.google.com/books/'
                   'content?id=2LjcIAAACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api'
    )
    b4.author.set([terry_pratchett])
    b4.save()

    return Book.objects.all()


@pytest.fixture
def client():
    return Client()
