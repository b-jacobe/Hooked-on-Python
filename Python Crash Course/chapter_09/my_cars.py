"""
my_cars.py

Import from car class module.

Created: 3-11-19
@author: Brian Jacobe
"""

"""Import entire module"""
#from car import Car, ElectricCar
import car

my_audi = car.ElectricCar("audi", "e-tron gt", 2020)
my_audi.battery.battery_size = 85
print(my_audi.get_descriptive_name())
my_audi.battery.describe_battery()
my_audi.battery.get_range()

my_ducati = car.Car("Ducati", "monster 797+", 2020)
print("\n"+my_ducati.get_descriptive_name())