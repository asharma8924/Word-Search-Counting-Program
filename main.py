# Word Search and Counting Program

import os

def count_word_occurrences(file_path, target_word):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            occurrences = content.lower().count(target_word.lower())
        return occurrences
    except FileNotFoundError:
        return 0

def list_files_and_folders(directory):
    files_and_folders = os.listdir(directory)
    return files_and_folders

# Main Program
if __name__ == "__main__":
    current_directory = os.getcwd()
    print(f"Current directory: {current_directory}")
    files_and_folders = list_files_and_folders(current_directory)
    print("Files and folders in the current directory:")
    for item in files_and_folders:
        print(item)

    file_to_search = input("Enter the name of the file to search (including path if needed): ")
    target_word = input("Enter the word to search for: ")
    total_occurrences = 0

    if os.path.isfile(file_to_search):
        total_occurrences = count_word_occurrences(file_to_search, target_word)
    elif os.path.isdir(file_to_search):
        for root, _, files in os.walk(file_to_search):
            for file in files:
                if file.endswith(".txt"):
                    file_path = os.path.join(root, file)
                    total_occurrences += count_word_occurrences(file_path, target_word)

        print(f"The word '{target_word}' was found {total_occurrences} times in the specified files and folders.")

        if total_occurrences > 0:
            print("Occurrences in files:")
            for root, _, files in os.walk(file_to_search):
                for file in files:
                    if file.endswith(".txt"):
                        file_path = os.path.join(root, file)
                        occurrences = count_word_occurrences(file_path, target_word)
                        if occurrences > 0:
                            print(f"'{target_word}' was found {occurrences} times in {file_path}")
