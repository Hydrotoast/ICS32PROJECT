import socket
import connectfour
import connectfour_function
import connectfour_I32CFSP_final


def _conduct_connectfour_battle():
    _welcome_banner()
    
    user_host = 'woodhouse.ics.uci.edu' #input('Please specify your IP address or a host.')
    user_port = 4444 #int(input('Please enter the port.'))
    user_id = 'Burbri' #input('Please enter your user id.').strip()
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
        if connectfour_I32CFSP_final.declare_match(connect_four_connection):
            print('Initializing the game.')
        else:
            print('We could not request the game. sorry!')
            
        game_state = connectfour_tools.init_the_game()

        while the_winner == connectfour.NONE:
            _make_move_please(game_state, user_player, ai_player, user_id)
            
            try:
                action = ask_action()
                move = int(ask_move)
                if not connectfour_tools.drop_or_pop_request(action, move, connect_four_connection):
                    raise connectfour.InvalidConnectFourMoveError
                #update board before ai plays
                ai_message = classify_ai_move(connect_four_connection)
                #update board after ai makes move
                    
                
                
            except ValueError:
                print('This is invalid move. Please type in 1~{}\n'.format(column_number))
            except connectfour.InvalidConnectFourMoveError:
                print('This is invalid move. Please try again.\n')
                
            

    except:
        print('Disconnected! Goodbye!')

def _welcome_banner():
    print('Welcome to the Connect Four Interface.')
    print('Before we begin. We need to get a few thing settled first.')


def _make_move_please(game_state: connectfour.ConnectFourGameState, user_player: str, ai_player: str, user_id: str):
    '''let the user know whose turn it is.'''
    if game_state.turn == user_player:
        print('{}, this is your turn. Please make a move.\n'.format(user_id))
    else:
        print('This is AI turn\'s. Please wait for a bit.')
        
        

if __name__ == '__main__':
    _conduct_connectfour_battle()
