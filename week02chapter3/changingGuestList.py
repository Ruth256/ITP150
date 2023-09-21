#3-5. Changing Guest List: You just heard that one of your guests can’t make the dinner, so you need to send out a new set of invitations. You’ll have to think of someone else to invite.

#Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#Print a second set of invitation messages, one for each person who is still in your list.

guestList = ['Loydene McWaters', 'Lynn Adams', 'Jaime Buckner']

print(f"You are invited to my dinner {guestList[0]}!")
print(f"You are invited to my dinner {guestList[1]}!")
print(f"You are invited to my dinner {guestList[2]}!")

print(f"Sorry, {guestList[0]} couldn't make it")

guestList[0] = "Oreo"

print(f"You are invited to my dinner {guestList[0]}!")
print(f"You are invited to my dinner {guestList[1]}!")
print(f"You are invited to my dinner {guestList[2]}!")
