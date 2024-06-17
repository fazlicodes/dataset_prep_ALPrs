import os
import random
import json

random.seed(42)

def list_folders_and_contents(directory):
    folder_names = []
    folder_paths = []
    dataset_info = {
        'train': [],
        'test': [],
        'val': []
    }
    for folder_name in os.listdir(directory):
        folder_path = os.path.join(directory, folder_name)
        if os.path.isdir(folder_path):
            folder_names.append(folder_name)
            folder_paths.append(folder_path)
    
    folder_names.sort()
    train_split = [] # Must contain file path, folder name, and file name
    val_split = [] # Must contain file path, folder name, and file name
    test_split = [] # Must contain file path, folder name, and file name
    for folder in folder_names:
        file_names = []
        file_paths = []
        #Find the files in the folder and add them to the list
        for file_name in os.listdir(os.path.join(directory, folder)):
            file_path = os.path.join(directory, folder, file_name)
            if os.path.isfile(file_path):
                file_names.append(file_name)
                file_paths.append(file_path)


        # Randomly select 60% of the file_path to train_split
        train_split = random.sample(file_paths, int(len(file_paths)*0.6))

        # Randomly select 20% from the remaining file_paths to val_split
        val_split = random.sample(list(set(file_paths) - set(train_split)), int(len(file_paths)*0.2))

        # The remaining file_paths are for test_split
        test_split = list(set(file_paths) - set(train_split) - set(val_split))

        for item in train_split:
            # Add a list containing file path, folder name, and file name to the train list
            dataset_info['train'].append([item, folder_names.index(folder),folder])

        for item in val_split:
        # Add a list containing file path, folder name, and file name to the val list
            dataset_info['val'].append([item, folder_names.index(folder),folder])
        
        for item in test_split:
        # Add a list containing file path, folder name, and file name to the test list
            dataset_info['test'].append([item, folder_names.index(folder),folder])
            

        #Save dataset info as json file
    with open('MLRSNET_new_split.json', 'w') as fp:
        json.dump(dataset_info, fp, indent=4)
            
        # breakpoint()
# Replace 'your_directory_path' with the actual path you want to explore
directory_path = 'datasets/MLRSNet/Images'

if os.path.exists(directory_path) and os.path.isdir(directory_path):
    list_folders_and_contents(directory_path)
else:
    print(f"The specified directory '{directory_path}' does not exist or is not a valid directory.")
