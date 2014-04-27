###connectfour_consol_final.py
##
##ICS 32 Spring 2014
##Bohyun Brianna Kim ID: 27523065, Albert Blatter ID: 76229838
##Project #2: Send Me On My Way


import connectfour
import collections
import connectfour_tools


def _main():
    '''function that runs connectfour consol'''
    _greet_to_players(connectfour.RED, connectfour.YELLOW)
    the_winner = connectfour.NONE
    player_one = connectfour.RED
    player_two = connectfour.YELLOW
    column_number = connectfour.BOARD_COLUMNS
    game_state = connectfour_tools.init_the_game()

    while the_winner == connectfour.NONE:
        
        _please_make_move(game_state, player_one, player_two)    

        try:
            action = connectfour_tools.ask_action()
            move = connectfour_tools.ask_move()
            game_state = connectfour_tools.pop_or_drop(game_state, action, move)
            connectfour_tools.display_board(game_state.board)
            the_winner = connectfour.winning_player(game_state)
        except ValueError:
            print('This is invalid move. Please type in 1~{}\n'.format(column_number))
        except connectfour.InvalidConnectFourMoveError:
            print('This is invalid move. Please try again.\n')

    connectfour_tools.print_the_winning_player(the_winner, player_one, player_two)

    
def _greet_to_players(player_one, player_two) -> None:
    '''greet to the users'''
    print('Welcome to ConnectFour! \n')
    print('Player 1, you are the {} player. Player 2, you are the {} player'.format(player_one, player_two))


def _please_make_move(game_state: connectfour.ConnectFourGameState, player_one: str, player_two: str)-> None:
    '''let players know whose turn it is.'''
    if game_state.turn == player_one:
        print('{} player, this is your turn. Please make a move\n'.format(player_one))
    else:
        print('{} player, this is your turn. Please make a move\n'.format(player_two))


if __name__ == '__main__':
    _main()
