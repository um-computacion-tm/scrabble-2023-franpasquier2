import unittest
from game.player import Player
from game.models import BagTiles  
class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player()
        self.assertEqual(
            len(player_1.tiles),
            7,
        )

    def test_exchange(self):
        player_1 = Player()
        initial_tiles = player_1.tiles.copy() 
        bag = BagTiles()  
        
        player_1.exchange(0) 
        self.assertEqual(initial_tiles, player_1.tiles)  
        self.assertEqual(len(initial_tiles), len(player_1.tiles)) 
        self.assertEqual(len(bag.tiles), 100)  


if __name__ == '__main__':
    unittest.main()