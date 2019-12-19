"""
6_10_cities.py

Make a dictionary called cities. Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country, population, and fact. Print the name of each city and all of the information
you have stored about it.

Created: 1-28-19
@author: Brian Jacobe

"""

cities = {
	"Burbank":{
		"State": "CA",
		"Country":"United States",
		"Fact":"I went to grade school and high school in this city."
	},
	"Glendale":{
		"State": "CA",
		"Country":"United States",
		"Fact":"I want to move here when I leave SF."
	},
	"Los Angeles":{
		"State":"CA",
		"Country":"United States",
		"Fact":"Riot Games HQ is in this city!"
	}
}

for city, info in cities.items():
	print("\nCity: " + city)
	print("\tState: "+ info["State"])
	print("\tCountry: "+ info["Country"])
	print("\tFact: "+ info["Fact"])