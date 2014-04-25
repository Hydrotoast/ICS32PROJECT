import socket
import connectfour
import connectfour_function
import connectfour_I32CFSP_final


def _conduct_connectfour_battle():
    _welcome_banner()
    
    user_host = 'woodhouse.ics.uci.edu' #input('Please specify your IP address or a host.')
    user_port = 4444 #int(input('Please enter the port.'))
    user_id = 'Burbri' #input('Please enter your user id.')

    connect_four_connection = connectfour_I32CFSP_final.connect(user_host, user_port)
    print('it worked(test)')
    
    try:
        print('trying')
        if connectfour_I32CFSP_final.login(connect_four_connection, user_id):
            print('Welcome!')
        else:
            print('Login Failed. Goodbye')

    except:
        print('Connection failed! Goodbye!')

def _welcome_banner():
    print('Welcome to the Connect Four Interface.')
    print('Before we begin. We need to get a few thing settled first')


def _

if __name__ == '__main__':
    _conduct_connectfour_battle()
