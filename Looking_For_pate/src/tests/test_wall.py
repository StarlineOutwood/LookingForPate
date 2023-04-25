import unittest
from sprites.wall import Wall


class TestPate(unittest.TestCase):
    def setUp(self):
        self.wall = Wall()

    def test_pate_exists_after_creation(self):
        self.assertNotEqual(self.wall, None)
