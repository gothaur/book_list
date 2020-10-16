import requests


def get_book(
        title='',
        author='',
        publisher='',
        subject='',
        isbn='',
        lccn='',
        oclc=''
):
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
        book_list.append(book['volumeInfo'])
    return book_list
