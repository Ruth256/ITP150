# 10-5. Programming Poll: Write a while loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file that stores all the responses.

filename = 'poll.txt'

reasons = []

while True:
    reason = input("Why do you like programming? ")
    reasons.append(reason)

    askAgain = input("Do you want to answer again? (y/n) ")
    
    if (askAgain != 'y'):
        break

with open(file_name, 'a') as file_object:
    for reason in reasons:
        file_object.write(reason + "\n")