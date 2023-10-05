class Player:
    def __init__(self, id, bag = None):
        self.tiles = []
        self.id = id
        self.bag = bag

    def has_letters(self, tiles):
        if not self.bag:
            raise ValueError("No se ha proporcionado una bolsa de fichas")

        for tile in tiles:
            if tile in self.tiles:
                self.tiles.remove(tile)
            else:
                return False
        return True
    
    def use_letters(self, tiles):
        for tile in tiles:
            if tile in self.tiles:
                self.tiles.remove(tile)
            else:
                raise ValueError("No tienes la letra en tu conjunto de fichas")

