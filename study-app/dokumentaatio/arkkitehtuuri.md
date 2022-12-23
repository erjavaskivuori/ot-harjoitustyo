# Arkkitehtuurikuvaus

## Rakenne

Koodin pakkausrakenne on seuraavanlainen:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/pakkaus.png)

Rakenne vastaa kolmitasoista kerrosarkkitehtuuria. Pakkaus _ui_ sisältää käyttöliittymästä vastaavan koodin, _services_ sovelluslogiikasta ja _repositories_ tietokantaopraatioista vastaavan koodin. Pakkaus _entities_ sisältää kolme luokkaa, _User_, _Course_ ja _Task_, jotka kuvaavat sovelluksen käyttämiä tietokohteita.

## Käyttöliittymä

Käyttöliittymä sisältää kahdeksan erilaista näkymää:
- Aloitusnäkymä, josta siirrytään kirjautumiseen tai rekisteröitymiseen
- Kirjautuminen
- Uuden käyttäjän luominen
- Kurssilistaus
- Kurssisivu
- Uuden tehtävän luominen
- Tehtävä sivu
- Listaus kaikista tehtävistä

Näkymät on toteutettu omina luokkinaan. Näkymien näyttämisestä vastaa UI-luokka. Kukin näkymä näkyy aina yksi kerrallaan. Käyttöliittymä kutsuu sovelluslogiikasta vastaavan StudyAppService-luokan metodeja.

## Sovelluslogiikka

Seuraava luokkakaavio kuvaa ohjelman osien suhdetta:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/luokkakaavio.png)

Luokkakaaviossa on tarkimmin kuvattu sovelluksen loogisen tietomallin muodostavat luokat User, Course ja Task. Luokat kuvaavat käyttäjiä, käyttäjien kursseja ja kursseihin liittyviä tehtäviä. 

Sovelluksen toiminnallisuudesta vastaa StudyAppService-luokan olio. Luokka hyödyntää tietokantaoperaatioista vastaavia luokkia UserRepository, CourseRepository sekä TaskRepository, joiden kautta se pääsee käsittelemään käyttäjiä, kursseja ja tehtäviä. 

StudyAppService-luokka tarjoaa metodin kaikille käyttöliittymän toiminnoille.

Ohjelman osien suhteita kuvaava pakkauskaavio:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/pakkauskaavio.drawio.png)

## Tietojen pysyväistallennus

Tietojen tallentamisesta vastaavat pakkaukseen _repositories_ UserRepository-, CourseRepository- ja TaskRepository-luokat. Tiedot tallennetaan SQLite-tietokantaan.

### Tiedostot

Kaikki käyttäjiin, kursseihin ja tehtäviin liittyvät tiedot tallennetaan samaan tiedostoon. Tiedoston nimi määritellään sovelluksen juureen sijoitetussa .env-konfiguraatiotiedostossa. 

SQLite-tietokannassa käyttäjien tiedot tallennetaan users-tauluun, kurssien courses-tauluun ja tehtävien courseTasks-tauluun. Tietokannan taulut alustetaan initialize_database.py-tiedostossa.

## Päätoiminnallisuudet

Sovelluksen toimintalogiikka kuvattuna päätoiminnallisuuksien osalta sekvenssikaavioina.

### Käyttäjän kirjautuminen

Kun kirjautumisnäkymän kenttiin syötetään käyttäjätunnus ja salasana ja tämän jälkeen painetaan Login-painiketta, sovelluksessa kontrolli etenee seuraavasti:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/sekvenssi-kirjautuminen.png)

Login-painikkeen painamiseen reagoi tapahtumankäsittelijä, joka kutsuu sovelluslogiikan StudyAppService login-metodia, jolle annetaan parametreiksi käyttäjätunnus ja salasana. Sovelluslogiikka selvittää UserRepository-luokan find_by_username-metodia kutsumalla onko kyseinen käyttäjätunnus olemassa ja mikäli on, metodi palauttaa käyttäjätunnuksen ja siihen kuuluvan salasanan. Jos salasanat täsmäävät, käyttäjä pääsee kirjautumaan sisään. Tämän seurauksena käyttöliittymä vaihtaa näkymäksi AllCoursesView:n ja renderöi näkymään kirjautuneen käyttäjän kurssit. 

### Uuden käyttäjän luominen

Kun rekisteröitymisnäkymän kenttiin syötetään uusi käyttäjätunnus ja salasana ja tämän jälkeen painetaan Register-painiketta, sovelluksessa kontrolli etenee seuraavasti:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/sekvenssi-kayttajan-luominen.png)

Register-painikkeen painamiseen reagoi tapahtumankäsittelijä, joka kutsuu sovelluslogiikan StudyAppService create_user-metodia, jolle annetaan parametreiksi käyttäjätunnus ja salasana. Sovelluslogiikka selvittää UserRepository-luokan find_by_username-metodia kutsumalla onko kyseinen käyttäjätunnus olemassa. Mikäli ei ole, uusi käyttäjä voidaan luoda kutsumalla UserRepository-luokan create_user-metodia. Metodille annetaan parametreiksi käyttäjätunnus ja salasanan hajautusarvo. Salasanan hajautusarvo luodaan BCrypt-funktion avulla. Metodi palauttaa User-olion ja käyttäjä kirjataan automaattisesti sovellukseen sisään. Tämän seurauksena käyttöliittymä vaihtaa näkymäksi AllCoursesView:n.

### Kurssin luominen

Kun kurssilistausnäkymässä annetaan uuden kurssin nimi ja painetaan Create-painiketta, sovelluksessa kontrolli etenee seuraavasti:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/sekvenssi-kurssin-luominen.png)

Create-painikkeen painamiseen reagoi tapahtumankäsittelijä, joka kutsuu sovelluslogiikasta vastaavan StudyAppService-luokan metodia create_course antaen samalla parametriksi kurssin nimen. Sovelluslogiikka kutsuu sitten CourseRepository-luokan metodia create_course, jolle annetaan parametreiksi kirjautunut käyttäjä User-oliona sekä kurssin nimi. Metodi palauttaa Course-olion, josta tulee sovelluslogiikan self._course -muuttujan arvo. Tämän seurauksena käyttöliittymä vaihtaa näkymäksi CourseView:n.

### Tehtävän lisääminen kurssille

Uuden tehtävän luominen aloitetaan siirtymällä tehtävän luomisnäkymään painamalla kurssisivulla Add task -painiketta. Kun tehtävän luomisnäkymässä annetaan otsikko, kuvaus sekä valitaan tehtävän määräpäivä ja painetaan sitten Add-painiketta, sovelluksessa kontrolli etenee seuraavasti:

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/sekvenssi-tehtavan-luominen.png)

Add task -painikkeen painamisen seurauksena käyttöliittymä vaihtaa näkymäksi CreateTaskView:n. Kun käyttäjä painaa Add-painiketta, siihen reagoi tapahtumankäsittelijä, joka kutsuu StudyAppService-luokan add_task-metodia. Metodin parametreiksi annetaan otsikko, kuvaus ja määräpäivä. Kuvaus on vapaaehtoinen, ja mikäli kenttään ei syötä mitään, tallentuu tietokantaan tyhjä merkkijono. Sovelluslogiikka kutsuu sitten TaskRepository-luokan create_task-metodia, jolle annetaan parametreiksi kurssi, johon tehtävä liittyy, Course-oliona, otsikko, kuvaus ja määräpäivä. Tämän seurauksena käyttöliittymä vaihtaa näkymäksi CourseView:n.