#yackety_protocol
import socket
import collection


YacketyCollection = collections.namedtuple.('YacketyCollection', ['socket','socket_input', 'socket_output'])


def connect(host:str, port:int) ->YacketyCollection:
    yackety_socket = socket.socket()
    yackety_socet.connect((host,port))
    
    yackety_socekt_input = yackety_socket.makefile('r')
    yackety_socekt_output = yackety_socket.makefile('w')

    return YacketyCollection(yackety_socket,Yackety_socket_input, output)


def close(YacketyColection)-> None:
    if connection.socket_input !=None:
        connectiion.socket_input.close

    if connection.socket_output !=None:
        connectiion.socket_output.close

    if connection.socket !=None:
        connectiion.socket.close

    
def hello(connection: YacketyConnection, username: str) -> None:
    _write_line(connection, 'YACKETY_HELL0@{}'.format(username))
    return _readline(connection) == 'YACKETY_HELLO'


def _write_line(connection: YacketyConnection, line_to_write: str) >None:
    connection.socket_output.write(line_to_write +'\r\n')
    connection.socket_output.flush()

    
def _read_line(connection:YacketyConnection):
    connection.socket_input.readline()
somefuctions 
