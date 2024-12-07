import os
import shutil
from datetime import datetime, timedelta
#import sys
import argparse

def find_date():
    today = datetime.now()
    #print (today)
    yesterday = str(today - timedelta(days=1))
    #print (yesterday.split(" ")[0])
    yesterday_date = yesterday.split(" ")[0]
    return yesterday_date

def get_variables():
    # Get the first argument passed to the script (after the script name)
    # if len(sys.argv) > 1:
    #     var = sys.argv[1]
    #     LOCATION = var[0].upper() + var[1:]
    #     print(f"Received variable: {LOCATION}")
    # else:
    #     print("No location how variable provided")
    parser = argparse.ArgumentParser(description="Add folder name")

    parser.add_argument('--arg1', type=str, help="Folder name")
    #parser.add_argument('arg2', type=str, help="Test")
    args = parser.parse_args()
    var = str(args.arg1)[0].upper()+str(args.arg1)[1:]
    print (var)
    return var

def move_and_rename_files(root_dir):
    """
    Moves all files from nested subdirectories to the root directory and renames them
    by prefixing with their relative path.

    :param root_dir: The root directory containing subdirectories and files.
    """
    for subdir, _, files in os.walk(root_dir, topdown=False):
        if subdir == root_dir:
            # Skip the root directory itself
            continue
        
        # Get the relative path of the current subdir with respect to root_dir
        relative_path = os.path.relpath(subdir, root_dir)
        sanitized_path = relative_path.replace(os.sep, "_")  # Replace path separators with underscores
        
        # Process each file in the current subdirectory
        for file in files:
            source_path = os.path.join(subdir, file)
            
            # Create a new file name by prefixing with the sanitized relative path
            new_file_name = f"{sanitized_path}_{file}"
            dest_path = os.path.join(root_dir, new_file_name)
            
            # Move the file to the root directory with the new name
            shutil.move(source_path, dest_path)
            print(f"Moved and renamed: {source_path} -> {dest_path}")
        
        # Optionally remove the now-empty subdirectory
        if not os.listdir(subdir):
            os.rmdir(subdir)
            print(f"Removed empty directory: {subdir}")

# Specify the root directory
root_directory = f"/ROOT_DIRECTORY_PATH/{get_variables()}/{find_date()}"
#find_date()
#get_variables()
#print(root_directory)
move_and_rename_files(root_directory)
