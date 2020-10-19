# Praca z książkami

## Wyszukiwanie książek w bazie

Książek można wyszukiwać wysyłając zapytanie metodą GET wg następującego klucza:

```
https://lista-ksiazek.herokuapp.com/api/books/?key=value
```

to zapytanie wymaga conajmniej jednego z parametrów:

* title= zwraca wyniki, w których wpisany tekst znajduje się w tytule
* author= zwraca wyniki, w których dane autora zawierają wpisany tekst
* laguage= zwraca wyniki, w których wpisany tekst znajduje się w języku publikacji
* date_from= zwraca wyniki, w których data publikacji jest większa od wpisanej
* date_to= zwraca wyniki, w których data publikacji jest mniejsza od wpisanej

### Zapytanie
Przykład wyszukiwania książki Eryk Terry'ego Pratchetta:
```
GET https://lista-ksiazek.herokuapp.com/api/books/?title=eryk&author=Pratchett
```
### Odpowiedź
```
[
    {
        "id":6,
        "author":[
            {
                "id":1,
                "name":"Terry Pratchett"
            }
        ],
        "image_link":"http://books.google.com/books/content?id=4i--PwAACAAJ&printsec=frontcover&img=1&zoom=5&source=gbs_api",
        "title":"Eryk",
        "isbn_number":"9788376480312"
        ,"language":"en",
        "page_count":113,
        "partial_date":true,
        "published_date":"2009-01-01"
    }
]
```
