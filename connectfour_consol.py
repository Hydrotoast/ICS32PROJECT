import connectfour


def display_board(board: [[str]])-> None:
    '''display the current board'''
    print('  '.join(map(lambda x: str(x + 1), range(connectfour.BOARD_COLUMNS))))
    for y in range(connectfour.BOARD_ROWS):
        print('  '.join('.' if board[x][y] == ' ' else board[x][y] for x in range(connectfour.BOARD_COLUMNS)))
 
def main():
    '''function that runs connectfour consol'''
    
    print('Welcome to ConnectFour! \n')
    print('Player 1, you are the R player. Player 2, you are the Y player')
    the_winner = connectfour.NONE
    player_one = connectfour.RED
    player_two = connectfour.YELLOW
    display_board(connectfour.new_game_state().board)
    game_state = connectfour.new_game_state()

    #play the game until it ends
    while the_winner == connectfour.NONE:
        if game_state.turn == player_one:
            print('Player 1 this is your turn. please make a move')
        else:
            print('Player 2 this is your turn. please make a move')

        try:
            move = int(input('where will you drop your piece? type 1~7'))-1
            game_state = connectfour.drop_piece(game_state, move)
            display_board(game_state.board)
            the_winner = connectfour.winning_player(game_state)
        except ValueError:
            print('Invalid input. Please type integer between 1 and 7')
        except connectfour.InvalidConnectFourMoveError:
            print('The column is full. Please select other column')

    #print the winner
    if the_winner == player_one:
        print('player 1, you won!')
    else:
        print('player 2, you won!')
    
        
        
if __name__ == '__main__':
    main()

