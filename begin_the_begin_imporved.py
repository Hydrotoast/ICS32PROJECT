###begin_the_begin_imporved.py
##
##ICS 32 Spring 2014
##Bohyun Brianna Kim ID: 27523065, Albert Blatter ID: 76229838
##Project #1: Begin the Begin

import os
import shutil

SIZE = 'size'
NAME_ENDING = 'name_ending'
NAME = 'name'

def run_program()-> None:
    '''
    Runs the user interface from start to finish
    '''
    print('Welcome to File Directory.\n')
    while True:
        search_path = input('Please specify the path to the directory you want to search for : \n').strip()
        if not os.path.isdir(search_path):
            print('Invalid direcory input. Please try again.')
        else:
            print('blah')


def search_file(search_path)->list:
    '''searches through the files that satisfies given condition and return the path of each file in the list'''
    file_list = []
    directory_list = _directory_path_list(search_path)
    for element in directory_list:
        try:
            if _check_file(search_path, element):
                file_stats = _file_stats(search_path, element)
                
            elif _check_directory(search_path, element):
            
        except PermissionError:
            pass
    return


#### these are private functions
def _directory_path_list(search_path: str)-> list:
    '''returns the list of directory from given path'''
    directory_list = os.listdir(search_path)
    return directory_list


def _check_file(search_path: str, element: str)-> str:
    if os.path.isfile(os.path.join(search_path, element)):
        return True


def _check_directory(search_path: str, element: str)-> str:
    if os.path.isdir(os.path.join(search_path, element)):
        return True

    
def _file_stats(search_path: str, element: str)->str:
    return os.stat(os.path.join(search_path, element))


def _search_by_option(option: str, file_stats: str, desired_file):
    if option == SIZE:
        
    elif option == NAME_ENDING:

    else:
        

def _check_interesting_file_size(file_stats, desired_file)-> bool:
    if file_stats.st_size >= desired_file:
        return true



def _check_interesting_file_type()

def _check_interesting_file_name()

if __name__ == '__main__':
    run_program()
        
