import unittest
from Pate import Pate

class TestLaudna(unittest.TestCase):
    def setup(self):
        self.pate = Pate()

    def test_pate_exists_after_creation(self):
        self.assertNotEqual(self.pate, None)