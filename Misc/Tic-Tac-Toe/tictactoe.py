"""
tictactoe.py

This program is a tic-tac-toe
game that involves 2 players.
Once the game board is filled up
regardless of win/lose conditions,
the game will end.

@Author: Brian Jacobe
@Date: 11/10/19
@Last Update: 12/3/19
"""

# Prints out a 3x3 board
def display_board(board):
    show_board = (board[0] + "|" + board[1] + "|" + board[2] + "\n"
                + board[3] + "|" + board[4] + "|" + board[5] + "\n"
                + board[6] + "|" + board[7] + "|" + board[8])
    return show_board

# Grabs player input and assigns 'x' or 'o'
def player_input():
    user_input = input("Please select either 'x' or 'o'.\n")
    return user_input

# Assign marker position based on int 1-8 value
def place_marker(board, marker):
    marker_message = marker + " - player: Please select a position between the values (0-8).\n"
    position = int(input(marker_message))
    availability = space_check(board, position)
    if 0 <= position <= 8:
        if availability == False:
            print("That space is unavailable.\n")
            place_marker(board, marker)
        else:
            board[position] = marker
    else:
        if availability == False:
            print("That value is out of bounds.\n")
            place_marker(board, marker)
    

# Check if win condition is met, mark represents
# player marker
def win_condition(board, mark):
    if board[0] == mark and board[1] == mark and board[2] == mark:
        return True
    elif board[3] == mark and board[4] == mark and board[5] == mark:
        return True
    elif board[6] == mark and board[7] == mark and board[8] == mark:
        return True
    elif board[0] == mark and board[3] == mark and board[6] == mark:
        return True
    elif board[1] == mark and board[4] == mark and board[7] == mark:
        return True
    elif board[2] == mark and board[5] == mark and board[8] == mark:
        return True
    elif board[0] == mark and board[4] == mark and board[8] == mark:
        return True
    elif board[2] == mark and board[4] == mark and board[6] == mark:
        return True
    else:
        return False

# Check if space is available
def space_check(board, position):
    if position < 0 or position >= len(board):
        return False
    elif board[position] == ' ':
        return True
    else:
        return False
    pass

# Check if the board is full
def full_board_check(board):
    counter = 0
    for check in board:
        if check == 'x' or check == 'o':
            counter += 1
    if counter == 9:
        return True
    else:
        return False

# Ask if the players want to play again
def replay():
    error_message = "Invalid entry please try again.\n"
    user_input = input("Would you like to play again? (Y/N)\n")
    if user_input == 'y' or user_input == 'n':
        return user_input
    else:
        return error_message
        
# =================================================================================
divider = "="*30
clear_board = "\n"*100

print(clear_board)
print(divider)
print("Welcome to Tic-Tac-Toe!")
print(divider)

game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
board_state = full_board_check(game_board)
game_state = True
replay_input = None
player_turn = 0
# Establish player markers
player_1 = player_input()
player_2 = None

if player_1 == 'x':
    player_2 = 'o'
else:
    player_2 = 'x'

while game_state == True:
    while board_state == False:
        if player_turn == 0:
            place_marker(game_board,player_1,)
            print(display_board(game_board))
            player_turn = 1
        else:
            place_marker(game_board,player_2)
            print(display_board(game_board))
            player_turn = 0
        winner_1 = win_condition(game_board, player_1)
        winner_2 = win_condition(game_board, player_2)
        if winner_1 == True and winner_2 == False:
            print("Player 1 wins!\n")
            board_state = True
        elif winner_2 == True and winner_1 == False:
            print("Player 2 wins!\n")
            board_state = True
        elif winner_1 == False and winner_2 == False and board_state == False:
            continue
        else:
            print("Draw!\n")
            board_state = True
    replay_input = replay()
    if replay_input == 'n':
        game_state = False
        break
    else:
        game_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
        player_turn = 0
        player_1 = player_input()
        player_2 = None
        print("\n"*100)
        if player_1 == 'x':
            player_2 = 'o'
        else:
            player_2 = 'x'
        print("Welcome back!\n")
        game_state = True