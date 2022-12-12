# Arkkitehtuurikuvaus

## Rakenne

Koodin pakkausrakenne on seuraavanlainen:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/pakkaus.png)

Rakenne vastaa kolmitasoista kerrosarkkitehtuuria. Pakkaus _ui_ sisältää käyttöliittymästä vastaavan koodin, _services_ sovelluslogiikasta ja _repositories_ tietokantaopraatioista vastaavan koodin. Pakkaus _entities_ sisältää kolme luokkaa, _User_, _Course_ ja _Task_, jotka kuvaavat sovelluksen käyttämiä tietokohteita.

## Käyttöliittymä

Käyttöliittymä sisältää seitsemän erilaista näkymää:
- Aloitusnäkymä, josta siirrytään kirjautumiseen tai rekisteröitymiseen
- Kirjautuminen
- Uuden käyttäjän luominen
- Kurssilistaus
- Kurssisivu
- Uuden tehtävän luominen
- Tehtävä sivu

Näkymät on toteutettu omina luokkinaan. Näkymien näyttämisestä vastaa UI-luokka. Kukin näkymä näkyy aina yksi kerrallaan. Käyttöliittymä kutsuu sovelluslogiikasta vastaavan StudyAppService-luokan metodeja.

## Sovelluslogiikka

Seuraava luokkakaavio kuvaa ohjelman osien suhdetta:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/luokkaakaavio.png)

Luokkakaaviossa on tarkimmin kuvattu sovelluksen loogisen tietomallin muodostavat luokat User, Course ja Task. Luokat kuvaavat käyttäjiä, käyttäjien kursseja ja kursseihin liittyviä tehtäviä. 

Sovelluksen toiminnallisuudesta vastaa StudyAppService-luokan olio. Luokka hyödyntää tietokantaoperaatioista vastaavia luokkia UserRepository, CourseRepository sekä TaskRepository, joiden kautta se pääsee käsittelemään käyttäjiä, kursseja ja tehtäviä. 

StudyAppService-luokka tarjoaa metodin kaikille käyttöliittymän toiminnoille.

Ohjelman osien suhteita kuvaava pakkauskaavio:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/pakkauskaavio.drawio.png)

## Päätoiminnallisuudet

### Käyttäjän kirjautuminen

Kun kirjautumisnäkymän kenttiin syötetään käyttäjätunnus ja salasana ja tämän jälkeen painetaan Login-painiketta, sovelluksessa kontrolli etenee seuraavasti:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/sekvenssi-kirjautuminen.png)