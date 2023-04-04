import unittest
from Laudna import Laudna

class TestLaudna(unittest.TestCase):
    def setup(self):
        self.laudna = Laudna()

    def test_created_laudna_excists(self):
        self.assertNotEqual(self.laudna, None)
