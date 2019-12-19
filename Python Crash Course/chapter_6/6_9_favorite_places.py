"""
6_9_pets.py

Make a dictionary called favorite_places. Think of three
names to use as keys in the dictionary, and store one to three favorite places
for each person. To make this exercise a bit more interesting, ask some friends
to name a few of their favorite places. Loop through the dictionary, and print
each person’s name and their favorite places.

Created: 1-28-19
@author: Brian Jacobe

"""

favorite_places = {
	"Brian":"Japan",
	"Nick":"Canada",
	"Ashley":"Korea"
}
for name, place in favorite_places.items():
	print(name.title() + "'s favorite place to visit is " + place + ".")