"""
8_14_cars.py

Write a function that stores information about a car in a dictionary.
The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the function
with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.

Created: 2-14-19
@author: Brian Jacobe

"""

def car_info(manufactuer, model, **options):
	car = {}
	car['manufactuer'] = manufactuer
	car['model'] = model
	for key, value in options.items():
		car[key] = value
	return car

my_audi = car_info('Audi', 'A4', year=2020, color='black', package='Black Optic')
print(my_audi)