import unittest
from game.scrabble import ScrabbleGame, InvalidWordException, InvalidJokerConversion
from game.models import Tile
from game.board import Board
from game.cell import Cell
from game.player import Player
from game.dictionary import Dictionary 
from unittest.mock import Mock
class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        scrabble_game = ScrabbleGame(players_count=3)
        self.assertEqual(len(scrabble_game.players), 3)
        self.assertEqual(scrabble_game.current_turn, 0)

    def test_playing(self):
        game = ScrabbleGame(players_count=2)
        self.assertTrue(game.playing())

    def test_next_turn(self):
        game = ScrabbleGame(2)
        self.assertEqual(game.turn, 0)
        game.next_turn()
        self.assertEqual(game.turn, 1)

    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player.name, scrabble_game.players[0].name)

    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player.name, scrabble_game.players[1].name)

    def test_next_turn_when_player_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player.name, scrabble_game.players[0].name)
        
    def test_validate_word(self):
        game = ScrabbleGame(2)
        word = "Facultad"
        location = (7, 7)
        orientation = "Horizontal"
        self.assertEqual(game.validate_word(word,location,orientation), True)
        
    def test_validate_word_simple(self):
        # Prueba simple para validar_word
        game = ScrabbleGame(players_count=3)
        game.current_player = game.players[0]

        word = "HELLO"
        location = (7, 7)
        orientation = "Horizontal"

        with self.assertRaises(InvalidWordException):
            is_valid = game.validate_word(word, location, orientation)
            
    def test_validate_word_not_in_dictionary(self):
        game = ScrabbleGame(2)
        word = "Kadabra"
        location = (0, 0)
        orientation = "Horizontal"
        
        # Aquí necesitas validar que la excepción sea lanzada.
        with self.assertRaises(InvalidWordException):
            game.validate_word(word, location, orientation)

    def test_validate_word_exceeds_board(self):
        game = ScrabbleGame(2)
        word = "Facultad"
        location = (14,14)
        orientation = "H"
        with self.assertRaises(InvalidWordException):
            game.validate_word(word, location, orientation)
            
    def test_game_over_true(self):
        game = ScrabbleGame(players_count=2)
        game.bag_tiles.tiles = []  # Vacía la bolsa de fichas

        is_game_over = game.game_over()

        self.assertTrue(is_game_over)

    def test_game_over_false(self):
        game = ScrabbleGame(players_count=2)
        game.bag_tiles.tiles = [Tile('A', 1)]  # Agrega una ficha a la bolsa

        is_game_over = game.game_over()

        self.assertFalse(is_game_over)
    
    def test_show_amount_tiles_bag(self):
        game = ScrabbleGame(2)
        self.assertEqual(game.show_amount_tiles_bag(), 29)
    
    def test_shuffle_rack(self):
        game = ScrabbleGame(2)
        game.next_turn()
        game.current_player.rack = [Tile('A', 1), Tile('B',3), Tile('C',2)]
        game.shuffle_rack()
        self.assertEqual(len(game.current_player.rack), 3)
        
    def test_clean_word_to_use(self):
        game = ScrabbleGame(2)
        word = 'Imaginación'
        self.assertEqual(game.clean_word_to_use(word), 'IMAGINACION')
    
    '''def test_convert_joker_fine(self):
        game = ScrabbleGame(2)
        game.next_turn()
        game.current_player.rack = [Tile('?', 0)]
        game.convert_joker('A')
        self.assertEqual(game.current_player.rack[0].letter, 'A')
        self.assertEqual(game.current_player.rack[0].value, 1)'''

    def test_convert_wildcard_no_wildcard(self):
        game = ScrabbleGame(2)
        game.next_turn()
        game.current_player.rack = [Tile('A', 1)]
        with self.assertRaises(InvalidJokerConversion):
            game.convert_joker('B')

    def test_input_to_int_wrong_fine(self):
        game = ScrabbleGame(2)
        string = '0'
        self.assertEqual(game.input_to_int(string), 0)

    def test_input_to_int_wrong(self):
        game = ScrabbleGame(2)
        string = 'm'
        self.assertEqual(game.input_to_int(string), None)

    def test_calculate_scores_with_no_players(self):
        game = ScrabbleGame(players_count=4)  # Instancia de la clase o módulo que contiene 'calculate_scores'
        game.players = []  # Configuración para simular que no hay jugadores
        game.board.played_cells = [Mock(calculate_value=Mock(return_value=5))]  # Ejemplo de celdas simuladas

        game.calculate_scores()

        # Verificar que no se generen puntuaciones si no hay jugadores
        self.assertEqual(len(game.players), 0)  # Asegurarse de que no haya jugadores

    def test_calculate_scores_with_players_and_cells(self):
        game = ScrabbleGame(players_count=4)  # Instancia de la clase o módulo que contiene 'calculate_scores'
        # Configuración para simular jugadores y celdas con diferentes valores
        players = [Mock(add_score=Mock()) for _ in range(2)]
        cells = [Mock(calculate_value=Mock(return_value=i + 1)) for i in range(5)]

        game.players = players
        game.board.played_cells = cells

        game.calculate_scores()

        # Verificar que los puntajes se han calculado y sumado correctamente para todos los jugadores y celdas
        for player in players:
            player.add_score.assert_called_once_with(sum(cell.calculate_value.return_value for cell in cells))

    def test_put_initial_tiles_bag(self):
        game = ScrabbleGame(2)
        self.assertEqual(len(game.bag_tiles.tiles), 29)
        game.put_initial_tiles_bag()
        self.assertEqual(len(game.bag_tiles.tiles), 100)


if __name__ == "__main__":
    unittest.main()



