# Vaatimusmäärittely

## Sovelluksen tarkoitus

Käyttäjä voi sovelluksen avulla pitää kirjaa kurssien suorittamisesta. Kullekin meneillään olevalle kurssille käyttäjä voi tehdä oman tehtävälistan, johon kirjataan kurssiin liittyvät tehtävät. Sovelluksella voi olla useita rekisteröityneitä käyttäjiä, jotka pystyvät tarkastelemaan vain omia tehtävälistojaan.

## Sovelluksen toiminnallisuudet

### Tunnuksen luominen ja kirjautuminen

* Käyttäjä voi luoda käyttäjätunnuksen sovellukseen.
    - Kahdella käyttäjällä ei voi olla samaa käyttäjätunnusta. Pituudeltaan käyttäjätunnuksen tulee olla vähintään kolme merkkiä. Mikäli syötteet eivät täytä vaatimuksia, sovellus ilmoittaa siitä.
* Käyttäjä voi kirjautua sovellukseen ja sieltä ulos.
    - Kirjautuakseen käyttäjän tulee syöttää olemassaoleva käyttäjätunnus ja siihen kuuluva salasana kirjautumislomakkeelle. Mikäli käyttäjätunnus ja salasana eivät vastaa mitään tietokantaan tallennettua käyttäjää, sovellus ilmoittaa siitä.


### Kirjautuneena järjestelmään

* Käyttäjä näkee omat kurssit.
* Käyttäjä voi luoda uuden kurssin ja sille tehtäviä. 
    - Tehtäville määritellään otsikon lisäksi määräpäivä sekä halutessaan tehtävälle voi lisätä tarkemman kuvauksen.
    - Kurssisivulla käyttäjä näkee erikseen listattuna tekemättömät ja valmiit tehtävät.
    - Tehtävät ja kurssit näkyvät vain sille käyttäjälle, joka on luonut tehtävät.
* Käyttäjä voi katsella yhtä aikaa kaikkiin kursseihin liittyviä tehtäviä määräpäivän mukaan järjestettynä.
* Käyttäjä voi poistaa kurssin, jolloin myös siihen liittyvät tehtävät poistuvat.

## Jatkokehitysideoita

* Käyttäjä voi tarkastella poistettuja kursseja ja halutessaa palauttaa kurssin.
* Käyttäjä voi muokata kurssin nimeä tai tehtäviä.
* Erilaiset käyttäjäprofiilit: esimerkiksi opettaja, joka voi jakaa opiskelijoille  tehtävälistan kurssin suorituksista.