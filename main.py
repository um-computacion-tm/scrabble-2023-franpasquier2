from game.scrabble import Scrabble

def welcome_message():
    print('Bienvenido')

def get_player_count():
    while True:
        try:
            player_count = int(input('Cantidad de jugadores: '))
            if 2 <= player_count <= 4:
                return player_count
            else:
                raise ValueError
        except ValueError:
            print('Valor inválido. Debe ser entre 2 y 4.')

def play_turn(game):
    current_player = game.get_current_player()
    print(f"Turno del jugador {current_player}")

    tiles_to_draw = 7 - len(current_player.hand)
    for _ in range(tiles_to_draw):
        tile = game.bag_tiles.draw_tile()
        current_player.hand.append(tile)

    print(f"Tu mano actual: {current_player.hand}")

    word = input("Ingresa una palabra: ")
    location_x = int(input("Ingresa la posición X: "))
    location_y = int(input("Ingresa la posición Y: "))
    orientation = input("Ingresa la orientación (V/H): ").upper()

    if game.validate_word(word, (location_x, location_y), orientation):
        print("Palabra válida. ¡Bien hecho!")
    else:
        print("Palabra inválida. Inténtalo de nuevo.")

def main():
    welcome_message()
    player_count = get_player_count()
    game = Scrabble(player_count)
    print(f'La cantidad de jugadores es: {player_count}')

    while game.playing():
        play_turn(game)

if __name__ == "__main__":
    main()
    
        