"""
8_7_album.py

Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.

Add an optional parameter to make_album() that allows you to store the
number of tracks on an album. If the calling line includes a value for the number
of tracks, add that value to the album’s dictionary. Make at least one new
function call that includes the number of tracks on an album.

Created: 2-11-19
@author: Brian Jacobe

"""

def make_album(artist_name, album_title, num_tracks=''):
	music_album = {"artist":artist_name, "album":album_title}
	if num_tracks:
		music_album["tracks"] = num_tracks
	return music_album

artist_1 = make_album("Bruno Mars", "24K Magic", 9)
artist_2 = make_album("Maroon 5", "Songs Aboug Jane", 12)
artist_3 = make_album("Asking Alexandria", "The Black", 12)
print(artist_1)
print(artist_2)
print(artist_3)