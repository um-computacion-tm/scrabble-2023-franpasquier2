from game.models import BagTiles

class Player:
    def __init__(self):
        self.bag = BagTiles() 
        self.tiles = self.bag.take(7)  

    def exchange(self, tile_index):
        if 0 <= tile_index < len(self.tiles):
            exchanged_tile = self.tiles.pop(tile_index) 
            self.bag.put([exchanged_tile])  
            new_tile = self.bag.take(1)[0]  
            self.tiles.append(new_tile)  

    def get_score(self):
        
        pass

    def __str__(self):
        return ', '.join(tile.letter for tile in self.tiles)


    