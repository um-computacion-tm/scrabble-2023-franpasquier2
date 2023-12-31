# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html)

## [0.0.35] - 7-11-2023

### Add 

-Add a new file with a WORDPARSER class that contains methods for manipulating words and tokens:

    -string_to_tiles(input_string, list): Converts a text string into a list of tiles.

    
    -special_to_tiles(input_string, list): Handles special two-letter combinations ('CH', 'LL', 'RR') and converts them into tiles.

    -word_to_tiles(word): Converts a word into a list of tiles, identifying special combinations.

    -locations_to_positions(word, location, orientation): Determines the positions occupied by a word's tiles on a board, based on the word, location, and orientation.

    -word_to_cells(word, location, orientation, board): Converts a word into a list of cells, used to place tiles on a board.

    -word_to_false_cells(word): Creates empty cells based on a word's tiles, but does not place them on the board.

    -result_to_list_of_words(result): Extracts the first entry of each sublist into a results list, used to store and handle valid words.

-Add a new file with a WORDANALYZER class to analyze and manipulate words and cells in a Scrabble-type game, which contains these methods:

    -calculate_word_value(word): Calculates the total value of a word considering letter and word multipliers.

    -compare_tiles_and_letters(tile, letter): Compares whether the letter on a tile matches a given letter.

    -get_tiles_for_word_placement(word, location, orientation, board): Gets the tiles that will be used to place a word on a board at a given position and orientation.

    -tiles_needed_to_form_word(word, location, orientation, board): Identifies the tiles needed to form a word given a location and orientation on the board.

    -Methods of obtaining cells around a word on the board:
        get_cell_in_the_extreme_horizontal
        get_cell_in_the_extreme_vertical
        get_cell_around_word_horizontal
        get_cell_around_word_vertical

    -verify_cell_around_word(list_cell, list_tiles, board): Checks if the cells around a word contain tiles and if they are available on the board.

    -Methods to check letters/cells before and after a word in a specific orientation:
        check_cells_before_horizontal
        check_cells_before_vertical
        check_cells_after_horizontal
        check_cells_after_vertical

    -find_words_in_directions(location_of_word, orientation, string, board): Finds words in a direction (horizontal or vertical) around an already placed word.

    -check_tiles_around_word(list_tiles, orientation, board): Checks the words around the tiles of a word placed on a board, in a specific orientation (horizontal or vertical).

- Add new methods in main.

### Changed

- I made all kinds of modifications to the other classes to be able to fix coverage.

- Big changes to my class board

## [0.0.34] - 5-11-2023

### Changed

-I made some changes and modifications to my BagTiles class

### Add

-Add new methods in my models class that check if a token is a wildcard or not and a method that allows changing the letter and value of a token.

-Add a new method in my ScrabbleGame class put_initial_tiles_bag that is responsible for preparing the bag of game tiles, calling the initial_tiles() function that initializes the tiles with their corresponding values ​​and quantities.


## [0.0.33] - 3-11-2023

### Changed

-Changes and modifications in Scraabble, to improve code coverage.

### Add

- Add a new class Tools_1, which contain methods that are intended to assist in formatting, checking and handling cells and their contents within the game board.

## [0.0.32] - 31-10-2023

### Add

-Also add new methods that manage the logic and interaction of the Scrabble game.

### Changed

-I was making changes and modifications in main to be able to run the game.

-Changes in my .codeclimate.yml

## [0.0.31] - 26-10-2023

### Add

-Add new methods to my Tile class

-New methods in Main:

The change_joker_to_tile function allows the player to attempt to exchange a joker for a normal tile while handling exceptions if an error occurs.

convert_joker_into_tile prompts the player to enter a letter to replace the joker. It then checks to see if the letter entered is in a list of valid letters (the Scrabble alphabet). If it is a valid letter, the game's convert_joker method is called to make the replacement and a success message is displayed.

### Changed

-I made some modifications to the player to improve the coverage since there were lines that were not read.

-Multipliers of words and letters on a Scrabble board and creates a matrix representation of the game board in my Board class.

## [0.0.30] - 24-10-2023

### Add

- Add a new method that calculates player scores based on the cells played on the board during a turn and updates player scores accordingly. Each player will receive a score based on the letters they played and any multipliers on the cells played.

