# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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

put(self, tiles): Este método permite devolver fichas a la bolsa.

## [0.0.2] - 2023-08-28

### Added

- Create the board, cell, players, scrabble classes

- The Board class generates a board with the appropriate dimensions, that is, 15 rows and 15 columns.

- The Cell class represents a cell in a game, such as a word game, and has methods for adding a letter, calculating its value, and taking multipliers into account.

- The Player class is used to create objects that represent the players in a game and has a useful attribute to store the tokens or items that a player owns.

- ScrabbleGame creates a complete Scrabble game. It has a board, a bag of chips, and a list of players.

Each test with its respective code
