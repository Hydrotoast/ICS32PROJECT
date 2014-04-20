import os

def run_program()-> None:
    '''opens the program and asks user for directory input'''
    print('Welcome to File Directory. \n')
    while True:
        search_path = input('Please specify the path to the directory you want to search for: \n')
        if os.path.isdir(search_path) == False:
            print('Invalid directory input. Please try again.')
        else:
            search_characteristics()


def search_characteristics()-> None:
    '''asks user which search characteristic they want to use'''
    while True:
        try:
            search = int(input('Enter an integer 1-3 of the search charcteristic you want to use: \n\n1. Search by Name\n2. Search by Name Ending \n3. Search by Size\n\n'))
            if search == 1:
                search_by_name()
            elif search == 2:
                print('2')
                #search_name_ending()
            elif search == 3:
                print('3')
                #search_by_size()
            else:
                print('Invliad input. Please enter an integer between 1-3.')    
        except:
            print('Invalid input. Please enter an integer between  1-3.')


def search_by_name() -> str:
    ''' searches for files whose name is exactly as input'''
    while True:
        try:
            the_file = input("What exact file do you want to search for? (Ex. 'boo.jpg') \n")
            
        except:
            print('Invalid input or file does not exist. Please try agian.')
            
def search_name_ending():
    ''' searches for files with name ending specified'''
    while True:
        try:
            the_file = input("What file ending do you want to search for? (Ex.'.docx') \n")
        except:
            print('Invalid input or file does not exist. Please try agian.')

def search_by_size():
    ''' searches for files with size specified'''
    while True:
        try:
            the_file = input("What file size do you want to search for?")
        except:
            print('Invalid input or file does not exist. Please try agian.')
            
def create_file_list(search_path: str) -> :
    ''''''
    #use os.path.join
    file_list = []
    directory = os.listdir(search_path)
    for element in directory:
        if os.path.isfile(element):
            if element == the_file:
                file_list.append(element)
            else:
                break
        else:
            file_list.append(check_file_exists(element)) #if not a file, it is a folder. Thus, we search through all the folders to find files/ a file that we want


run_program()
