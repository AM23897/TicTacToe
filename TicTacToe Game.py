import os
import time

#Define Initial Values for the variables
board = [' ']*10
player1 = 0
player2 = 0
ccount = 1
game_matrix = [' ']*10
game_status = True
start_game = False
rematch = True

#The Main controller method for the game where the whole execution is handled
def tictactoe():
    global board
    global player1
    global player2
    global ccount
    global game_matrix
    global game_status
    global start_game
    global rematch

    while rematch:
        correct_key = get_key_choice()
        if correct_key==True:
            rematch = getInput()
        else:
            break

#Takes choice from user whether the user wants to play again? If the user choice is anything except Y\y, the game ends.
def replay():
    time.sleep(2)
    os.system('cls||clear')
    choice = input('Do you want to play again?')
    if choice=='Y' or choice=='y':
        game_status = True
        return game_status
    else:
        game_status = False
        return game_status

#Clears the board after the game is complete. To reset all the variable and list values for the new match to begin.
def clear_board():
    global board
    global player1
    global player2
    global ccount
    global game_matrix

    board = [' ']*10
    game_matrix = [' ']*10
    player1 = 0
    player2 = 0
    ccount = 0

#Displays the board status after every move taken by each Player.
def display_board():
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-----')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-----')
    print(board[1]+'|'+board[2]+'|'+board[3])

#Takes an input from Player 1 whether the Player chooses X\0 as it's key.
# If the Player 1 makes choice of X as its key then the Player 2 key is set as 0 by default and vice versa.
def get_key_choice():
    key_choice = input('Player 1: Choose X or 0:')
    if key_choice == 'X' or key_choice == 'x' or key_choice == '0':
        if(key_choice == 'X' or key_choice == 'x'):
            player1,player2 = 'X','0'
            print('Player1:' + player1)
            print('Player2:' + player2)
            game_matrix[0] = '#'
            game_matrix[1] = player1
            game_matrix[2] = player2
            game_matrix[3] = player1
            game_matrix[4] = player2
            game_matrix[5] = player1
            game_matrix[6] = player2
            game_matrix[7] = player1
            game_matrix[8] = player2
            game_matrix[9] = player1
            key_value = True
            return key_value
        elif(key_choice == '0'):
            player1,player2 = '0','X'
            print('Player1:' + player1)
            print('Player2:' + player2)
            game_matrix[0] = '#'
            game_matrix[1] = player1
            game_matrix[2] = player2
            game_matrix[3] = player1
            game_matrix[4] = player2
            game_matrix[5] = player1
            game_matrix[6] = player2
            game_matrix[7] = player1
            game_matrix[8] = player2
            game_matrix[9] = player1
            key_value = True
            return key_value
    else:
        key_value = False
        print('Invalid Choice! Please choose a correct Key: X or 0')
        return key_value

#This method takes input from the user for Location to place Key and checks for Win/Tie:
def getInput():
    global board
    global game_status
    global ccount
    while game_status and len(game_matrix)!=1:
        loc_choice = int(input("Enter a Location:"))
        if ccount>9:
            game_status = False
            break
        else:
            if board[loc_choice]=='X' or board[loc_choice]=='0':
                print("Enter a valid choice!")
                continue
            else:
                board[loc_choice] = game_matrix[len(game_matrix)-1]
                game_matrix.pop()
                has_won = checkWin()
                is_full = is_board_full()
                if has_won:
                    display_board()
                    print(board[loc_choice] + ' has Won!')
                    rematch_choice = replay()
                    clear_board()
                    return rematch_choice
                elif is_full:
                    display_board()
                    print('Game Tie!')
                    rematch_choice = replay()
                    clear_board()
                    return rematch_choice
                else:
                    display_board()
                    ccount+=1
                    game_status = True
                    continue

#Here it checks for the Win Status whether the Player has won
def checkWin():
    if (board[7]==board[8]==board[9] and board[7]==board[8]==board[9]!=' ') or \
    (board[4]==board[5]==board[6] and board[4]==board[5]==board[6]!=' ') or \
    (board[1]==board[2]==board[3] and board[1]==board[2]==board[3]!=' ') or \
    (board[7]==board[4]==board[1] and board[7]==board[4]==board[1]!=' ') or \
    (board[8]==board[5]==board[2] and board[8]==board[5]==board[2]!=' ') or \
    (board[9]==board[6]==board[3] and board[9]==board[6]==board[3]!=' ') or \
    (board[7]==board[5]==board[3] and board[7]==board[5]==board[3]!=' ') or \
    (board[1]==board[5]==board[9] and board[1]==board[5]==board[9]!=' '):
        win_status = True
        return win_status
    else:
        win_status = False
        return win_status

#This method checks for Board Status whether the board is full. To check the Tie Status.
def is_board_full():
    if len(game_matrix)==1:
        game_tied = True
        return game_tied
    else:
        game_tied = False
        return game_tied

#Start Game
tictactoe()
