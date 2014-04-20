import os

def search_by_size(search_path: str)->list:

    interested_path_list = []
    the_file = 2097151
    directory_list = os.listdir(search_path)
    for element in directory_list:
        if os.path.isfile(os.path.join(search_path,element)):
            file_info = os.stat(os.path.join(search_path,element))
            if file_info.st_size >= the_file:
                interested_path_list.append(os.path.join(search_path,element))                
        else:
            new_path = os.path.join(search_path,element)
            interested_path_list += search_by_size(new_path)
            
    return interested_path_list



