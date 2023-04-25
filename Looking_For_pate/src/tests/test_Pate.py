import unittest
from sprites.pate import Pate


class TestPate(unittest.TestCase):
    def setUp(self):
        self.pate = Pate()

    def test_pate_exists_after_creation(self):
        self.assertNotEqual(self.pate, None)
