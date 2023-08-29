import unittest
from game.models import BagTiles
from game.player import Player

class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.player = Player()
    
    def test_initial_tiles(self):
        self.assertEqual(len(self.player.tiles), 7)

    def test_exchange(self):
        initial_tiles = self.player.tiles.copy()
        initial_bag_size = len(self.player.bag.tiles)
        
        # Intercambia la primera ficha
        self.player.exchange(0)
        
        self.assertNotEqual(initial_tiles, self.player.tiles)
        self.assertEqual(len(self.player.tiles), 7)  # Asegura que el jugador aún tiene 7 fichas
        self.assertEqual(len(self.player.bag.tiles), initial_bag_size)  # La bolsa no debe cambiar

    # Agrega más pruebas según tus necesidades

if __name__ == '__main__':
    unittest.main()

