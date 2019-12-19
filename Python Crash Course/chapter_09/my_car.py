"""
my_car.py

Import from car class module.

Created: 3-11-19
@author: Brian Jacobe
"""

from car import Car

my_audi = Car('Audi','A4 - Black Optics', 2019)

print(my_audi.get_descriptive_name())
my_audi.odometer_reading = 10
my_audi.read_odometer()