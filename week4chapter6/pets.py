#6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. 
#In each dictionary, include the kind of animal and the owner’s name. 
#Store these dictionaries in a list called pets. 
#Next, loop through your list and as you do, print everything you know about each pet.

pets = []

pet = {
    'ptype': 'dog',
    'pname': 'aurora',
    'age': '9',
    'owner': 'Lisa',
}
pets.append(pet)

pet = {
    'ptype': 'cat',
    'pname': 'pretzel',
    'age': '2',
    'owner': 'Ryan',
}
pets.append(pet)

pet = {
    'ptype': 'dog',
    'pname': 'atalene',
    'age': '5',
    'owner': 'John',
}
pets.append(pet)

for pet in pets:
    print("\nHere is what I know about " +pet['pname'].title() + ":")
    for key, value in pet.items():
        print("\t" +key + ":" +str(value))








