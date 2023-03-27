import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_saldo_luotu_oikein(self):
        self.assertEqual(str(self), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lisays_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(500)
        
        self.assertEqual(str(self), "Kortilla on rahaa 15.00 euroa")
    
    def test_raha_vahenee_kun_ostetaan_ruokaa(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self), "Kortilla on rahaa 5.00 euroa")

    def test_saldo_ei_mene_miinukselle(self):
        self.maksukortti.ota_rahaa(1500)
        self.assertEqual(str(self), "Kortilla on rahaa 10.00 euroa")
    
    def test_tulee_true_ja_false(self):
        tulos = self.maksukortti.ota_rahaa(500)
        self.assertEqual(tulos, True)
        tulos = self.maksukortti.ota_rahaa(1000)
        self.assertEqual(tulos, True)