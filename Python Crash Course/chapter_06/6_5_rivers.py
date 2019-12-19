"""
6_5_rivers.py

Make a dictionary containing three major rivers and the country
each river runs through. One key-value pair might be 'nile': 'egypt'.
• Use a loop to print a sentence about each river, such as The Nile runs
through Egypt.
• Use a loop to print the name of each river included in the dictionary.
• Use a loop to print the name of each country included in the dictionary.

Created: 1-26-19
@author: Brian Jacobe

"""

river_list = {
	"Nile" : "Egypt",
	"Mississippi" : "United States",
	"Amazon" : "Brazil, Peru, Columbia"
}

for river, country in river_list.items():
	print("The " + river + " runs through " + country + ".")

for river in river_list:
	print("River: " + river)

for country in river_list.values():
	print("Country: " + country)