- Next commit, I will increase the coverage percentage

## [0.0.29] - 23-10-2023

-New method that checks if a letter can be placed in this cell based on the rules of the game, such as if it is already occupied or if the multiplier type is valid.


## [0.0.28] - 22-10-2023

### Changed

-I made changes to main that make it more complete and offer more advanced functionality for playing Scrabble on the console. Provides player options, exception handling, and a more complete interface.

-I made some small modifications to my player class

### Add
-Add new valid and invalid joker conversion classes to my scrabble class


## [0.0.27] - 20-10-2023

### Add

- Add new methods in main, which focus on validating the input and output functionality of the game, specifically capturing and validating the number of players, as well as starting the game once a valid number is entered. Testing ensures that the game responds appropriately to valid and invalid input and continues to function after receiving valid input.

## [0.0.26] - 19-10-2023

### Changed

-I made changes to my models.py class, it now defines the tiles in a list called tile_info with tuples containing the letter, value and quantity of each tile. It then uses a loop to create the tokens based on the information in this list.

### Add

-Add Dockerfile

## [0.0.25] - 18-10-2023

### Changed

- Rename calculate_word_value to tools, then add tools

- Modify my scrabble class so that my covergae is higher

- Delete the env folder from my repository

## [0.0.24] - 10-10-2023

### Changed

- I made modifications to my board class to make it a more flexible and functional version, expanding its capacity and versatility, providing a solid foundation for the development and playability of the game.

- Improve the usability and customization capacity of the dashboard.


## [0.0.23] - 09-10-2023

### Add 

- New methods in the player classes that evaluate the behavior and functionalities of a player in the game, such as the ability to take chips from a bag, exchange chips, view their chips, manage their score, start and end turns, pass turns and validate if you have the necessary tokens to form valid words

### Changed

- Changes to my srcabble class


## [0.0.22] - 07-10-2023

### Add 

- Add new methods to my player class, related to the management of tokens, scoring and the status of a player's turn in a game.


## [0.0.21] - 05-10-2023

### Add

- Add a new method that tests that the player's letter bag updates correctly after using some letters.

## [0.0.20] - 3-10-2023

### Changes
-Confirmed that it throws an error (ValueError) when trying to set an invalid multiplier type.

-Verified that it correctly sets the multiplier type and multiplier value when a valid multiplier type is provided.

### Add

- Add a test that the tiles list is empty after initialization.

- Add a test has_letters function with different scenarios, both with valid letters and invalid letters in the player's letter bag.


## [0.0.19] - 29-09-2023

### Add
- Add a new file containing all the words.

### Changes

- I made some modifications to dictionary that can check if a word is in a list of valid words after removing accents and converting it to lowercase.

## [0.0.18] - 26-09-2023

### Add

- Add a new method in the cell class that checks if a cell can contain a letter based on its current state.

- Also add an input validation in the add_letter method to verify that the data entered complies.

## [0.0.17] - 25-09-2023

### Add

-Add a method to change the multiplier and multiplier type of a cell.

-Add a method to check if the cell is occupied with a letter.

### Changed

-In the cell class I deleted some methods that were duplicated, to improve coverage.

## [0.0.16] - 24-09-2023

### Add

- Add additional validation in the add_letter method to ensure that only Tile objects can be added as letters to the cell. This would help avoid errors in the code.
- Also add a 'remove_letter' method to remove a letter from the cell


## [0.0.15] - 23-09-2023

### Add

- Add validations for multiplier and multiplier_type in the __init__ constructor. If any of these values ​​do not meet the specified requirements, a ValueError exception will be raised with a corresponding error message. This ensures that the values ​​provided are valid when instantiating the Cell class.



## [0.0.14] - 21-09-2023

### Add

- To check if a word passes through the center of the board both vertically and horizontally, add a function called validate_word_passes_center in the Board class
- This function checks if the word will pass through the center of the board based on its length and orientation. If the word passes through the center, the function returns True; otherwise it returns False.


## [0.0.13] - 14-09-2023

### Add 

- The is_empty function checks if a board is empty. It loops through all the cells on the board and, if it finds at least one cell with a letter (that is, it is not empty), it returns False, indicating that the board is not empty. If it does not find any cell with a letter, it returns True, indicating that the board is empty.


