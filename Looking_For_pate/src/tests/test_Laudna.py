import unittest
from sprites.laudna import Laudna
from sprites.wall import Wall
from sprites.pate import Pate


class TestLaudna(unittest.TestCase):
    def setUp(self):
        self.laudna = Laudna()
        self.walls = [Wall(210, 0, True)]
        self.pate = Pate(-100, 0)

    def test_created_laudna_excists(self):
        self.assertNotEqual(self.laudna, None)

    def test_Laudna_move_through_walls(self):
        can = self.laudna.can_move(self.walls, 210, 0)
        self.assertEqual(can, False)

    def test_Laudna_can_move_not_towards_the_wall(self):
        can = self.laudna.can_move(self.walls, -210, 0)
        self.assertEqual(can, True)
