"""
review.py

Module file to review Python Crash Course
book.

Created: 1-12-19
Last Updated: 7-11-19
@author: Brian Jacobe

"""
import pizza

# ============= PYTHON 3+ FEATURES =============
# f-string Python 3.6
first_name = "Brian"
last_name = "Jacobe"
age = 28
print(f"My name is {first_name} {last_name} and i'm {age} years old.")

# ============= LIST & LIST COMPREHENSION =============

review_list = ['apple', 'orange', 'pear']

del review_list[0]
review_list.insert(0, 'grapes')
review_list.append('kiwi')
print(review_list)

print("Here are a list of fruits:")
for i in review_list:
	print(i)

# List Comprehension
# Note - setting i==1, i wlll be defined as a boolean
c_list = [i for i in range(1,11)]
print(c_list)

# ============= SLICE =============

s_list = []
for i in range(0,10):
	i += 1
	s_list.append(i)

# Slice [start:stop:step]
print(s_list[3:10:2])
print(s_list[3:])
print(s_list[:3])
print(s_list[-3:])

# Looping through a Slice
# Helpful if you know the position
l_list = ['Deborah', 'Adam', 'Jonathan', 'Aygun', 'Khalil']
print("Here are the last three players on my team:")
for i in l_list[-3:]:
	print(i)

# Copying List
comp_list = [i for i in range(0,11)]
copy_list = comp_list[:]
print(sum(copy_list))
print(sum(comp_list))


# ============= IF-ELIF-ELSE STATEMENTS =============
my_cars = ['Audi Q7 S', 'Audi A4 Black Optic', 'Ducati Monster 1200 S']

for i in my_cars:
	if i == 'Audi Q7 S':
		print('My SUV: ' + i)
	elif i == 'Audi A4 Black Optic':
		print('My daily work car: ' + i)
	else:
		print('On the weekend, I drive my motorcycle, a ' + i)

m_value = 1200000
c_value = str(m_value)
c_list = []
print(3 % 3)

for i in c_value:
	if len(c_list) % 3 == 0 and len(c_list) != len(c_value):
		c_list.append(i)
		print(str(len(c_list)) + " " + str(i))
	else:
		c_list.append(i)
print(len(c_list))

user_info = {"name":"Brian Anthony Jacobe", "net worth":1200000}
print(user_info)
print("Brian's Net Worth is: $" + str(user_info["net worth"]))
print("Let's ride like we're in TRON Legacy!")


# ============= PALINDROME TEST =============

p_word = "kayak"
p_list = []
for i in p_word:
	p_list.append(i)

r_list = p_list[:]
r_list.reverse()

if r_list == p_list:
	print("This word is a palindrome!")
else:
	print("This word is not a palindrome.")

# ============= DICTIONARY =============
user_info = {
	"user_name":"bjacobe",
	"salary":120000,
	"dogs":"yes"
	}

# Accessing values in dictionary
print(user_info["user_name"])
print(user_info["salary"])
print(user_info["dogs"])

# Adding new key-value pairs
user_info["vehicles"] = 3
print(user_info["vehicles"])

# Modifying values in a dictionary
user_info["salary"] = 250000
print(user_info["salary"])

# Removing key-value pairs
del user_info["dogs"]
print(user_info)

# Looping through all key-value pairs
user_info = {
	"Brian":1,
	"Jonathan":117,
	"Aygun":50,
	"Deborah":17
	}

# Sorted function to get a copy of key-values in order
for name, number in sorted(user_info.items()):
	print("\nUser: " + name)
	print("Favorite Number: " + str(number) + "\n")

# Sorted function to get a copy of keys in order
for name in sorted(user_info.keys()):
	print("User: " + name)

# Sorted function to get a copy of values in order
for number in sorted(user_info.values()):
	print("Favorite Number: " + str(number))

# set() allows python to identify unique items in the list
for number in set(user_info.values()):
	print("Unique Number: " + str(number))

# Nesting
user_list = []
for user_count in range(30):
	new_user = {
		"user_name":"user"+str(user_count), 
		"user_id":str(0000) + str(user_count),
		"user_password":"pass" + "_" + str(user_count),
		"user_points":10
	}
	user_list.append(new_user)
print(user_list)

for user in user_list[0:5]:
	if user["user_points"] == 10:
		user["user_points"] = 15
	elif user["user_points"] == 15:
		user["user_points"] = 20
print(user_list)

# List within a dictionary
user_order = {
	"id": 932234,
	"items": ["GALAXY S10+","Sony RX100 VI"]
}
print(user_order)

# Dictionary within a dictionary

jacobe_asset = {
	"Vehicles": {
		"Luxury Small Car": "Audi A4 Black Optic", 
		"Luxury SUV": "Audi Q7 S",
		"Motorcycle":"Ducati Monster 1200 S"
		},
	"Real Estate":{
		"Home":"House",
		"Bedrooms":3,
		"Value":1200000
		}
}

