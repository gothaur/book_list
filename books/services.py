import requests


def url_query_string(title='', author='', publisher='', subject='', isbn='', lccn='', oclc=''):
    path_part = {
        'intitle:': title,
        'inauthor:': author,
        'inpublisher:': publisher,
        'subject:': subject,
        'isbn:': isbn,
        'lccn:': lccn,
        'oclc:': oclc,
    }
    url = 'https://www.googleapis.com/books/v1/volumes?q='
    query_string = ''

    for key, value in path_part.items():
        if value != '':
            query_string += f'{key}{value}+'
    url += query_string.rstrip('+')
    return url


def get_book(title='', author='', publisher='', subject='', isbn='', lccn='', oclc=''):

    url = url_query_string(title, author, publisher, subject, isbn, lccn, oclc)

    r = requests.get(url)
    books = r.json()
    book_list = []

    for book in books['items']:
        isbn_list = book['volumeInfo'].get('industryIdentifiers', [])
        industry_identifiers = [
            isbn['identifier'] for isbn in isbn_list if isbn['type'] == 'ISBN_13'
        ]
        book_dict = {
            'title': book['volumeInfo'].get('title', ''),
            'authors': book['volumeInfo'].get('authors', ''),
            'publishedDate': book['volumeInfo'].get('publishedDate', ''),
            'pageCount': book['volumeInfo'].get('pageCount', ''),
            'publisher': book['volumeInfo'].get('publisher', ''),
            'imageLinks': book['volumeInfo'].get('imageLinks', {}).get('smallThumbnail', ''),
            'language': book['volumeInfo'].get('language', ''),
            'industryIdentifiers': industry_identifiers[0] if len(industry_identifiers) > 0 else '',
        }
        book_list.append(book_dict.copy())

    return book_list
