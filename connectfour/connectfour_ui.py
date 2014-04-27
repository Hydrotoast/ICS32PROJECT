###connectfour_ui.py
##
##ICS 32 Spring 2014
##Bohyun Brianna Kim ID: 27523065, Albert Blatter ID: 76229838
##Project #2: Send Me On My Way


import socket
import connectfour
import connectfour_function
import connectfour_I32CFSP_final
import connectfour_tools


def _conduct_connectfour_battle():
    ''' conduct the battle with AI'''
    _welcome_banner()
    
    user_host = input('Please specify your IP address or a host.').strip()
    user_port = int(input('Please enter the port.'))
    user_id = input('Please enter your User ID.').strip()
    the_winner = connectfour.NONE
    user_player = connectfour.RED
    ai_player = connectfour.YELLOW
    column_number = connectfour.BOARD_COLUMNS
    row_number = connectfour.BOARD_ROWS

    connect_four_connection = connectfour_I32CFSP_final.connect(user_host, user_port)    

    try:
        if connectfour_I32CFSP_final.login(connect_four_connection, user_id):
            print('Welcome, {}!'.format(user_id))
        else:
            print('Login Failed.')
        #consdering to erase the "else" what do you think?
        if connectfour_I32CFSP_final.declare_match(connect_four_connection):
            print('Initializing the game.')
        else:
            print('Battle request Failed.')
        #consdering to erase the "else" what do you think?    
        game_state = connectfour_tools.init_the_game()

    
        while the_winner == connectfour.NONE:
            _make_move_please(game_state, user_player, ai_player, user_id)
            
            try:
                action = connectfour_tools.ask_action()
                move = connectfour_tools.ask_move()
                if not connectfour_I32CFSP_final.drop_or_pop_request(action, move, connect_four_connection):
                    raise connectfour.InvalidConnectFourMoveError
                game_state = connectfour_tools.pop_or_drop(game_state, action, move)
                connectfour_tools.display_board(game_state.board)
                the_winner = connectfour.winning_player(game_state)
                
                _make_move_please(game_state, user_player, ai_player, user_id)
                ai_message = connectfour_I32CFSP_final.classify_ai_move(connect_four_connection)
                game_state = connectfour_tools.pop_or_drop(game_state, ai_message.action, ai_message.move)
                connectfour_tools.display_board(game_state.board)
                the_winner = connectfour.winning_player(game_state)
                
            except ValueError:
                print('This is invalid move. Please type in 1~{}\n'.format(column_number))

            except connectfour.InvalidConnectFourMoveError:
                print('This is invalid move. Please try again.\n')

                
        _print_the_winning_player(the_winner, user_player, ai_player)

    except:
        print('Disconnected! Goodbye!')


def _welcome_banner():
    '''greet the user with welcoming words'''
    print('Welcome to the Connect Four Interface.')
    print()
    print('Before we begin. We need to get a few thing settled first.')
    print()


def _make_move_please(game_state: connectfour.ConnectFourGameState, user_player: str, ai_player: str, user_id: str):
    '''let the user know whose turn it is by printing out whose turn it is'''
    if game_state.turn == user_player:
        print('{}, this is your turn. Please make a move.\n'.format(user_id))
    else:
        print('This is AI turn\'s. Please wait for a bit.')


def _print_the_winning_player(the_winner: str, player_one: str, player_two: str) -> None:
    '''print the winner of the game'''
    if the_winner == player_one:
        print('Congratulation, {}! You defeated the evil AI!!!'.format(user_id))
    else:
        print('Shame on you! AI defeated you. Practice more to defeat it next time.')
        

if __name__ == '__main__':
    _conduct_connectfour_battle()
