# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the album information correctly.



def make_album(artist, title, numSongs=''):
    """Builds a dictionary of a music album"""
    album = {
        'artist': artist.title(),
        'title': title.title()
    }

    if numSongs:
        album['Number of Songs'] = numSongs

    return album

album = make_album("Pearl Jam", "Ten")

print(album)

album = make_album("guns n roses", "use your illusion")
print(album)

album = make_album("metallica", "black album", "7")
print(album)