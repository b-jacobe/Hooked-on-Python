"""
8_8_user_albums.py

Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.

Created: 2-11-19
@author: Brian Jacobe

"""

def make_album(artist_name, album_title, num_tracks=''):
	music_album = {"artist":artist_name, "album":album_title}
	if num_tracks:
		music_album["tracks"] = num_tracks
	return music_album

message = "\nPlease enter the album information."
message += "Enter 'q' to exit the program at any time."

while True:
	print(message)
	a_name = input("Artist: ")
	if a_name == 'q':
		break
	a_title = input("Album: ")
	if a_title == 'q':
		break
	n_tracks = input("Number of Tracks: ")
	if n_tracks == 'q':
		break

	full_album_info = make_album(a_name, a_title, n_tracks)
	print("\nYou entered: ")



