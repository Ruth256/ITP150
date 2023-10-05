# 10-1. Learning Python: Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. Start each line with the phrase In Python you can. . .. Save the file as learning_python.txt in the same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the with block.

import os
#print(os.getcwd())
file_name = 'C:/Users/devon/OneDrive/Desktop/ITP150/week06chapters9_10_11/fileTester.py'

# file_name = 'learning_python.text'
print("Here comes the entire file:")

with open(file_name, 'r') as file_object:
     data = file_object.read()
print(data)

print("Time for Loopin the lines:")
with open(file_name) as file_object:
     for line in file_object:
         print(line.rstrip())

print("Putting them in a list")
with open(file_name) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())