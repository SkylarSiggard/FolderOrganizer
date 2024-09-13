import os
import shutil


def copy_and_rename_folder(old_string, new_string):
    src_folder = os.path.join(os.getcwd(), f'{old_string}-folder')

    if not os.path.exists(src_folder):
        print(f"Folder '{old_string}-folder' does not exist.")
        return

    new_folder_name = f'{new_string}-test'
    new_folder_path = os.path.join(os.getcwd(), new_folder_name)

    shutil.copytree(src_folder, new_folder_path)
    print(f'Folder copied to: {new_folder_path}')

    for root, dirs, files in os.walk(new_folder_path, topdown=False):
        for file_name in files:
            if old_string in file_name:
                old_file_path = os.path.join(root, file_name)
                new_file_name = file_name.replace(old_string, new_string)
                new_file_path = os.path.join(root, new_file_name)
                os.rename(old_file_path, new_file_path)
                print(f'Renamed file: {old_file_path} -> {new_file_path}')

        for dir_name in dirs:
            if old_string in dir_name:
                old_dir_path = os.path.join(root, dir_name)
                new_dir_name = dir_name.replace(old_string, new_string)
                new_dir_path = os.path.join(root, new_dir_name)
                os.rename(old_dir_path, new_dir_path)
                print(f'Renamed directory: {old_dir_path} -> {new_dir_path}')

    final_folder_name = new_folder_name.replace(old_string, new_string)
    final_folder_path = os.path.join(os.getcwd(), final_folder_name)
    os.rename(new_folder_path, final_folder_path)
    print(f'Folder renamed to: {final_folder_path}')


old_string = input("Enter the string to replace (default: 'replace'): ") or "replace"
new_string = input("Enter the new string: ")

copy_and_rename_folder(old_string, new_string)
