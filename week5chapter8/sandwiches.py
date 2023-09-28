# 8-12. Sandwiches: Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sandwich that’s being ordered. Call the function three times, using a different number of arguments each time.

def sandwich_builder(*items):
    """Used by subway to make a great sub. Receives any number of toppings!"""
    print("What toppings do you want on your sub?")

    for item in items:
        print(f"I am adding {item} to your sub...")

    print("Your sub is ready! Would you like to make it a combo?")

sandwich_builder('italian cheese bread', 'pepperoni', 'provolone', 'olives', 'ranch' )

sandwich_builder('whole grain bread', 'cheese')

sandwich_builder('burnt bread', 'cottage cheese', 'beets', 'thumb tacks', 'rawhide', 'dawn dishsoap')