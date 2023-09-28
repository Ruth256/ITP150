# 8-9. Messages: Make a list containing a series of short text messages. Pass the list to a function called show_messages(), which prints each text message.

def show_messages(messages):
    """Receives a list of messages and prints them"""
    for message in messages:
        print(message.title())


messages = [
    "I need a vacation",
    "My brain is dying",
    "Bread?"
]

show_messages(messages)