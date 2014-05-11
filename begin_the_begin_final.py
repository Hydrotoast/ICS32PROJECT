#Kathy Pang 27857688 and Bohyun Kim 27523065 Lab 3 Project 1

import os
import shutil


def run_program()-> None:
    '''opens the program and asks user for directory input'''
    print('Welcome to File Directory. \n')
    while True:
        search_path = input('Please specify the path to the directory you want to search for: \n').strip()
        if not os.path.isdir(search_path):
            print('Invalid directory input. Please try again.')
        else:
            search_characteristics(search_path)
            break

       
def search_characteristics(search_path: str)-> None:
    '''asks user which search characteristic they want to use'''
    while True:
        search = input('Enter an integer 1-5 of the search charcteristic you want to use: \n\n1. Search by Name\n2. Search by Name Ending \n3. Search by Size \n4. Restart Program \n5. Exit\n\n')
        search = search.strip()
        if search == '1':
            the_file = input("What exact file do you want to search for? (Ex. 'boo.jpg') \n")
            the_file = the_file.strip()
            interested_path_list = search_through("name", search_path, the_file)
            if not interested_path_list:
                print('The file does not exist.')
            else:
                file_actions(interested_path_list)
                break
        elif search == '2':
            the_file = input("How does the file name end? (Ex. '.py') \n")
            the_file = the_file.strip()
            interested_path_list = search_through("name ending", search_path, the_file)
            if not interested_path_list:
                print('The file does not exist.')
            else:
                file_actions(interested_path_list)
                break
        elif search == '3':
            the_file = int(input("What file size are you looking for? (Ex. '20901') \n"))
            interested_path_list = search_through("size", search_path, the_file)
            if not interested_path_list:
                print('The file does not exist.')
            else:
                file_actions(interested_path_list)
                break
        elif search == '4':
            run_program()
            break
        elif search == '5':
            break
        else:
            print('Invalid input. Please enter an integer between 1-5.')


def file_actions(interested_path_list: list):
    '''asks user which actions should be taken on their file specified'''
    while True: 
        action = input('Enter an integer 1-6 to take an action on a file: \n\n1. Print Path Only \n2. Print First Line of Text \n3. Copy File \n4. Touch File \n5. Restart Program \n6. Exit\n\n\n')
        action = action.strip()
        if action == '1':
            print_path_only(interested_path_list)
            break
        elif action == '2':
            print_first_text_line(interested_path_list)
            break
        elif action == '3':
            copy_file(interested_path_list)
            break
        elif action == '4':
            touch_file(interested_path_list)
            break
        elif action == '5':
            run_program()
            break
        elif action == "6":
            break
        else:
            print('Invalid input. Please enter an integer between 1-6.')


def search_through(function, search_path: str, the_file: str) -> list:
    '''searches through the files of what search characteristic the user inputs'''
    interested_path_list = []
    directory_list = os.listdir(search_path)
    for element in directory_list:
        try:
            if os.path.isfile(os.path.join(search_path, element)):
                file_info = os.stat(os.path.join(search_path, element))
                if function == "size":
                    if file_info.st_size >= the_file:
                        interested_path_list.append(os.path.join(search_path, element))
                elif function == "name ending":
                    if element[-len(the_file):] == the_file:
                        interested_path_list.append(os.path.join(search_path, element))
                elif function == "name":
                    if element == the_file:
                        interested_path_list.append(os.path.join(search_path, element))
            elif os.path.isdir(os.path.join(search_path, element)):
                    new_path = os.path.join(search_path, element)
                    interested_path_list += search_through(function, new_path, the_file)
        except PermissionError:
            pass
    return interested_path_list


def print_path_only(interested_path_list: list):
    '''prints only the path'''
    for element in interested_path_list:
        print(element)


def print_first_text_line(interested_path_list: list) -> str:
    ''' opens file and prints first ilne of text'''
    for element in interested_path_list:
        print(element)
        with open(element, 'r') as the_file:
            first_line = the_file.readline()
            print(first_line)
            #must make a try and except what if we delete file after get the file path?

        
def copy_file(interested_path_list: list)-> None:
    '''copies a file and stores it in the same directory'''
    for element in interested_path_list:
        print(element)
        shutil.copy(element, element + '.dup')
        #must make a try and except what if we delete file after get the file path?


def touch_file(interested_path_list: list):
    '''modify file's last modified timestamp to current datetime'''
    for element in interested_path_list:
        print(element)
        os.utime(element, None)
        #must make a try and except what if we delete file after get the file path?


if __name__ == '__main__':
    run_program()
    print('Exiting Program. Goodbye.')
