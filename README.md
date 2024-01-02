Word Search and Counting Program

This Python program is designed to search for a specific word in text files and count its occurrences. The program allows users to search for the word within a single file or recursively through all text files in a specified directory.

Functions
count_word_occurrences(file_path, target_word)

Counts the occurrences of the target word in the specified file.
Parameters:
file_path: Path to the file to be searched.
target_word: Word to be searched for.
Returns:
The number of occurrences of the target word.
list_files_and_folders(directory)

Lists all files and folders in the specified directory.
Parameters:
directory: Path to the directory to be listed.
Returns:
A list containing the names of files and folders in the directory.
Main Program
Obtains the current directory using os.getcwd() and lists the files and folders in it.
Accepts user input for the file to search (file_to_search) and the target word (target_word).
Calls the appropriate functions based on whether the input is a file or a directory.
If a file is specified, it directly counts the occurrences.
If a directory is specified, it recursively searches through all text files.
Displays the total occurrences and, if found, the occurrences in each file.
Usage
Run the program and follow the prompts:

python word_search_count.py

Enter the file or directory path and the word to search for. The program will provide information on the occurrences in the specified files and folders.

