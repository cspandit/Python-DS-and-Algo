import os
def list_files_recur(base_dir):
    for item in os.listdir(base_dir):
        item_path = os.path.join(base_dir, item)
        if os.path.isdir(item_path):
            list_files_recur(item_path)
        else:
            print(item_path)


def list_files(base_dir):
    for base_folder, dir_list, file_list in os.walk(base_dir):
        for file in file_list:
            if file[-3:] == ".py":
                print(os.path.join(base_folder, file))


list_files('C:\\Python-DS-and-Algo')