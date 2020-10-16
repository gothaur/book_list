import requests


def get_book(title='', author='', publisher='', subject='', isbn='', lccn='', oclc=''):

    url = f'https://www.googleapis.com/books/v1/volumes?q='
    if title:
        url += f'intitle:{title}+'
    if author:
        url += f'inauthor:{author}+'
    if publisher:
        url += f'inpublisher:{publisher}+'
    if subject:
        url += f'subject:{subject}+'
    if isbn:
        url += f'isbn:{isbn}+'
    if lccn:
        url += f'lccn:{lccn}+'
    if oclc:
        url += f'oclc:{oclc}+'

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
