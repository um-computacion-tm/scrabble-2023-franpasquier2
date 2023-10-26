import random

class Tile:
    def __init__(self, letter='', value=0):
        self.letter = str(letter)
        self.value = value

    def is_joker(self):
        if self.value == 0:
            return True
        else:
            return False
        
    def test_is_joker(self):
        tile = Tile('?', 0)
        self.assertEqual(tile.is_joker(), True)
        
    def convert_tile(self, new_letter, new_value):
        self.letter = new_letter
        self.value = new_value


class BagTiles:
    def __init__(self):
        self.tiles = []

        tile_info = [
            ('A', 1, 12), ('E', 1, 12), ('O', 1, 9),
            ('I', 1, 6), ('S', 1, 6), ('N', 1, 5),
            ('L', 1, 4), ('R', 1, 5), ('U', 1, 5),
            ('T', 1, 4), ('D', 2, 5), ('G', 2, 2),
            ('C', 3, 4), ('B', 3, 2), ('M', 3, 2),
            ('P', 3, 2), ('H', 4, 2), ('F', 4, 1),
            ('V', 4, 1), ('Y', 4, 1), ('J', 8, 1),('CH',5,1),('Q',5,1),
            ('LL', 8, 1), ('Ñ', 8, 1), ('RR', 8, 1),
            ('X', 8, 1), ('Z', 10, 1),
            (' ', 0, 2)  # Comodines en blanco
        ]

        for letter, value, count in tile_info:
            self.tiles.extend([Tile(letter, value)] * count)

        random.shuffle(self.tiles)

    def take(self, count):
        tiles = []
        for _ in range(count):
            tiles.append(self.tiles.pop(0))
        return tiles

    def put(self, tiles):
        self.tiles.extend(tiles)
        while len(self.tiles) > 100:  # Mantener un máximo de 100 fichas, incluyendo comodines
            self.tiles.pop()

   
  
   
        