# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at least three names of cats in the first file and three names of dogs in the second file. Write a program that tries to read these files and print the contents of the file to the screen. Wrap your code in a try-except block to catch the FileNotFound error, and print a friendly message if a file is missing. Move one of the files to a different location on your system, and make sure the code in the except block executes properly.

file_names = ['cats.txt', 'dogs.txt']

for file_name in file_names:
    print(f"Working with: {file_name}")

    try:
        with open(file_name) as file_object:
            data = file_object.read()
            print(data)

    except FileNotFoundError:
        print(f"{file_name} file not found! Are you sure that is the file name?")