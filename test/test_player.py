import unittest
from game.player import Player
from game.models import Tile, BagTiles


class TestPlayer(unittest.TestCase):
    def test_init(self):
        player_1 = Player(1)
        player_2 = Player(2)
        player_3 = Player(3)
        self.assertEqual(player_1.id,1)
        self.assertEqual(player_2.id,2)
        self.assertEqual(player_3.id,3)

    def test_tiles_empty_after_init(self):
        player = Player(1)
        self.assertEqual(len(player.tiles), 0)

    def test_missing_bag_raises_error(self):
        player = Player(1)  # No se proporciona una bolsa de fichas
        with self.assertRaises(ValueError):
            player.has_letters([])

    def test_has_letters_valid(self):
        bag_tile = BagTiles()
        bag_tile.tiles = [
        Tile(letter='H', value=1),
        Tile(letter='O', value=1),
        Tile(letter='L', value=1),
        Tile(letter='A', value=1),
    ]
        player = Player(1, bag_tile)
        tiles = [
            Tile(letter='H', value=1),
            Tile(letter='O', value=1),
            Tile(letter='L', value=1),
            Tile(letter='A', value=1),
        ]
        self.assertFalse(player.has_letters(tiles))

def test_has_letters_invalid(self):
    bag_tile = BagTiles()
    bag_tile.tiles = [
        Tile(letter='P', value=1),
        Tile(letter='O', value=1),
        Tile(letter='L', value=1),
        Tile(letter='A', value=1),
    ]
    player = Player(bag_tile)
    tiles = [
        Tile(letter='H', value=1),
        Tile(letter='O', value=1),
        Tile(letter='L', value=1),
        Tile(letter='A', value=1),
    ]
    self.assertFalse(player.has_letters(tiles))


def test_tiles_updated_after_use(self):
    bag_tile = BagTiles()
    bag_tile.tiles = [
        Tile(letter='H', value=1),
        Tile(letter='O', value=1),
        Tile(letter='L', value=1),
        Tile(letter='A', value=1),
    ]
    player = Player(bag_tile)
    tiles_to_use = [
        Tile(letter='H', value=1),
        Tile(letter='O', value=1),
    ]
    player.has_letters(tiles_to_use)  # Usar las letras
    self.assertEqual(len(player.tiles), 2)

    


if __name__ == '__main__':
    unittest.main()