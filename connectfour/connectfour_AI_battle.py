import socket
import connectfour
import connectfour_function

def conduct_connectfour_battle(user_host: str, user_port: int, user_id: str) -> None:
    s = socket.socket()
    the_winner = connectfour.NONE
    the_user = connectfour.RED
    try:
        s.connect((user_host, user_port))
        print('Connected! Let the Battle Begin!!!!!')
        game_state = connectfour.new_game_state()
        connectfour_consol.display_board(game_state.board)
        while the_winner == connectfour.NONE:
            if game_state.turn == the_user:
                print('%s this is your turn. Please make a move.' % user_id)
                move = int(input('where will you drop your piece? type 1~7.'))-1
            else:
                
        game_state = connectfour.drop_piece(game_state, move)
        display_board(game_state.board)
        the_winner = connectfour.winning_player(game_state)                
        
    except:
        print('Connection failed. Closing the game.')
    finally:
        s.close()


if __name__ == '__main__':
    user_host = input('Please specify IP address or a host')
    user_port = int(input('Please enter port'))
    user_id = input('Please enter your user id').strip()
    conduct_connectfour_battle(user_host, user_port)
