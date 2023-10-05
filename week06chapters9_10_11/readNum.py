import json

with open('favNum.json') as file_object:
    favNum = json.load(file_object)

print(f"Your favorite number is {favNum}")