## [0.0.12] - 13-09-2023

### Add 

-Create a class that is a dictionary that checks that words exist in the dictionary.

-Add the missing tests to my board class so that the coverage is complete.

-test_validate_word_inside_board_horizontal: Checks if a word fits correctly in a horizontal row on the board.

-test_validate_word_inside_board_vertical: Tests whether a word fits correctly into a vertical column on the board.

-test_validate_word_inside_board_without_orientation: Ensures that the method properly handles the case where no orientation is provided to validate the word on the board.


## [0.0.11] - 12-09-2023

### Changed

-The change made to check for collisions in the code was to add a condition that checks if the letter you are trying to place in a cell on the board conflicts with an already existing letter in that same cell. 

-If there is a letter in the cell and that letter is not the same as the letter you are trying to place, it is considered a collision and the word is invalid in that position. This applies to both horizontally and vertically placed words on the board.


## [Unreleased]

## [0.0.10] - 11-09-2023

### Changed

- Now the initial tokens are defined at the beginning and not by a method.

### Removed

- Remove the initial_tiles method


## [0.0.9] - 10-09-2023

### Added
 
-This version adds a method to validate if a word a player wants to place on the board fits on it. Calculate this from the location of the first letter of the word and the length of the word. Take the coordinates of the first letter and add the length to the x or y coordinate, depending on the orientation of the word (horizontal or vertical). If the result is greater than 15, which is the size of the board, it returns False, meaning the word is invalid. If the result is not greater than 15, it returns True, which means that the word has been validated. This feature works correctly and passes all tests.




## [0.0.8] - 09-09-2023

### Added

- Modify the file to calculate the word value
- This method calculates the value of a word on the game board, considering the letter and word multipliers. Examine each word cell, add the value of the tokens, and multiply the result by the word multiplier if present. This approach ensures accurate calculation of the word value in the context of the game.



## [0.0.7] - 08-09-2023

### Added

- "Adds a new attribute to the "Scrabble" class called "spin", which will record the spin state of the game. Also, adds an attribute called "turn" to count the total number of turns in the game.

- Introduces two new methods in the "Scrabble" class called "playing" and "next_turn". The "playing" method must return a true value (True) to indicate the end of the game, while the "next_turn" method will take care of increasing the "turn" variable by 1.

- Lastly, create a function called "main".




## [0.0.6] - 2023-08-29

### Added

- Add two essential new features to the 'Board' class.

- Added method that takes a row, column and a tile, and checks if it is possible to place the tile in the corresponding cell on the board.

- Validate if a word placed on the board is valid according to the specified address

## [0.0.5] - 2023-08-29

### Added


- In the player folder I made a change to chip initialization, chip swaps, and score calculation.


## [0.0.4] - 2023-08-29

### Added

I added the uuid function to the scrabble class.
Finally added the wildcard.



## [0.0.3] - 2023-08-28

### Added

- Player
he initializes his hand with 7 chips from the bag. You can also exchange a token with the stock using the exchange method

- Test player

check if when creating a player, he has 7 chips in his hand

checks if the player's chip exchange does not alter his hand or the number of chips in the bag

- BagTiles now wraps all tiles together with their correct values.

- I made a few small changes

## [0.0.2] - 2023-08-28

### Added

- Create the board, cell, players, scrabble classes

- The Board class generates a board with the appropriate dimensions, that is, 15 rows and 15 columns.

- The Cell class represents a cell in a game, such as a word game, and has methods for adding a letter, calculating its value, and taking multipliers into account.

- The Player class is used to create objects that represent the players in a game and has a useful attribute to store the tokens or items that a player owns.

- ScrabbleGame creates a complete Scrabble game. It has a board, a bag of chips, and a list of players.

Each test with its respective code

## [0.0.1] - 2023-08-28

### Added

- Create the Tile and BagTile classes

- The Tile class represents a letter tile with a letter and a value, while the BagTiles class represents a bag of such tiles.

- CLASS TILE

 __init__(self, letter, value) method

This is the constructor of the Tile class, which is called when a new Tile instance is created

-CLASS BAGTILES

__init__(self): Constructor of the class. It is in charge of initializing the bag of chips.

take(self, count): This method allows you to take a specified number of chips from the bag.

put(self, tiles): This method allows you to return chips to the bag.



