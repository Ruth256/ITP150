# 8-8. User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album’s artist and title. Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. Be sure to include a quit value in the while loop.

def make_album(artist, title, numSongs=''):
    """Builds a dictionary of a music album"""
    album = {
        'artist': artist.title(),
        'title': title.title()
    }

    if numSongs:
        album['Number of Songs'] = numSongs

    return album
#ends our make_album function

#begins our main program
print("Enter album date or enter quit to stop the program")

while True:
    artist= input("Enter the album's artist: ")
    #kill program if the user enters quit
    if artist == "quit":
        break

    title = input("Enter the album's title:")
    #kill the program if the user enters quit
    if artist == "quit":
        break
    #if we made it this far, they didn't quit. Let's create their album
    album = make_album(artist, title)
    print(album)


# album = make_album("Pearl Jam", "Ten")

# print(album)

# album = make_album("guns n roses", "use your illusion")
# print(album)

# album = make_album("metallica", "black album", "7")
# print(album)