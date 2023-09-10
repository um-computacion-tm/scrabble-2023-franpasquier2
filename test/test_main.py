import unittest


from game.scrabble import Scrabble
from unittest.mock import patch

class TestScrabbleGame(unittest.TestCase):
    def setUp(self):
        # Configura el estado inicial para las pruebas
        self.game = Scrabble(2)  # Cambia el número de jugadores según sea necesario

    def test_starting_player(self):
    # Verifica que el jugador inicial sea el primero en la lista de jugadores
      current_player = self.game.get_current_player()
      self.assertEqual(current_player, self.game.players[0])

    def test_next_turn(self):
    # Verifica que el jugador cambie correctamente después de un turno
        initial_player = self.game.get_current_player()
        self.game.next_turn()
        new_player = self.game.get_current_player()
        self.assertNotEqual(initial_player, new_player)

    def test_validate_word(self):
    # Simula una jugada válida y verifica que la palabra sea aceptada
        valid_word = "Valida"
        valid_location = (7, 7)
        valid_orientation = "H"
        self.assertTrue(self.game.validate_word(valid_word.upper(), valid_location, valid_orientation))

        invalid_word = "INVALIDA"
        invalid_location = (5, 5)
        invalid_orientation = "V"
        self.assertTrue(self.game.validate_word(invalid_word.upper(), invalid_location, invalid_orientation))

if __name__ == '__main__':
    unittest.main()