# Study-app

Käyttäjä voi sovelluksen avulla pitää kirjaa kurssien suorittamisesta. Kullekin meneillään olevalle kurssille käyttäjä voi tehdä oman tehtävälistan, johon kirjataan kurssin tulevat tehtävät. Sovelluksella voi olla useita rekisteröityneitä käyttäjiä, jotka pystyvät tarkastelemaan vain omia tehtävälistojaan.

## Dokumentaatio

- [Vaatimusmäärittely](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/vaatimusmaarittely.md)

- [Arkkitehtuurikuvaus](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/arkkitehtuuri.md)

- [Käyttöohje](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kayttoohje.md)

- [Testausdokumentti](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/testaus.md)

- [Tuntikirjanpito](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/tuntikirjanpito.md)

- [Changelog](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/changelog.md)


## Releaset

[Kaikki releaset](https://github.com/erjavaskivuori/ot-harjoitustyo/releases)


## Asennus
1. Riippuvuudet asennetaan komennolla:
```
poetry install
```
2. Tämän jälkeen täytyy tehdä alustustoimenpiteet komennolla:
```
poetry run invoke build
```
3. Sovellus käynnistetään komennolla:
```
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman käynnistäminen

Kun ohjelma on asennettu, sen voi käynnistää komentoriviltä käyttämällä seuraavaa komentoa:
```
poetry run invoke start
```
### Testaus

Testit suoritetaan komennolla:
```
poetry run invoke test
```
### Testikattavuusraportin genereointi

Testikattavuusraportin voi generoida komennolla:
```
poetry run invoke coverage-report
```
Raportti generoituu htmlcov-hakemistoon.

### Pylint tarkistukset

Tiedoston .pylintrc määrittelemät tarkistukset suoritetaan komennolla:
```
poetry run invoke lint
```