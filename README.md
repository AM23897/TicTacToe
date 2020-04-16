# TicTacToe Game - Python

This Game is divided into various sections through methods.

# tictactoe():
This Method is executed as soon as the Program execution starts and calls the central methods: get_key_choice() & getInput() 

# get_key_choice():
This Method takes input from the Player to make a choice of Key: X\0
And defines the set of moves for each Players 1 & 2 in a game_matrix List

# getInput():
This method takes input from the user based on 4 conditions:
1.Game Status is True
2.Length of Game Matrix is not equal to 1 as length of Game Matrix 1 indicates the end of the game
3.Any Player has not won the game
4.The game is not in Tie state

The process executes as: 
Whenever the condition 1 & 2 is True, the input is taken from the user for a location to place the key
If the key is anything apart from X\0, it asks for re-entering the location for the key
If the location is a valid location for the key then the key value is set at the location input by the Player
After setting the value at location, a value from the top of the matrix is pop up and thereafter the status of Win/Tie is checked
If the status is either Win/Tie, User is asked for rematch
If the status is neither Win nor Tie, the input is read again for the other Player

# checkWin():
This Method checks the Win Status for the Players after every move.

# is_board_full():
This Method checks after every move whether the Board is full and is there a Tie situation in Game.

# display_board():
This method displays the status of the Board after every move.

# replay():
This method checks whether the user wants to have a rematch.

# clear_board():
This Method resets the Board positions and the Global Variables as well as Lists to initial values to Start the new game from the initial Board position.
