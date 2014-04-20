import os

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

search_by_name('C:\\Python33','search_by_size.py')

