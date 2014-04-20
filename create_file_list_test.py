import os

def createfile_list(search_path: str)->list:

    interested_path_list = []
    the_file = 'Lecture 2.docx'
    directory_list = os.listdir(search_path)
    for element in directory_list:
        if os.path.isfile(os.path.join(search_path,element)):
            if element == the_file:
                interested_path_list.append(os.path.join(search_path,element))                
        else:
            new_path = os.path.join(search_path,element)
            interested_path_list += createfile_list(new_path)
            
    return interested_path_list

createfile_list('C:\\Users\\Boh\\Desktop\\Winter 2014\\women 50b')

