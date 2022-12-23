# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta Source code.

## Konfigurointi

Halutessaan sovelluksen käyttämän tallennustiedoston nimeä voi konfiguroida projketin juurihakemistossa olevassa `.env`-konfiguraatiotiedostossa. Mikäli tiedostoa ei vielä ole luotu, se luodaan automaattisesti data-hakemistoon. Tiedoston muoto:

```
DATABASE_FILENAME=database.sqlite
```

## Ohjelman käynnistäminen
1. Asenna ensin riippuvuudet komennolla:
```
poetry install
```
2. Tämän jälkeen tehdään alustustoimenpiteet komennolla:
```
poetry run invoke build
```
3. Sovellus voi käynnistää komennolla:
```
poetry run invoke start
```

## Aloitusnäkymä 

Kun sovelluksen käynnistää, avautuu ensimmäisen seuraavanlainen aloitusnäkymä:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-aloitusnakyma.png)

Aloitusnäkymästä käyttäjä voi valita kirjautumisen tai rekisteröitymisen.

## Kirjautuminen

Kirjautumisnäkymä on seuraavanlainen:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-kirjautuminen.png)

Kirjautuminen onnistuu "Login"-painiketta painamalla, mikäli kenttiin syötetty käyttäjätunnus ja salasana täsmäävät. Halutessaan voi palata takaisin aloitusnäkymään painamalla "Return"-painiketta.

## Rekisteröityminen

Rekisteröityäkseen käyttäjän tulee antaa uusi käyttäjänimi ja salasana ja painaa sitten "Register"-painiketta. Myös rekisteröitymisnäkymästä voi palata takaisin aloitusnäkymään "Return"-painiketta painamalla.

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-rekisteroityminen.png)

## Kirjautuminen ulos

Sovellukseen kirjautuneena jokaisessa näkymässä on oikeassa yläkulmassa "Logout"-painike, jota painamalla voi kirjautua ulos. Kun painiketta painaa, sovellus varmistaa, että käyttäjä haluaa kirjautua ulos.

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-uloskirjautuminen.png)

## Kurssien tarkastelu

Onnistuneen kirjautumisen tai rekisteröitymisen jälkeen siirrytään näkymään, jossa on lista kaikista käyttäjän kursseista. Uuden kurssin voi luoda syöttämällä kurssin nimen kenttään ja painamalla sitten "Create"-painiketta.

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-kurssilista.png)

Kurssin nimeä klikkaamalla voi siirtyä kurssinäkymään, jossa voi tarkastella kurssiin liittyviä tehtäviä. Ensimmäisenä listattuna on tekemättömät tehtävät ja näiden jälkeen jo valmiit tehtävät. Painamalla "Add task" -painiketta voi lisätä kurssille uuden tehtävän.

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-kurssinakyma.png)

## Kaikkien tehtävien katselu

Kurssilistausnäkymästä voidaan siirtyä tarkastelemaan kaikkia omia tehtäviä painamalla "See all tasks" -painiketta. Tehtävät on listattu päivämäärän mukaiseen järjestykseen. 

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-tehtavalista.png)

Tässä, ja seuraavana mainituissa näkymissä, on vasemmassa yläkulmassa nuoli, jota painamalla voi siirtyä takaisin edelliseen näkymään.

## Uuden tehtävän luominen

"Add task" -painikkeen painaminen avaa seuraavanlaisen näkymän:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-uusitehtava.png)

Luodakseen uuden tehtävän on annettava tehtävälle otsikko ja määräpäivä, jonka voi valita päivämääräkenttää painamalla avautuvasta kalenteri-ikkunasta. Halutessaan tehtävälle voi "Description"-kenttään syöttää myös tarkemman kuvauksen tehtävän sisällöstä. "Add"-painiketta painamalla tehtävä lisätään kurssille.

## Tehtävien tilan muuttaminen

Kurssinäkymässä tehtävää klikkaamalla voi siirtyä tehtävänäkymään, jossa näkee tehtävän tarkemmat tiedot. Tehtävänäkymässä tehtävän voi myös merkitä valmiiksi painamalla "Set done" -painiketta.

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-tehtavanakyma1.png)

Tehdyksi merkityn tehtävän voi palauttaa To-do-listaan painamalla tehtävänäkymässä "Return task to To-do-list" -painiketta.

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-tehtavanakyma2.png)

## Kurssin poistaminen

Kurssin voi poistaa painamalla kurssinäkymän oikeassa alareunassa olevaa "Remove course" -painiketta. Painikkeen painaminen avaa ikkunan, joka varmistaa, että käyttäjä haluaa poistaa kurssin:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-kurssinpoistaminen.png)