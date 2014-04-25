###connectfour_tools.py
##
##ICS 32 Spring 2014
##Bohyun Brianna Kim ID: 27523065, Albert Blatter ID: 76229838
##Project #2: Send Me On My Way

import collections
import connectfour

POP = 'p'
DROP = 'd'

 
def init_the_game()-> connectfour.ConnectFourGameState:
    '''initialize and print the board'''
    display_board(connectfour.new_game_state().board)
    game_state = connectfour.new_game_state()
    return game_state


def display_board(board: [[str]])-> None:
    '''display the current board'''
    print('  '.join(map(lambda x: str(x + 1), range(connectfour.BOARD_COLUMNS))))
    for y in range(connectfour.BOARD_ROWS):
        print('  '.join('.' if board[x][y] == ' ' else board[x][y] for x in range(connectfour.BOARD_COLUMNS)))
        

def pop_or_drop(game_state: connectfour.ConnectFourGameState, column_number: int) -> connectfour.ConnectFourGameState:
    '''give player an option whether to pop for drop a piece and execute the command'''
    action = input('Do you want to pop or drop? Pop for {}, drop for {}.'.format(POP,DROP)).lower().strip()
    if action == POP:
        move = int(_ask_move(column_number))-1
        print(move)
        new_game_state = connectfour.pop_piece(game_state, move)
        return new_game_state
    elif action == DROP:
        move = int(_ask_move(column_number))-1
        new_game_state = connectfour.drop_piece(game_state, move)
        return new_game_state
    else:
        print('This is invalid move. Please type pop for {}, drop for {}.'.format(POP,DROP))
        new_game_state = pop_or_drop(game_state, column_number)
        return new_game_state

def print_the_winning_player(the_winner: str, player_one: str, player_two: str) -> None:
    '''print the winner of the game'''
    if the_winner == player_one:
        print('{} player, you won!'.format(player_one))
    else:
        print('{} player, you won!'.format(player_two))


#####Private functions######
def _ask_move(column_number: int) -> int:
    '''ask user for column that they want to drop or pop their piece if given situation True. If the situation is False, give an error message.'''
    move = input('Please type in 1~{}'.format(column_number))
    return move

        
        
        
