import random

from IPython.display import clear_output
def display_board(board):
    print(board[7]+' | '+board[8]+' | '+board[9])
    print(board[4]+' | '+board[5]+' | '+board[6])
    print(board[1]+' | '+board[2]+' | '+board[3])

values=['#','X','O','X','O','X','O','X','O','X']
display_board(values)

def player_input():

    '''
    OUTPUT =(Player 1 Marker , Player2 marker)
    '''
    marker =''
    
    while marker != 'X' and marker != 'O':
        marker = input('Player 1:Do you want to be X or O ?').upper()     
        

    if marker == 'X':
        return ('X','O')
    else:
        return ('O','X')
               
player1_marker,player2_marker = player_input()

def place_marker(board,marker,position):

    board[position] = marker
place_marker(values,'#',8)
display_board(values)

def win_check(board,mark):
    #Below are the cases to win the game if any of the cases is true one player wins the game
    #Check all rowns and see all share the same marker
    #Check all the coloums and see if all share same marker

    def win_check(board,mark):
        return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

display_board(values)
win_check('test_board','X')

def choose_first():

    flip = random.randint(0,1)

    if flip == 0:
        return 'Player 1'
    else:
        return 'Player 2'
choose_first()
def space_check(board,position):
    
    #Board is empty
    return board[position] == '' 

def full_board_check(board):

    for i in range(1,10):
        if space_check(board,i):
            return False
        #Board is full
        else:
            return True
def player_choice():

    postion = 0

    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position = int (input('Choose a number from :(1-9)'))
        return position



