import connectfour

def display_board(board: [[str]])-> None:
    '''display the current board'''
    print('  '.join(map(lambda x: str(x + 1), range(connectfour.BOARD_COLUMNS))))
    for y in range(connectfour.BOARD_ROWS):
        print('  '.join('.' if board[x][y] == ' ' else board[x][y] for x in range(connectfour.BOARD_COLUMNS)))
