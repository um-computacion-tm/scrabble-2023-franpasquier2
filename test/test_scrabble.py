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

    def test_validate_word_direction(self):
        # Configura un caso de prueba con diferentes orientaciones

        # Caso 1: Orientación horizontal válida
        result1 = self.scrabble_game.validate_word("PALABRA", (0, 0), "H")
        self.assertTrue(result1)

        # Caso 2: Orientación vertical válida
        result2 = self.scrabble_game.validate_word("PALABRA", (0, 0), "V")
        self.assertTrue(result2)

        # Caso 3: Orientación no válida
        result3 = self.scrabble_game.validate_word("PALABRA", (0, 0), "D")
        self.assertFalse(result3)

    def test_validate_word_coordinates(self):
        # Configura un caso de prueba con diferentes coordenadas

        # Caso 1: Coordenadas válidas
        result1 = self.scrabble_game.validate_word("PALABRA", (0, 0), "H")
        self.assertTrue(result1)

        # Caso 2: Coordenadas fuera del límite horizontal
        result2 = self.scrabble_game.validate_word("PALABRA", (16, 0), "H")
        self.assertFalse(result2)

        # Caso 3: Coordenadas fuera del límite vertical
        result3 = self.scrabble_game.validate_word("PALABRA", (0, 16), "V")
        self.assertFalse(result3)

    def test_validate_word_crossing(self):
        # Configura un caso de prueba donde la palabra cruza con una palabra existente

        # Coloca una palabra existente en el tablero
        self.scrabble_game.board.cells[0][0].add_letter("P")
        self.scrabble_game.board.cells[0][1].add_letter("A")
        self.scrabble_game.board.cells[0][2].add_letter("L")
        self.scrabble_game.board.cells[0][3].add_letter("A")

        # Caso 1: Palabra que cruza con palabra existente
        result1 = self.scrabble_game.validate_word("PALABRA", (0, 0), "V")
        self.assertTrue(result1)

        # Caso 2: Palabra que no cruza con palabra existente
        result2 = self.scrabble_game.validate_word("BARCO", (0, 0), "H")
        self.assertTrue(result2)

if __name__ == '__main__':
    unittest.main()


