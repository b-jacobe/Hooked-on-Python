"""
8_6_city_names.py

Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the value
that’s returned.

Created: 2-11-19
@author: Brian Jacobe

"""

def city_country(city, country):
		location = city + ', ' + country 
		return location.title()

print(city_country("Burbank","United States"))
print(city_country("Tokyo","Japan"))
print(city_country("Los Angeles","United States"))