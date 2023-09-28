# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 
#Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size="L", message="I Love Python"):
    """Takes a size of a shirt and the message to be printed on it"""
    print(f"You ordered a {size} shirt with the message {message}")

make_shirt()
make_shirt(size='M')
make_shirt('S', 'Coding Club')