# Challenge 4

"""
Create a folder called 'myfolder' and inside the folder create a
file named 'myfile.txt'.

Now write a Python program that will follow tasks by:
- Ask the user for a new folder name
- Ask the user if he/she/thhey wants to delete 'myfile.txt'
- Rename the folder 'myfolder' according to user choice
- Delete the file 'myfile.txt' if the user says yes, otherwise do nothing
- Print confirmation of the tasks completed (e.g., "Folder renamed, file deleted")

Bonus additional: If the folder already exists then do not create it again.
Before start, make sure myfolder folder is created it and then move into renaming from myfolder
to the new name provided by the user.
"""

import os
import shutil

# Create a new folder and initial file path
initial_folder = "myfolder"
initial_file = os.path.join(initial_folder, "myfile.txt")

if not os.path.exists(initial_folder):
    os.makedirs(initial_folder)
if not os.path.exists(initial_file):
    with open(initial_file, "w") as f:
        f.write("Hello, this is my file.")

# Ask the user for new folder name
new_folder_name = input("Enter a new folder name (default: 'myfolder'): ").strip() or initial_folder

# Ask user to delete myfile.txt file
delete_file = input("Do you want to delete 'myfile.txt'? (yes/no) (y/n) default: no: ").strip().lower()

# Track actions for final confirmation
actions = []

# Rename the folder
if new_folder_name != initial_folder:
    # If destination already exists, skip rename and inform user
    if os.path.exists(new_folder_name):
        print(f"Cannot rename: destination folder '{new_folder_name}' already exists.")
        actions.append("folder rename skipped")
        final_folder = initial_folder
    else:
        try:
            shutil.move(initial_folder, new_folder_name)
            print(f"Folder renamed to '{new_folder_name}'.")
            actions.append("folder renamed")
            final_folder = new_folder_name
        except Exception as e:
            print(f"Failed to rename folder: {e}")
            actions.append("folder rename failed")
            final_folder = initial_folder
else:
    final_folder = initial_folder
    print("Folder name remains unchanged.")
    actions.append("folder unchanged")

# After potential rename, ensure the file path refers to the current folder
updated_file_path = os.path.join(final_folder, "myfile.txt")

# If the file doesn't exist in the final folder, create it.
if not os.path.exists(updated_file_path):
    with open(updated_file_path, "w") as f:
        f.write("Hello, this is my file.")
    actions.append("file created")

# Delete the file if user confirmed
if delete_file in ("yes", "y"):
    if os.path.exists(updated_file_path):
        try:
            os.remove(updated_file_path)
            print("File 'myfile.txt' deleted.")
            actions.append("file deleted")
        except Exception as e:
            print(f"Failed to delete file: {e}")
            actions.append("file delete failed")
    else:
        print("File 'myfile.txt' not found. Nothing to delete.")
        actions.append("file not found")
else:
    print("File 'myfile.txt' was not deleted.")
    actions.append("file not deleted")

# Final confirmation summary
summary = ", ".join(actions)
print(f"Tasks completed: {summary}")