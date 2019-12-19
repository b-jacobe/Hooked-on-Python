"""
my_electric_car.py

Import from car class module.

Created: 3-11-19
@author: Brian Jacobe
"""

from car import ElectricCar

my_tesla = ElectricCar("testla", "model s", 2019)
my_tesla.battery.battery_size = 70
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()