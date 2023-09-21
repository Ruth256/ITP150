#4-10. Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
# Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
# Print the message The last three items in the list are:. Use a slice to print the last three items in the list.

# Started with 4-1 pizza.py
yummy_pizzas = ['cheese', 'bean', 'round', 'square', 'flimsy']
# first three
print("The first three items in the list are:")
for pizza in yummy_pizzas[0:3]: # or [:3]
    print(pizza.title())

# three from the middle
print("Three items from the middle of the list are:")
for pizza in yummy_pizzas[1:4]: #cheese placement is 0, bean is 1, round is 2, square is 3, and flimsy is 4. 1-3 are the three from the middle.
    print(pizza.title())

# Last three
print("The last three items in the list are:")
for pizza in yummy_pizzas[-3:]:
    print(pizza.title())


