from game.scrabble import Scrabble

def main():
    print('Bienvenido')

    while True:
        try:
            player_count = int(input('Cantidad de jugadores: '))
            if player_count < 2 or player_count > 4:
                raise ValueError
            else:
                break
        except ValueError:
            print('Valor inválido. Debe ser entre 2 y 4.')

    game = Scrabble(player_count)

   
    print('La cantidad de jugadores es: ' + str(player_count))

    while game.playing():
        current_player = game.get_current_player()
        print(f"Turno del jugador {current_player}")

        # Sacar fichas de la bolsa
        tiles_to_draw = 7 - len(current_player.hand)  # Sacar suficientes fichas para tener 7 en la mano
        for _ in range(tiles_to_draw):
            tile = game.bag_tiles.draw_tile()
            current_player.hand.append(tile)

        print(f"Tu mano actual: {current_player.hand}")
        
        word = input("Ingresa una palabra: ")
        location_x = int(input("Ingresa la posición X: "))
        location_y = int(input("Ingresa la posición Y: "))
        orientation = input("Ingresa la orientación (V/H): ").upper()

        # Validar y jugar la palabra
        if game.validate_word(word, (location_x, location_y), orientation):
            print("Palabra válida. ¡Bien hecho!")
        else:
            print("Palabra inválida. Inténtalo de nuevo.")

        game.next_turn()

if __name__ == "__main__":
    main()
    
        