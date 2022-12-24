# Testausdokumentti

Ohjelmaa on testattu automatisoiduilla yksikkö- ja integraatiotesteillä unittestilla sekä manuaalisesti järjestelmä tason testeillä.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluslogiikasta vastaavaa `StudyAppService`-luokkaa testataan `TestStudyAppService`-testiluokalla. Testissä on käytössä `FakeUserRepository`-, `FakeCourseRepository`- ja `FakeTaskRepository`-luokat, jotka tallentavat tietoa muistiin pysyväistallennuksen sijaan.

### Repositorio-luokat

`UserRepository`-, `CourseRepository`- ja `TaskRepository`-luokkia testataan ainoastaan testeissä käytössä olevalla tiedostolla, jonka nimi on konfiguroitu .env.test-tiedostoon.

### Testauskattavuus

Sovelluksen testauksen haarautumakattavuus on 86%.

![kuva](https://github.com/erjavaskivuori/ot-harjoitustyo/blob/main/study-app/dokumentaatio/kuvat/testikattavuus.png)

Haarautumakattavuudessa ei oteta huomioon käyttöliittymäkerrosta.

## Järjestelmätestaus

Sovelluksen järjestelmätestaus on suoritettu manuaalisesti.

### Asennus ja toiminnallisuudet

Sovellus on haettu ja sitä on testattu käyttöohjeen kuvaamalla tavalla Linux-ympäristössä.

Testauksessa on käyty läpi kaikki määrittelydokumentin ja käyttöohjeen listaamat toiminnallisuudet. Kaikkien toiminnallisuuksien testaamisessa on syötekenttiä yritetty täyttää myös virheellisillä arvoilla.