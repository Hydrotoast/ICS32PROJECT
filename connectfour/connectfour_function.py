import connectfour

def display_board(board: [[str]], column_number, row_number: int)-> None:
    '''display the current board'''
    print(_generate_index_for_board(column_number))
    print(_generate_main_board(board, column_number, row_number))
    
    


#These are private function
def _generate_index_for_board(column_number: int) -> str:
    '''Returns column index for the game board'''
    index = '   '.join(map(lambda x: str(x+1), range(column_number)))
    return index


def _generate_main_board(board: [[str]], column_number: int, row_number: int) -> str:
    '''Returns main board for the game board'''
    for y in range(row_number):
        main_board = '   '.join('.' if board[x][y] == ' ' else board[x][y] for x in range(column_number))
        return main_board

    


