# File: automate_task.py

import os
import shutil

def organize_files(directory):
    """Organizes files in the specified directory into subfolders by file type."""
    if not os.path.isdir(directory):
        print("Invalid directory")
        return

    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            file_ext = os.path.splitext(file_name)[1][1:].lower()
            if file_ext:
                folder = os.path.join(directory, file_ext)
                os.makedirs(folder, exist_ok=True)
                shutil.move(file_path, os.path.join(folder, file_name))
    print(f"Files in {directory} have been organized by type.")

if __name__ == '__main__':
    target_directory = 'downloads'
    organize_files(target_directory)
