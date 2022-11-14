import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_konstruktori_asettaa_rahamaaran_oikein(self):
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)
    
    def test_konstruktori_asettaa_edullisten_maaran_oikein(self):
        self.assertEqual((self.kassapaate.edulliset), 0)

    def test_konstruktori_asettaa_maukkaiden_maaran_oikein(self):
        self.assertEqual((self.kassapaate.maukkaat), 0)

    def test_edullisesti_ei_liian_pieni_maksu(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(100), 100)

    def test_maukkaasti_ei_liian_pieni_maksu(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(100), 100)

    def test_edullisesti_kateisella_palauttaa_oikean_summan(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(300), 60)

    def test_maukkaasti_kateisella_palauttaa_oikean_summan(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(450), 50)

    def test_edullisesti_kateisella_kassa_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100240)

    def test_edullisesti_kateisella_kassa_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)

    def test_maukkaasti_kateisella_kassa_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100400)

    def test_maukkaasti_kateisella_kassa_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(300)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)

    def test_edullisesti_kateisella_ostetut_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(400)
        self.assertEqual((self.kassapaate.edulliset), 1)

    def test_edullisesti_kateisella_ostetut_ei_kasva(self):
        self.kassapaate.syo_edullisesti_kateisella(100)
        self.assertEqual((self.kassapaate.edulliset), 0)

    def test_maukkaasti_kateisella_ostetut_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual((self.kassapaate.maukkaat), 1)

    def test_maukkaasti_kateisella_ostetut_ei_kasva(self):
        self.kassapaate.syo_maukkaasti_kateisella(100)
        self.assertEqual((self.kassapaate.maukkaat), 0)


    def test_edullisestikort_ei_liian_pieni_saldo(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(kortti), False)

    def test_maukkaastikort_ei_liian_pieni_saldo(self):
        kortti = Maksukortti(100)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(kortti), False)

    def test_edullisesti_kortilla_toimii(self):
        kortti = Maksukortti(300)
        self.assertEqual((self.kassapaate.syo_edullisesti_kortilla(kortti)), True)

    def test_maukkaasti_kortilla_toimii(self):
        kortti = Maksukortti(450)
        self.assertEqual((self.kassapaate.syo_edullisesti_kortilla(kortti)), True)

    def test_edullisesti_kortilla_ostetut_kasvaa(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual((self.kassapaate.edulliset), 1)

    def test_edullisesti_kortilla_ostetut_ei_kasva(self):
        kortti = Maksukortti(100)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual((self.kassapaate.edulliset), 0)

    def test_maukkaasti_kortilla_ostetut_kasvaa(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual((self.kassapaate.maukkaat), 1)

    def test_maukkaasti_kateisella_ostetut_ei_kasva(self):
        kortti = Maksukortti(100)        
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual((self.kassapaate.maukkaat), 0)

    def test_edullisesti_korttimaksu_ei_muuta_kassaa(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)

    def test_maukkaasti_korttimaksu_ei_muuta_kassaa(self):
        kortti = Maksukortti(500)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)

    def test_kortille_lataaminen_kasvattaa_kassaa(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, 100)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100100)

    def test_kortille_ei_negatiivista_latausta(self):
        kortti = Maksukortti(0)
        self.kassapaate.lataa_rahaa_kortille(kortti, -10)
        self.assertEqual((self.kassapaate.kassassa_rahaa), 100000)