###connectfour_I32CFSP_final.py
##
##ICS 32 Spring 2014
##Bohyun Brianna Kim ID: 27523065, Albert Blatter ID: 76229838
##Project #2: Send Me On My Way

import collections
import socket
import connectfour
import connectfour_tools


ConnectFourConnection = collections.namedtuple('ConnectFourConnection', ['socket','socket_input','socket_output'])
ConnectFourMessage = collections.namedtuple('ConnectfourMessage', ['username','text'])


def connect(host: str, port: int) -> ConnectFourConnection:
    '''
    Connects to the connectfour server so that the user can play game. Raises error if the connection was not successful.
    '''

    connect_socket = socket.socket()
    connect_socket.connect((host, port))

    connect_socket_input = connect_socket.makefile('r')
    connect_socket_output = connect_socket.makefile('w')

    return ConnectFourConnection(
        socket = connect_socket,
        socket_input = connect_socket_input,
        socket_output = connect_socket_output)


def login(connection: ConnectFourConnection, username: str) -> bool:
    '''
    Logs a user into ConnectFour service. return true if the connection was successful and false otherwise.
    '''
    _write_line(connection, 'I32CFSP_HELLO '+ username)
    return _expect_line(connection, 'WELCOME '+ username)


def declare_match(connection: ConnectFourConnetion) -> bool:
    _write_line(connection, 'AI_GAME')
    return _expect_line(connection, 'READY')


    
### These are Private function
def _read_line(connection: ConnectFourConnection) -> str:
    ''' reads a line of the text sent from the server'''
    return connection.socket_input.readline()[:-1]


def _expect_line(connection: ConnectFourConnection, line_to_expect: str) -> bool:
    '''
    Reads a line of text sent from the server, expecting it to contain a particular text.'''
    return _read_line(connection) == line_to_expect


def _write_line(connection: ConnectFourConnection, line: str) -> None:
    '''
    Writes a line oftext to the server,
    '''
    connection.socket_output.write(line + '\r\n')
    connection.socket_output.flush()
    
    
     
