#Kathy Pang 27857688 and Bohyun Kim 27523065 Lab 3 Project 1

import os    

def run_program()-> None:
    '''opens the program and asks user for directory input'''
    print('Welcome to File Directory. \n')
    while True:
        search_path = input('Please specify the path to the directory you want to search for: \n')
        if os.path.isdir(search_path) == False:
            print('Invalid directory input. Please try again.')
        else:
            search_characteristics(search_path)
            print(search_path)

def search_characteristics(search_path: str)-> None:
    '''asks user which search characteristic they want to use'''
    while True:
        search = input('Enter an integer 1-3 of the search charcteristic you want to use: \n\n1. Search by Name\n2. Search by Name Ending \n3. Search by Size\n\n')
        if search == '1':
            while True:
                try:
                    the_file = input("What exact file do you want to search for? (Ex. 'boo.jpg') \n")
                    search_by_name(search_path, the_file)
                except:
                    print('Invalid input or file does not exist. Please try agian.')
            
        elif search == '2':
            while True:
                try:
                    the_file = input("How does the file name end? (Ex. '.py') \n")
                    search_by_name_ending(search_path, the_file)
                except:
                    print('Invalid input or file does not exist. Please try agian.')
            
        elif search == '3':
            while True:
                try:
                    the_file = input("What file size are you looking for? (20901) \n")
                    search_by_size(search_path, the_file)
                except:
                    print('Invalid input or file does not exist. Please try agian.')
            
        else:
            print('Invliad input. Please enter an integer between 1-3.')    

def search_by_name(search_path: str, the_file: str) -> list:
    ''' searches for files whose name is exactly as input'''

    interested_path_list = []
    directory_list = os.listdir(search_path)
    for element in directory_list:
        if os.path.isfile(os.path.join(search_path,element)):
            if element == the_file:
                interested_path_list.append(os.path.join(search_path,element))                
        else:
            new_path = os.path.join(search_path,element)
            interested_path_list += search_by_name(new_path, the_file)
    return interested_path_list
    
run_program()
