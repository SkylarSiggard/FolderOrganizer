# Folder and File Renaming Script

This Python script allows you to copy a folder and its entire contents (including subfolders and files) while replacing a specific string in the names of the folder, subfolders, and files with a user-defined string.

## Features
- **Recursively copies** the source folder and all its subfolders and files.
- Renames all occurrences of the specified string (`old_string`) in the folder names, subfolder names, and file names.
- Allows the user to provide input for both the string to be replaced and the new string.
- If the user provides no input for the string to replace, it defaults to `replace`.

## Requirements
- Python 3.x
- No external libraries are required beyond Python's standard library.

## How It Works
1. The script asks the user for a string to replace (`old_string`).
    - If no input is provided, it defaults to `"replace"`.
2. The user provides a new string (`new_string`) that will replace the `old_string`.
3. The script then:
    - Copies the folder and all of its contents to a new folder in the same location.
    - Renames the folder, subfolders, and files by replacing all occurrences of `old_string` with `new_string`.

## Usage

1. Place the folder you want to copy and rename in the same directory as the script.
2. Run the script using Python:
    ```bash
    python rename_folders_and_files.py
    ```
3. When prompted, enter:
    - The string you want to replace in folder and file names.
    - The new string to use in the renamed files and folders.
4. The script will:
    - Copy the folder and all its subfolders/files.
    - Rename all instances of the old string to the new one.

### Example

Assume you have a folder named `replace-test` with the following structure:

- `replace-test/ ├── replace-hello.txt └── replace-subfolder/ └── replace-world.txt`

When running the script with the following inputs:

- `old_string = 'replace'`
- `new_string = 'changed'`

The folder structure will become:

- `changed-test/ ├── changed-hello.txt └── changed-subfolder/ └── changed-world.txt`


## Parameters

- **old_string**: The string to replace in the folder, subfolder, and file names (default: `replace`).
- **new_string**: The new string that will replace the old string in the names.

## Notes

- Ensure that the folder to be copied is placed in the same directory as the script before running.
- This script will handle nested subdirectories and files at any depth.
- If the string to be replaced does not exist in the folder or file names, no changes will be made to that part of the structure.
