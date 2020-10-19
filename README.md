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

## Zapytanie
Przykład wyszukiwania książki Eryk Terry'ego Pratchetta:
```
GET https://lista-ksiazek.herokuapp.com/api/books/?title=eryk&author=Pratchett
```
