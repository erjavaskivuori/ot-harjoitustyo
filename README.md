# Study-app

Käyttäjä voi sovelluksen avulla pitää kirjaa kurssien suorittamisesta. Kullekin meneillään olevalle kurssille käyttäjä voi tehdä oman tehtävälistan, johon kirjataan kurssin tulevat tehtävät. Sovelluksella voi olla useita rekisteröityneitä käyttäjiä, jotka pystyvät tarkastelemaan vain omia tehtävälistojaan.

## Dokumentaatio

- [vaatimusmaarittely.md](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/vaatimusmaarittely.md)

- [tuntikirjanpito.md](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/tuntikirjanpito.md)

- [changelog.md](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/changelog.md)

- [arkkitehtuuri.md](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/arkkitehtuuri.md)

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

#### Ohjelman käynnistäminen:
```
poetry run invoke start
```
### Testaus
```
poetry run invoke test
```
### Testikattavuusraportin genereointi
```
poetry run invoke coverage-report
```
### Pylint tarkistukset
```
poetry run invoke lint
```