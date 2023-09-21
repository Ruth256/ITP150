#3-7. Shrinking Guest List: You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.

#Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
#Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#Print a message to each of the two people still on your list, letting them know they’re still invited.
#Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

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

print(f"Only two guests allowed {guestList[0]}!")
print(f"Only two guests allowed {guestList[1]}!")
print(f"Only two guests allowed {guestList[2]}!")
print(f"Only two guests allowed {guestList[3]}!")
print(f"Only two guests allowed {guestList[4]}!")
print(f"Only two guests allowed {guestList[5]}!")

print(guestList)

guestList = ['Oreo', 'Loydene McWaters', 'Betty Boop', 'Lynn Adams', 'Jaime Buckner', 'Mr.Rogers']
print(guestList)

popped_guestList = guestList.pop(0)
print(f"Sorry for the uninvite {guestList[0]}!")
popped_guestList = guestList.pop(1)
print(f"Sorry for the uninvite {guestList[1]}!")
popped_guestList = guestList.pop(2)
print(f"Sorry for the uninvite {guestList[2]}!")
popped_guestList = guestList.pop(3)
print(f"Sorry for the uninvite {guestList[3]}!")
print(popped_guestList)




