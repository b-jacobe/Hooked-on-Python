"""
8_5_cities.py

Write a function called describe_city() that accepts the name of
a city and its country. The function should print a simple sentence, such as
Reykjavik is in Iceland. Give the parameter for the country a default value.
Call your function for three different cities, at least one of which is not in the
default country.

Created: 2-10-19
@author: Brian Jacobe

"""

def describe_city(city, country="United States"):
	print(city + " is in " + country + ".")

describe_city("Burbank")
describe_city("Tokyo", "Japan")
describe_city("Los Angeles")