import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti = Maksukortti(1000)

    def test_kassapaate_on_olemassa(self):
        self.assertNotEqual(self.kassapaate, None)

    def test_tiedot_astetettu_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_edullinen_lounas_kateisella_kassa(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_edullinen_lounas_kateisella_vaihtoraha(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(vaihto, 60)

    def test_edullinen_lounas_kateisella_ei_riita_rahat(self):
        vaihto = self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihto, 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_edullinen_lounas_kateisella_lounas_plus_yks(self):
        self.kassapaate.syo_edullisesti_kateisella(300)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_maukas_lounas_kateisella_kassa(self):
        self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_maukas_lounas_kateisella_vaihtoraha(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(500)
        self.assertEqual(vaihto, 100)

    def test_maukas_lounas_kateisella_ei_riita_rahat(self):
        vaihto = self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)
        self.assertEqual(vaihto, 200)
        self.assertEqual(self.kassapaate.maukkaat, 0)


    def test_maukas_lounas_kateisella_lounas_plus_yks(self):
        self.kassapaate.syo_maukkaasti_kateisella(600)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_edullinen_lounas_kortilla_lounas_ja_palautus(self):
        tulee = self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(tulee, True)

    def test_edullinen_lounas_kortilla_loikeat_muutokset(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 7.60 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)


    def test_edullinen_lounas_kortilla_ei_rahaa_lounas_ja_palautus(self):
        kortti = Maksukortti(200)
        tulee = self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(tulee, False)
        self.assertEqual(self.kassapaate.edulliset, 0)  

    def test_edullinen_lounas_kortilla_ei_rahaa_muutokset(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")       

    def test_maukas_lounas_kortilla_lounas_ja_palautus(self):
        tulee = self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(tulee, True)

    def test_maukas_lounas_kortilla_muutokset(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 6.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_maukas_lounas_kortilla_ei_rahaa_lounas_ja_palautus(self):
        kortti = Maksukortti(200)
        tulee = self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(tulee, False)

    def test_maukas_lounas_kortilla_ei_rahaa_muutokset(self):
        kortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(kortti)
        self.assertEqual(str(kortti), "Kortilla on rahaa 2.00 euroa")

    def test_saldon_lisays(self):
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 1000)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 20.00 euroa")
        self.assertEqual(self.kassapaate.kassassa_rahaa, 101000)

    