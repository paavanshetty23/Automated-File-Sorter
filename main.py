import os
import shutil
from datetime import datetime

# Input for the source directory
source_dir = input("Enter the source directory: ")


target_dirs = {
    'Documents': ['.pdf', '.docx', '.txt'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Videos': ['.mp4', '.mkv', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar', '.7z'],
}

try:
   
    for folder in target_dirs.keys():
        folder_path = os.path.join(source_dir, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    
    for file_name in os.listdir(source_dir):
        file_path = os.path.join(source_dir, file_name)
        
        if os.path.isdir(file_path):
            continue
        
        _, ext = os.path.splitext(file_name)

        moved = False
        for folder, extensions in target_dirs.items():
            if ext.lower() in extensions:
                shutil.move(file_path, os.path.join(source_dir, folder, file_name))
                moved = True
                break
        
        if not moved:
            misc_folder = os.path.join(source_dir, 'Miscellaneous')
            if not os.path.exists(misc_folder):
                os.makedirs(misc_folder)
            shutil.move(file_path, os.path.join(misc_folder, file_name))

    
    print("Files have been successfully sorted.")

except Exception as e:
    print(f"An error occurred: {e}")
