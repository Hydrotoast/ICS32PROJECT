import os

def search_by_name_ending(search_path: str)->list:

    interested_path_list = []
    the_file = '.py'
    length = -len(the_file)
    directory_list = os.listdir(search_path)
    for element in directory_list:
        if os.path.isfile(os.path.join(search_path,element)):
            if element[length:] == the_file:
                interested_path_list.append(os.path.join(search_path,element))                
        else:
            new_path = os.path.join(search_path,element)
            interested_path_list += search_by_name_ending(new_path)
            
    return interested_path_list

search_by_name_ending('C:\\Python33')
