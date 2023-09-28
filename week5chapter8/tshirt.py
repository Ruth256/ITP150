#8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
#The function should print a sentence summarizing the size of the shirt and the message printed on it.

def make_shirt(size, message):
    """Takes a size of a shirt and the message to be printed on it"""
    print(f"You ordered a {size} shirt with the message {message}")



make_shirt("XL", "Welcome")
make_shirt("welcome", "XL")
#Before creating a key-pair, position mattered
make_shirt(size= "XL", message="Woo")
make_shirt(message="Woo", size="XL")
