import socket

    
def user_drop(column: str, socket_out: file)-> None:
    '''combines user column with DROP and send it to socket'''
    message = 'DROP '+column+'\r\n'
    socket_out.write(message)
    socket_out.flush()

def connect_socket(user_host: str, user_port: int, user_id: str) -> socket:
    s = socket.socket()
    try:
        print('connecting')
        s.connect((user_host, user_port))
        print('connected')
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
    finally:
        print('closing')
        s.close()
        print('Good Bye!')        
    
#OfficeHour question: what functions do I need for this module?

if __name__ == '__main__':
    user_host = input('Please specify IP address or a host')
    user_port = int(input('Please enter port'))
    user_id = input('Please enter your user id').strip()
    connect_socket(user_host, user_port, user_id)
