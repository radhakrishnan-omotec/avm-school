
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']  # create an empty board


def print_board():
    print(' TIC - TAC  - TOE')
    print('-------------')
    print('|', board[0], '|', board[1], '|', board[2], '|')
    print('-------------')
    print('|', board[3], '|', board[4], '|', board[5], '|')
    print('-------------')
    print('|', board[6], '|', board[7], '|', board[8], '|')
    print('-------------')

def make_move(position, player):
    board[position] = player
    

def is_winner(player):
    return (board[0] == player and board[1] == player and board[2] == player) or \
           (board[3] == player and board[4] == player and board[5] == player) or \
           (board[6] == player and board[7] == player and board[8] == player) or \
           (board[0] == player and board[3] == player and board[6] == player) or \
           (board[1] == player and board[4] == player and board[7] == player) or \
           (board[2] == player and board[5] == player and board[8] == player) or \
           (board[0] == player and board[4] == player and board[8] == player) or \
           (board[2] == player and board[4] == player and board[6] == player)
'''           
The escape sequence ("") is used to indicate that the current line of code is continued on the next line. In this code, it is used to split a long line of code into multiple lines for better readability.

The code checks for eight possible winning combinations in the game, and each winning combination is checked on a separate line. To make the code more readable, the code has been split into multiple lines using the escape sequence after each "or" statement. This allows each winning combination to be listed on a separate line, making it easier to read and understand the code.

Without the escape sequence, the entire code would need to be written on a single line, which would make it difficult to read and understand.
'''
def is_board_full():
    return ' ' not in board # will return true if no position has " " in the game board i.e, all positions are occupied

print_board()

while True:
    # Player X's turn
    position = int(input('Player X, choose your position (1-9): ')) - 1
    if board[position] == 'O':
        print("Choose some other position, as this one is already occupied")
        position = int(input('Player X, choose your position (1-9): ')) - 1
    if board[position] == ' ':
        make_move(position, 'X')
        print_board()
        if is_winner('X'):
            print('Player X wins!')
            break
        elif is_board_full():
            print('It is a tie!')
            break

    # Player O's turn
    position = int(input('Player O, choose your position (1-9): ')) - 1
    if board[position] == 'X':
        print("Choose some other position, as this one is already occupied")
        position = int(input('Player O, choose your position (1-9): ')) - 1
    if board[position] == ' ':
        make_move(position, 'O')
        print_board()
        if is_winner('O'):
            print('Player O wins!')
            break
        elif is_board_full():
            print('It is a tie!')
            break 