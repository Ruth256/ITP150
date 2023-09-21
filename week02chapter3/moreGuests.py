#3-6. More Guests: You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.

#Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
#Use insert() to add one new guest to the beginning of your list.
#Use insert() to add one new guest to the middle of your list.
#Use append() to add one new guest to the end of your list.
#Print a new set of invitation messages, one for each person in your list.

guestList = ['Loydene McWaters', 'Lynn Adams', 'Jaime Buckner']

print(f"You are invited to my dinner {guestList[0]}!")
print(f"You are invited to my dinner {guestList[1]}!")
print(f"You are invited to my dinner {guestList[2]}!")

print(f"More company to join us {guestList[0]}!")
print(f"More company to join us {guestList[1]}!")
print(f"More company to join us {guestList[2]}!")

guestList.insert(0, 'Oreo')
print(guestList)

guestList.insert(2, 'Betty Boop')
print(guestList)

guestList = []

guestList.append('Oreo')
guestList.append('Loydene McWaters')
guestList.append('Betty Boop')
guestList.append('Lynn Adams')
guestList.append('Jaime Buckner')
guestList.append('Mr.Rogers')

print(guestList)

print(f"You are invited to my dinner {guestList[0]}!")
print(f"You are invited to my dinner {guestList[1]}!")
print(f"You are invited to my dinner {guestList[2]}!")
print(f"You are invited to my dinner {guestList[3]}!")
print(f"You are invited to my dinner {guestList[4]}!")
print(f"You are invited to my dinner {guestList[5]}!")

print(guestList)






