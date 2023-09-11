import unittest
from game.board import Board
from game.player import Player
from game.models import Tile, BagTiles
from game.scrabble import Scrabble

class TestScrabble(unittest.TestCase):
    def setUp(self):
        self.scrabble_game = Scrabble(2)  # Cambia el número de jugadores según sea necesario

    def test_initialization(self):
        self.assertEqual(len(self.scrabble_game.players), 2)
        self.assertIsInstance(self.scrabble_game.board, Board)
        self.assertIsInstance(self.scrabble_game.bag_tiles, BagTiles)
        self.assertEqual(self.scrabble_game.current_player_index, 0)
        self.assertEqual(self.scrabble_game.turn, 0)

    def test_next_turn(self):
        initial_player_index = self.scrabble_game.current_player_index
        self.scrabble_game.next_turn()
        new_player_index = self.scrabble_game.current_player_index
        self.assertNotEqual(initial_player_index, new_player_index)

    def test_get_current_player(self):
        current_player = self.scrabble_game.get_current_player()
        self.assertEqual(current_player, self.scrabble_game.players[0])


    def test_playing(self):
        # Prueba que el juego sigue en curso al comienzo (bolsa de fichas no está vacía)
        self.assertTrue(self.scrabble_game.playing())

        # Simula el agotamiento de las fichas en la bolsa (el juego debería terminar)
        self.scrabble_game.bag_tiles.tiles = []
        self.assertFalse(self.scrabble_game.playing())

    def test_draw_tile(self):
        # Prueba que se pueda sacar una ficha de la bolsa
        tile = self.scrabble_game.draw_tile()
        self.assertIsInstance(tile,Tile)

        # Prueba que no se puedan sacar más fichas si la bolsa está vacía
        self.scrabble_game.bag_tiles.tiles = []
        tile = self.scrabble_game.draw_tile()
        self.assertIsNone(tile)

   

if __name__ == '__main__':
    unittest.main()


