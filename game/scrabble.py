# scrabble.py
from game.board import Board
from game.player import Player
from game.models import BagTiles
from game.dictionary import Dictionary  
import random

# Excepciones
class InvalidWordException(Exception):
    pass
class InvalidJokerConversion(Exception):
    pass

class ScrabbleGame:
    def __init__(self, players_count):
        self.board = Board()
        self.bag_tiles = BagTiles()
        self.current_turn = 0
        self.current_player = None
        self.players: list[Player] = []
        self.dict = Dictionary()
        self.turn = 0
        # Crear instancias de Player con nombres
        for i in range(players_count):
            player_name = f"Player {i+1}"
            self.players.append(Player(name=player_name, bag_tiles=self.bag_tiles))
    
    def playing(self):
        return True
    
    def next_turn(self):
        if self.current_player is None:
            self.current_player = self.players[0]
        elif self.current_player == self.players[-1]:
            self.current_player = self.players[0]
        else:
            player_turn = self.players.index(self.current_player) + 1
            self.current_player = self.players[player_turn]
        self.turn += 1

    def dict_validate_word(self, word):
        dict = Dictionary()
        return dict.verify_word(word)
    
    def clean_word_to_use(self, word):
        dict = Dictionary()
        word = dict.remove_accents(word)
        word = word.strip().upper()
        return word
    

    def validate_word(self, word, location, orientation):
        if not self.dict_validate_word(word):
            raise InvalidWordException('Su palabra no existe en el diccionario')

        if not self.board.validate_word_inside_board(word, location, orientation):
            raise InvalidWordException('Su palabra excede el tablero')

        if not self.board.validate_word_place_board(word, location, orientation):
            raise InvalidWordException('Su palabra no se cruza con ninguna palabra válida')
        return True

    def game_over(self):
        if len(self.bag_tiles.tiles) == 0:
            return True
        return False
    
    def get_board(self):
        return self.board

    def show_amount_tiles_bag(self):
        return len(self.bag_tiles.tiles)
      
    def shuffle_rack(self):
        random.shuffle(self.current_player.rack)
    
    def input_to_int(self, string):
        try:
            return int(string)
        except ValueError:
            return None
            
    def convert_joker(self, new_letter):
        bag = BagTiles()
        if self.current_player.has_joker() is True:
            index = self.current_player.find_joker()
            joker = self.current_player.rack[index]
            matching_tile = next((t for t in bag.tiles if t.letter == new_letter), None)
            if matching_tile.letter == new_letter:
                joker.convert_tile(new_letter, matching_tile.value)
        else:
            raise InvalidJokerConversion('No tienes un comodin en tu rack')
        
    def calculate_scores(self):
        for player in self.players:
            player_score = 0
            for cell in self.board.played_cells:
                cell_value = cell.calculate_value()
                player_score += cell_value
            player.add_score(player_score)
        