print("\n" + str(jacobe_asset))

# ============= WHILE LOOP =============

current_number = 1
while current_number <= 5:
	print(current_number)
	current_number += 1

"""
# User input and while loop
### PALINDROME REVIEW ###
user_input = ""
original_list = []
prompt = "\nPalindrome Test:"
prompt += "\nEnter a word to see if it's a palindrome or not."
prompt += "\nEnter 'quit' to end the program."

while user_input != "quit":
    user_input = input(prompt)
    if user_input != "quit":
        for i in user_input:
            original_list.append(i)
            reverse_list = original_list[:]
            reverse_list.reverse()
        if original_list == reverse_list:
            print("Pass: This word is a palindrome.")
        else:
            print("Fail: This word is not a palindrome.")
        original_list = []

# Import / break / while loop
import random
number = "\nPick a number between 1 and 5."
number += "\nThe computer will try to guess your number!"
number += "\nEnter '0' to exit the program.\n"
while number != 0:
    user_value = input(number)
    computer_value = random.randint(1,5)
    if int(user_value) == 0:
        break
    else:
        print("You entered: " + str(user_value))
        print("Computer entered: " + str(computer_value))
        if computer_value == int(user_value):
            print("Match!")
        else:
            print("Not a match, try again!")
"""

# Using continue in loop
my_value = 0
while my_value < 10:
	my_value += 1
	# Prints odd numbers
	if my_value % 2 == 0:
		continue
	else:
		print(my_value)

# Using while loop with multiple lists
unverified_users = ['Brian', 'Maxine']
verified_users = []
while unverified_users:
	users = unverified_users.pop()
	print("Verifying user: " + users.title())
	verified_users.append(users)
print("The following users have been verified:")
for verified_user in verified_users:
	print(verified_user.title())

# Removing all instances of a string in a list

pets = ["dog", "cat", "cat", "bird", "reptile", "cat", "goldfish", "rabit"]

while "cat" in pets:
	pets.remove("cat")
print(pets)

# Filling a dictionary with user input
"""
# Initialize an empty dictionary
# Set a flag to indicate the survey is active
survey = {}
survey_active = True

while survey_active:
	name = input("\nWhat is your name? ")
	response = input("What is your favorite car brand? ")

	survey[name] = response

	repeat = input("Would you like to ask another person for their response? (yes/no) ")
	if repeat == "no":
		survey_active = False

print("\n --------- Survey Results ---------")
for name, response in survey.items():
	print(name + " favorite car brand is: " + response + ".")
"""
# ============= FUNCTION =============

# Function - w/o parameter
def greet_users():
	print("Hello User!")

greet_users()

# Function - w/ single parameter

def greet_users(user):
	print("Hello, " + user.title() + "!")

greet_users("Brian")

# Positional Arguments

def game_price(tax, cost):
	sales_tax = tax * 0.010
	sales_tax_value = sales_tax * cost
	sub_total = sales_tax_value + cost
	print(sub_total)

game_price(9.25, 59.99)

# Keyword Arguments

game_price(cost = 59.99, tax = 8.75)

# Default Values

def game_price(tax, cost=59.99):
	sales_tax = tax * 0.010
	sales_tax_value = sales_tax * cost
	sub_total = sales_tax_value + cost
	print(sub_total)

game_price(7.50)

# Return a simple value

def get_formated_name(first_name, last_name):
	# Return a full name, neatly formatted.
	full_name = first_name + " " + last_name
	return full_name.title()

user = get_formated_name("brian", "jacobe")

print(user)

def get_formated_name(first_name, last_name, middle_name=''):
	if middle_name:
		full_name = first_name + ' ' + middle_name + ' ' + last_name
	else:
		full_name = first_name + ' ' + last_name
	return full_name.title()

user = get_formated_name("Brian", "Jacobe")
print(user)
user = get_formated_name("Brian", "Jacobe", "Tenedero")
print(user)

# Returning a dictionary

def build_person(first_name, last_name, age=''):
	person = {"First":first_name, "Last":last_name}
	if age:
		person['age'] = age
	return person
person = build_person("Brian", "Jacobe", 27)
print(person)

# Function in conjunction with while loop
"""
def get_formated_name(first_name, last_name):
	full_name = first_name + ' ' + last_name
	return full_name.title()

while True:
	print("\nPlease tell me your name.")
	f_name = input("First Name: ")
	l_name = input("Last Name: ")
	full_name = get_formated_name(f_name, last_name)

	print("\nHello, " + full_name + "!")
"""

def greet_users(names):
	for name in names:
		msg = "Hello, " + name.title() + "!"
		print(msg)

