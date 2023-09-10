from game.models import BagTiles
#player.py
class Player:

    def __init__(self):
        self.hand = []
        

    def get_tiles(self, count, bag):
        self.hand.extend(bag.take(count))

    def exchange_tiles(self,index,bag=BagTiles):
        tile_to_exchange = self.rack.pop(index)
        new_tile = bag.take(1)
        bag.put([tile_to_exchange])
        self.rack.append(new_tile)
    