#6-4. Glossary 2: Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values.
#When you’re sure that your loop works, add five more Python terms to your glossary. 
#When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    'sort': 'permanently sorts items',
    'append': 'moves an item to the end',
    'print': 'outputs message',
    'len': 'returns items in a list',
    'index': 'gets the position of an item in a list',
    'reverse':'reverses items',
    'whitespace': 'nonprinting character',
    'f': 'formats',
    'strings': 'a series of characters',
    'constants': 'where variable values stay the same'

    }
#term = 'sort'

#print(f"{term}:\n {glossary[term]}")

for term, information in glossary.items():
    print(f"{term}:\n {information}")

#term = 'append'

#print(f"{term}:\n {glossary[term]}")

#term = 'print'

#print(f"{term}:\n {glossary[term]}")

#term = 'len'

#print(f"{term}:\n {glossary[term]}")

#term = 'index'

#print(f"{term}:\n {glossary[term]}")