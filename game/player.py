from game.models import BagTiles

class Player:
    def __init__(self):
        self.bag = BagTiles()  # Crea una instancia de BagTiles para el jugador
        self.tiles = self.bag.take(7)  # Inicializa las fichas del jugador

    def exchange(self, tile_index):
        if 0 <= tile_index < len(self.tiles):
            exchanged_tile = self.tiles.pop(tile_index)  # Remueve la ficha a intercambiar
            self.bag.put([exchanged_tile])  # Agrega la ficha intercambiada a la bolsa
            new_tile = self.bag.take(1)[0]  # Toma una nueva ficha de la bolsa
            self.tiles.append(new_tile)  # Agrega la nueva ficha al jugador

    def get_score(self):
        # Implementa la lógica para calcular el puntaje del jugador
        pass

    def __str__(self):
        return ', '.join(tile.letter for tile in self.tiles)


    