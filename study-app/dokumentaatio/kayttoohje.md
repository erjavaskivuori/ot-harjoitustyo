# Käyttöohje

Lataa projektin viimeisimmän releasen lähdekoodi valitsemalla Assets-osion alta Source code.

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

## Kurssien tarkastelu

Onnistuneen kirjautumisen tai rekisteröitymisen jälkeen siirrytään näkymään, jossa on lista kaikista käyttäjän kursseista. Uuden kurssin voi luoda syöttämällä kurssin nimen kenttään ja painamalla sitten "Create"-painiketta.

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-kurssilista.png)

Kurssin nimeä klikkaamalla voi siirtyä kurssinäkymään, jossa voi tarkastella kurssiin liittyviä tehtäviä. Ensimmäisenä listattuna on tekemättömät tehtävät ja näiden jälkeen jo valmiit tehtävät. Painamalla "Add task" -painiketta voi lisätä kurssille uuden tehtävän.

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-kurssinakyma.png)

Takaisin kurssilistaukseen voi palata painamalla "Return"-painiketta.

## Uuden tehtävän luominen

"Add task" -painikkeen painaminen avaa seuraavanlaisen näkymän:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-uusitehtava.png)

Luodakseen uuden tehtävän on annettava tehtävälle otsikko ja määräpäivä, jonka voi valita päivämääräkenttää painamalla avautuvasta kalenteri-ikkunasta. Halutessaan tehtävälle voi "Description"-kenttään syöttää myös tarkemman kuvauksen tehtävän sisällöstä. "Add"-painiketta painamalla tehtävä lisätään kurssille.

## Tehtävien tilan muuttaminen

Kurssinäkymässä tehtävää klikkaamalla voi siirtyä tehtävänäkymään, jossa näkee tehtävän tarkemmat tiedot. Tehtävänäkymässä tehtävän voi myös merkitä valmiiksi painamalla "Set done" -painiketta.

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-tehtavanakyma1.png)

Tehdyksi merkityn tehtävän voi palauttaa TO-DO-listaan painamalla tehtävänäkymässä "Return task to TO-DO-list" -painiketta.

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-tehtavanakyma2.png)

## Kurssin poistaminen

Kurssin voi poistaa painamalla kurssinäkymän oikeassa alareunassa olevaa "Remove course" -painiketta. Painikkeen painaminen avaa ikkunan, joka varmistaa, että käyttäjä haluaa poistaa kurssin:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/kaytto-ohje-kurssinpoistaminen.png)