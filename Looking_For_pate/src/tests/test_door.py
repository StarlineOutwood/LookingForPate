import unittest
from sprites.door import Door


class TestPate(unittest.TestCase):
    def setUp(self):
        self.door = Door()

    def test_pate_exists_after_creation(self):
        self.assertNotEqual(self.door, None)
