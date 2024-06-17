import os
import random

def list_folders_and_contents(directory):
    folder_names = []
    folder_paths = []
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        if os.path.isdir(folder_path):
            folder_names.append(folder_name)
            folder_paths.append(folder_path)
    
    folder_names.sort()
    for folder in folder_names:
        print(f"{folder}")
        # file_names = []
        # #Find the files in the folder and add them to the list
        # for file_name in os.listdir(os.path.join(directory, folder)):
        #     file_path = os.path.join(directory, folder, file_name)
        #     if os.path.isfile(file_path):
        #         file_names.append(file_name)

        # breakpoint()


            
        
# Replace 'your_directory_path' with the actual path you want to explore
directory_path = '/l/users/sanoojan.baliah/Felix/dataset_prep/datasets/MLRSNet/Images'

if os.path.exists(directory_path) and os.path.isdir(directory_path):
    list_folders_and_contents(directory_path)
else:
    print(f"The specified directory '{directory_path}' does not exist or is not a valid directory.")