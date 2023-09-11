import unittest
from game.scrabble import ScrabbleGame
from game.player import Player

class TestScrabbleGame(unittest.TestCase):
    def test_init(self):
        players_count = 3
        scrabble_game = ScrabbleGame(players_count)
        
        # Verifica que el juego se haya inicializado correctamente
        self.assertIsNotNone(scrabble_game.board)
        self.assertIsNotNone(scrabble_game.bag_tiles)
        
        # Verifica que el número de jugadores sea el esperado
        self.assertEqual(len(scrabble_game.players), players_count)
        
        # Verifica que los jugadores sean instancias válidas de la clase Player
        for player in scrabble_game.players:
            self.assertIsInstance(player, Player)
        
        # Verifica que el jugador actual esté configurado como None al principio
        self.assertIsNone(scrabble_game.current_player)

    def test_next_turn_when_game_is_starting(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = None
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player, scrabble_game.players[0])

    def test_next_turn_when_player_is_not_the_first(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[0]
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player, scrabble_game.players[1])

    def test_next_turn_when_player_is_last(self):
        scrabble_game = ScrabbleGame(players_count=3)
        scrabble_game.current_player = scrabble_game.players[2]
        scrabble_game.next_turn()
        self.assertEqual(scrabble_game.current_player, scrabble_game.players[0])

if __name__ == '__main__':
    unittest.main()