user_list = ["Brian", "Adam", "Aygun"]
print(greet_users(user_list))

# Every function should have one specific job

# SIMULATE PRINTING DESIGN & MOVE TO COMPLETED MODEL WHEN COMPLETE
def print_models(unprinted_designs, completed_models):
	while unprinted_designs:
		current_design = unprinted_designs.pop()
		print("Printing model: " + current_design)
		completed_models.append(current_design)

# DISPLAY COMPLETED MODELS THAT WERE PRINTED
def show_completed_models(completed_models):
	print("\nThe following models have been printed:")
	for models in completed_models:
		print(models)

unprinted_designs = ["project_jacobe", "LoL Pro", "Portfolio"]
completed_models = []
"""
print(print_models(unprinted_designs, completed_models))
print(show_completed_models(completed_models))
"""

# Sending copy of list to prevent list modification (slice)
print(print_models(unprinted_designs[:], completed_models))
print(show_completed_models(completed_models))
print(unprinted_designs)
print(completed_models)

# Passing an arbitrary number of arguments
def make_pizza(*toppings):
	"""Print the list of toppings that have been requested"""
	return toppings

print(make_pizza('pepperoni', 'mushroom'))
print(make_pizza('cheese'))

# Mixing positional and arbitrary arguments
# Note that arbitrary arguments are placed last
"""
def make_pizza(size, *toppings):
	print("\nMaking a " + str(size) + "-inch pizza with the following toppings: ")
	for topping in toppings:
		print("- " + topping)
	return 0
"""

make_pizza(16, "pepperoni", "mushroom", "cheese")

# Using Arbitrary Keyword Arguments
def build_profile(first, last, **user_info):
	"""Build a Dictionary containing user info"""
	profile = {}
	profile["first"] = first
	profile["last"] = last
	for key, value in user_info.items():
		profile[key] = value
	return profile

user_profile = build_profile('Brian', 'Jacobe', age=27,occupation="Software Engineer")
print(user_profile)
# Importing an entire module
print(pizza.make_pizza(16, 'pepperoni'))
print()

# ============= CLASS =============
# NOTE: functions = lowercase, class = uppercase
# 		Every function within a class is a 'method'
class Dog():
	"""Dog Model"""

	def __init__(self, name, age):
		"""Initialize name and age attributes"""
		self.name = name
		self.age = age

	def sit(self):
		"""Simiulate dog sitting in response to command"""
		print(self.name.title() + " is now sitting.")
		return ""

	def roll_over(self):
		"""Simulate rolling over in response to a command"""
		print(self.name.title() + " rolled over!")
		return ""

# Making an Instance from a class

my_dog = Dog('Max',3)

print("My dog's name is " + my_dog.name.title() + ".")
print(my_dog.sit())
print(my_dog.roll_over())

# Inheritence

class Car(object):
	"""A simple attempt to represent a car."""

	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year
		self.odometer_reading = 0

	def get_descriptive_name(self):
		long_name = str(self.year) + ' ' + self.make + ' ' + self.model
		return long_name.title()

	def read_odometer(self):
		print("This car has " + str(self.odometer_reading) + " miles on it.")

	def update_odometer(self, mileage):
		if mileage >= self.odometer_reading:
			self.odometer_reading = mileage
		else:
			print("You can't roll back an odometer!")

	def increment_odometer(self, miles):
		self.odometer_reading += miles

# Inheritence in Python 2.7+
"""
class Car(object):
	def __init__(self, make, model, year):
		--snip--

class ElectricCar(Car):
	def __init__(self, make, model, year):
		super(ElectricCar, self).__init__(make, model, year) 
		--snip--
"""

# Inheritence as attributes
class Battery():
	"""A simple attempt to model a battery for an electric car."""
	def __init__(self, battery_size=70):
		self.battery_size = battery_size

	def describe_battery(self):
		"""Returns a statement about the battery size"""
		battery = "This car has a " + str(self.battery_size) + "-kWh battery."
		return battery

	def get_range(self):
		"""Returns a statement about the range this battery provides"""
		if self.battery_size <= 70:
			range = 240
		elif self.battery_size > 70 and self.battery_size <= 85:
			range = 270

		message = "This car can go approximately " + str(range)
		message += " miles on a full charge."
		return message

# Inheritence in Python 3+
class ElectricCar(Car):
	"""Models aspects of a car, specific to electric vehicles"""
	def __init__(self, make, model, year):
		"""Initialize attributes of parent class."""
		super(ElectricCar, self).__init__(make, model, year)
		self.battery = Battery()

my_testla = ElectricCar('tesla', 'model s', '2019')
print(my_testla.get_descriptive_name())
print(my_testla.battery.describe_battery())
print(my_testla.battery.get_range())


