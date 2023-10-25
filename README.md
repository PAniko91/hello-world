# First Home assignment - Minesweeper_game
This Python program creates a Minesweeper board game that uses inputs from the user to define both the board's dimensions and the number of mines.
It is relying on random plancement techniques to distribute the mines on the board.
The objective of the game is to reveal all the grid squares that are not hiding mines while avoiding detonating any square that conceals a mine beneath.

User Input:
The program engages the user through the console, requesting two specific details at the beginning:
1) The size of the board: Users are instructed to specify the dimensions of the game board, which should be provided as a positive integer representing the number of rows and columns in a square board.
2) Number of Mines settled in the board: User is asked to determine how many mines should be on the board.
If user is providing in both cases invalis inputs, application is going to warn them to act based on the requirements.

Board Setup:
Following the user's input, the app proceeds to create the board according to the specified dimensions. This board is set up as a two-dimensional list, where each cell is initially assigned with a value of 0.

Mine distribution:
The program randomly places the defined number of bombs across the board. These mines are are represented with a value of "X" in the board.

Printing the Board:
After initializing the board and placing mines, the program shows the board to the console. The board is displayed in a grid format, and each cell is identified with coordinates (letters for rows and numbers for columns).
This board will be not visible for the user as this shows the solution. Another table is going to be generated which will be visible for the user and where the user can perform certain actions in order to play the game.
Currently this is not yet implemented, in the next phase this will be detailed out.

Usage:
- Run the Python script (in Command line or Text Editor such as VS Code)
- Provide the board size and number of mines when prompted.
- The program will generate and display the Minesweeper board with random mine placement.
Note: This code does not incorporate the complete Minesweeper game; it only generates the initial board for the game.
