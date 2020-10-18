from django.urls import (
    reverse_lazy
)
import pytest
from books.forms import (
    AddBookForm,
    SearchBookForm,
    ImportBookForm,
)
from books.models import (
    Book
)


@pytest.mark.django_db
def test_book_model(book):
    assert Book.objects.get(
        title='Eryk'
    ) == book
    assert len(Book.objects.all()) == 1


@pytest.mark.django_db
def test_add_book_form():
    form = AddBookForm(
        data={
            'title': 'Eryk',
            'author': 'Terry Pratchett',
            'published_date': '2009'
        }
    )

    assert form.is_valid() is True

    form = AddBookForm(
        data={
            'title': 'Eryk',
            'author': 'Terry Pratchett',
            'published_date': '2009.10.10'
        }
    )

    assert form.is_valid() is False


def test_search_book_form():
    form = SearchBookForm(
        data={
            'title': 'Eryk',
        }
    )

    assert form.is_valid() is True

    form = SearchBookForm(
        data={
            'date_to': '2008-01-08',
            'date_from': '2020-10-10',
        }
    )

    assert form.is_valid() is False


@pytest.mark.parametrize(
    "key, value, result", (
        ('isbn', '', True),
        ('isbn', '1234567890', True),
        ('isbn', '1234567890123', True),
        ('isbn', '1234567890123456', False),
        ('oclc', 'ocm12345678', True),
        ('oclc', 'ocn123456789', True),
        ('oclc', 'on1234567890123', True),
        ('oclc', '', True),
        ('oclc', '1234567890123456', False)
    )
)
def test_import_book_form(key, value, result):
    assert ImportBookForm(
        data={
            key: value
        }
    ).is_valid() == result


@pytest.mark.django_db
def test_create_view(client):
    book = {
        'title': 'produkt 1',
        'author': 'opis pierwszego produktu',
        'page_count': 25
    }
    response = client.get(reverse_lazy('books:add-book'))
    assert response.status_code == 200
    response = client.post(reverse_lazy('books:add-book'), book)
    assert response.status_code == 302


@pytest.mark.django_db
def test_list_vew(client, books):
    url = reverse_lazy('books:book-list')
    response = client.get(
        url,
        {
            'books': books,
        }
    )
    assert response.status_code == 200
    assert len(response.context['books']) == 4
    assert response.context['books'][0] == books[0]
    assert response.context['books'][1] == books[1]
    assert response.context['books'][2] == books[2]
