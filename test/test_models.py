import unittest
from game.models import Tile, BagTiles
from unittest.mock import patch

class TestTiles(unittest.TestCase):
    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)

    def test_is_joker(self):
        tile = Tile('?', 0)
        self.assertEqual(tile.is_joker(), True)
    
    def test_is_not_joker(self):
        tile = Tile('A', 1)  # Cualquier letra que no sea un comodín, por ejemplo, 'A'
        self.assertEqual(tile.is_joker(), False)

    def test_convert_tile(self):
        tile = Tile('A',1)
        tile.convert_tile('B', 2)
        self.assertEqual(tile.letter, 'B')
        self.assertEqual(tile.value, 2)

    def test_tile(self):
        tile = Tile('A', 1)
        self.assertEqual(tile.letter, 'A')
        self.assertEqual(tile.value, 1)
    def test_is_wildcard(self):
        tile = Tile('?', 0)
        self.assertEqual(tile.is_wildcard(), True)
    def test_convert_tile(self):
        tile = Tile('A',1)
        tile.convert_tile('B', 2)
        self.assertEqual(tile.letter, 'B')
        self.assertEqual(tile.value, 2)

class TestBagTiles(unittest.TestCase):
    @patch('random.shuffle')
    def test_bag_tiles(self, patch_shuffle):
        bag = BagTiles()
        self.assertEqual(len(bag.tiles), 29)  # Total de fichas, incluyendo comodines
        self.assertEqual(patch_shuffle.call_count, 1)
        self.assertEqual(patch_shuffle.call_args[0][0], bag.tiles)

    def test_take(self):
        bag = BagTiles()
        tiles = bag.take(2)
        self.assertEqual(len(bag.tiles), 27)  # Total de fichas restantes después de tomar

    def test_put(self):
        bag = BagTiles()
        put_tiles = [Tile('Z', 10), Tile('Y', 4)]
        bag.put(put_tiles)
        self.assertEqual(len(bag.tiles), 31)

    def test_initial_tiles(self):
        bag = BagTiles()
        bag.initial_tiles()
        self.assertEqual(len(bag.tiles),100)
    
    def test_initial_tiles_distribution(self):
        bag = BagTiles()
        initial_tiles_count = {'A':12,'E':12,'O':9,'I':6,'S':6,'N':5,'L':4,'R':5,'U':5,'T':4,'D':5,'G':2,'C':4,'B':2,'M':2,'P':2,'H':2,'F':1,'V':1,'Y':1,'CH':1,'Q':1,'J':1,'LL':1,'Ñ':1,'RR':1,'X':1,'Z':1,'?':2}
        bag.initial_tiles()
        letter_counts = {}
        for letter in initial_tiles_count:
            letter_counts[letter] = sum(1 for tile in bag.tiles if tile.letter == letter)
        for letter, expected_count in initial_tiles_count.items():
            with self.subTest(letter=letter):
                self.assertEqual(letter_counts[letter], expected_count, f"Letter {letter} count is not as expected.")
