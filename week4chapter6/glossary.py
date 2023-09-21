# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. 
#Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {
    'sort': 'permanently sorts items',
    'append': 'moves an item to the end',
    'print': 'outputs message',
    'len': 'returns items in a list',
    'index': 'gets the position of an item in a list'
    }
term = 'sort'

print(f"{term}:\n {glossary[term]}")

term = 'append'

print(f"{term}:\n {glossary[term]}")

term = 'print'

print(f"{term}:\n {glossary[term]}")

term = 'len'

print(f"{term}:\n {glossary[term]}")

term = 'index'

print(f"{term}:\n {glossary[term]}")



