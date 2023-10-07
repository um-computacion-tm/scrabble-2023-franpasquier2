import unittest
from game.player import Player
from game.models import Tile, BagTiles

class TestPlayer(unittest.TestCase):
    def setUp(self):
        # Configurar un jugador con una bolsa de fichas para usar en las pruebas
        bag_tile = BagTiles()
        bag_tile.tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        self.player = Player(1, bag_tile)

    def test_init(self):
        player_1 = Player(1)
        player_2 = Player(2)
        player_3 = Player(3)
        self.assertEqual(player_1.id, 1)
        self.assertEqual(player_2.id, 2)
        self.assertEqual(player_3.id, 3)

    def test_tiles_empty_after_init(self):
        player = Player(1)
        self.assertEqual(len(player.tiles), 0)

    def test_missing_bag_raises_error(self):
        player = Player(1)  # No se proporciona una bolsa de fichas
        with self.assertRaises(ValueError):
            player.has_letters([])

    def test_has_letters_valid(self):
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        self.assertFalse(self.player.has_letters(tiles))

    def test_has_letters_invalid(self):
        tiles = [
            Tile(letter='P', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        self.assertFalse(self.player.has_letters(tiles))

    def test_tiles_updated_after_use(self):
        tiles_to_use = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
        ]
        self.player.has_letters(tiles_to_use)  # Usar las letras
        self.assertEqual(len(self.player.tiles), 0)

    def test_view_tiles(self):
        # Verifica que la función view_tiles devuelva una lista de fichas vacía al inicio
        self.assertEqual(self.player.view_tiles(), [])

    def test_view_score(self):
        # Verifica que la función view_score devuelva el puntaje correcto al inicio (0)
        self.assertEqual(self.player.view_score(), 0)

    def test_start_turn(self):
        # Verifica que la función start_turn establezca correctamente la bandera is_current_turn en True
        self.player.start_turn()
        self.assertTrue(self.player.is_current_turn)

    def test_end_turn(self):
        # Verifica que la función end_turn establezca correctamente la bandera is_current_turn en False
        self.player.end_turn()
        self.assertFalse(self.player.is_current_turn)

    def test_pass_turn(self):
        # Verifica que la función pass_turn llame a end_turn para finalizar el turno
        self.player.start_turn()  # Iniciar el turno primero
        self.player.pass_turn()
        self.assertFalse(self.player.is_current_turn)

    
if __name__ == '__main__':
    unittest.main()