import os
import sys
import pickle

# Ruta absoluta del directorio raíz del proyecto
project_root = os.path.dirname(os.path.abspath(__file__))
# Agregar el directorio raíz a sys.path
sys.path.insert(0, project_root)
# Importar las clases de game sin problemas
from game.scrabble import ScrabbleGame, InvalidJokerConversion

class Main:
    def __init__(self):
        print('Bienvenido a Scrabble Game!')
        self.player_count = self.get_player_count()
        self.game = ScrabbleGame(self.player_count)  
        self.board = self.game.get_board()
        
    def valid_player_count(self, player_count):
        try:
            count = int(player_count)
            return 2 <= count <= 4
        except ValueError:
            return False
    
    def get_player_count(self):
        while True:
            player_count = input('Cantidad de jugadores (2-4): ')
            if self.valid_player_count(player_count) is True:
                return int(player_count)
            print('Valor inválido. Debe ser un número entre 2 y 4')
    
    def next_turn(self):
        self.game.next_turn()

    def show_rack(self):
        return ' '.join(f'[{tile.letter}]' for tile in self.game.current_player.rack)
    
    def take_turn(self):
        print(f'Tu mano actual es: {self.show_rack()}')
        while True:
            option = input("Elija alguna opción:\n1) Jugar\n2) Ver Puntuación\n3) Pasar")
            option = self.game.input_to_int(option)
            if option == 1:
                self.play()
                break
            elif option == 2:
                self.show_scores()
            elif option == 3:
                break
    
    def exchange_tiles(self):
        while True:
            amount = input("¿Cuántas fichas quieres intercambiar? (1-7) (0 para salir): ")
            amount = self.game.input_to_int(amount)
            numbers = [1, 2, 3, 4, 5, 6, 7]
            if amount in numbers:
                self.convert_tiles_in_another_tile(amount, numbers)
                return 'finish'
            elif amount == 0:
                break
            else: 
                print('Valor invalido, intente de nuevo')
    
    def convert_tiles_in_another_tile(self, amount, numbers):
        for i in range(amount):
            index = input("Elige la ficha que vas a intercambiar una a una (1-7): ")
            index = self.game.input_to_int(index)
            if index in numbers:
                self.game.current_player.exchange_tiles(index, self.game.bag_tiles)
            elif index == 0:
                break
            else:
                print('Valor invalido, intente de nuevo')

    def change_joker_to_tile(self):
        while True:
            try:
                if self.convert_joker_into_tile():
                    break
            except InvalidJokerConversion as e:
                print(f'Error: {e}')
    
    def convert_joker_into_tile(self):
        new_letter = input('Ingrese la letra que desea cambiar por el comodin (0 para terminar): ')
        new_letter= new_letter.strip().upper()
        alphabet = ['A', 'B', 'C', 'CH', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'LL', 'M', 'N','Ñ', 'O', 'P', 'Q', 'R', 'RR', 'S', 'T', 'U', 'V', 'X', 'Y', 'Z']
        if new_letter in alphabet:
            self.game.convert_joker(new_letter)
            print('Se ha cambiado con exito')
            return True
        elif new_letter == '0':
            return True
        else:
            print('Valor invalido, intente de nuevo')
            return False
    
    '''def validate_move(self, word, start, direction):
        # Lógica para validar si la jugada es legal
        pass'''

    '''def show_scores(self):
        for player in self.game.players:
            print(f"Puntuación de {player.name}: {player.score}")

    def save_game(self, file_name):
        with open(file_name, 'wb') as file:
            pickle.dump(self.game, file)
        print(f"Partida guardada en '{file_name}'")'''

    def load_game(self, file_name):
        with open(file_name, 'rb') as file:
            self.game = pickle.load(file)
        print(f"Partida cargada desde '{file_name}'")

    def validate_move(self, word, start, direction):
        if self.game.board.is_valid_move(word, start, direction):
            return True
        else:
            return False
        
    def play_game(self):
        print('¡Que comienze el juegoo!')
        self.game.put_initial_tiles_bag()
        self.game.put_tiles_in_rack()        
        while not self.game.game_over():
            self.game.next_turn()
            self.show_board()
            player_number = self.game.get_current_player_id()
            print(f'Turno del jugador {player_number}')
            self.take_turn()
            self.get_tiles_to_full_rack()
        print('¡Juego finalizado!')
        self.show_scores()
        
    def show_instructions(self):
    # Mensajes para ayudar a los jugadores a comprender las reglas del juego
        print("Instrucciones de Scrabble:")
        print("1. El objetivo es formar palabras en el tablero con las fichas disponibles.")
        print("2. Las palabras deben conectarse con otras ya existentes.")

    def enhance_ui(self):
        pass


if __name__ == "__main__":
    main = Main()
    main.play_game()