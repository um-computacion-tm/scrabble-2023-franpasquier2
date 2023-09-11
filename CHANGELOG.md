# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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



