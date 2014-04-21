import socket

INVALID = 'INVALID\r\n'
OKAY = 'OKAY\r\n'
    
def user_drop(column: str, s)-> str:
    '''combines user column with DROP and send it to socket'''
    message = 'DROP '+column+'\r\n'
    socket_in = s.makefile('r')
    socket_out = s.makefile('w')
    socket_out.write(message)
    socket_out.flush()
    reply = socket_in.readline()
    return reply

def check_to_continue(reply: str, s):
    ''' if the user's move in invalid, go to user_drop. else continue game'''
    if reply == INVALID:
        print('This is an invalid move. Please enter different column number')
        column = input('Please enter the column number.')
        new_reply = user_drop(column, s)
        AI_move = check_to_continue(new_reply)
    else:
        socket_in = s.makefile('r')
        AI_move = socket_in.readline()[-3]
        socket_in.readline()
    return AI_move

def connect_socket(user_host: str, user_port: int, user_id: str) -> socket:
    s = socket.socket()
    try:
        print('connecting')
        s.connect((user_host, user_port))
        print('connected')
    except:
        s.close()
    return s

def setup_game(s: socket) -> None:
    try:
        socket_in = s.makefile('r')
        socket_out = s.makefile('w')
        socket_out.write('I32CFSP_HELLO '+user_id+'\r\n')
        socket_out.flush()
        reply = socket_in.readline()
        socket_out.write('AI_GAME\r\n')
        socket_out.flush()  
        reply = socket_in.readline()
        print(reply)
    except:
        print('Connection Failed. Closing the socket.')
        s.close()
        
#OfficeHour question: what functions do I need for this module?

if __name__ == '__main__':
    user_host = input('Please specify IP address or a host')
    user_port = int(input('Please enter port'))
    user_id = input('Please enter your user id').strip()
    connect_socket(user_host, user_port, user_id)
    s = connect_socket(user_host, user_port, user_id)
    setup_game(s)
    column = input('Please enter the column number.')
    reply = user_drop(column, s)
    print(reply)
    print(check_to_continue(reply, s))
