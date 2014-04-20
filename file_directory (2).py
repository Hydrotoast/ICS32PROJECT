#Kathy Pang 27857688 and Bohyun Kim 27523065 Lab 3 Project 1

import os



def check_file_exists(search_path: str):
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

check_file_exists()

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
    

def search_characteristics():
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

def print_path():
    '''prints file path only'''

def print_first_text_line(file_path: str) -> str:
    '''opens file and prints the first line of text'''
    open_file = None
    try:
        open_file = open(file_path, 'r')
        open_file.readline()
        for line in open_file:
            print(line)
    finally:
        if open_file != None:
            open_file.close()

                
##def copy_file():
##    '''copies a file and stores it in same directory'''
##
##def touch_file():
##    '''modifies the file to last modified timestamp'''
##
##def file_actions():
##    '''asks user which actions should be taken on their file specified'''
##    while True:
##        try:
##            action = int(input('Enter an integer 1-4 to taken an action on a file: \n')
##            if action == 1:
##                print('test')
##                #print_path()
##            elif action == 2:
##                print('test')
##                #print_first_text_line()
##            elif action == 3:
##                print('test')
##                #copy_file()
##            elif action == 4:
##                print('test')
##                #touch_file()
##            else:
##                print('Invliad input. Please enter an integer between 1-4.')
##        except:
##                print('Invalid input. Please enter an integer between 1-4.')
##    
##

def run_program():
    '''opens the program and asks user for directory input'''
    print('Welcome to File Directory. \n')
    while True:
        search_path = input('Please specify the path to the directory you want to search for: \n')
        if os.path.isdir(search_path) == False:
            print('Invalid directory input. Please try again.')
        else:
            search_characteristics()

##run_program()

###if __name__ == '__main__':
