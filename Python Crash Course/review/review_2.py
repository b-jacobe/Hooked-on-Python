"""
review_2.py

Review the material learned up to this
point.

Created: 7-12-19
Last Updated: 8-4-19
@author: Brian Jacobe

"""

# ========= NUMBERS =========
value_a = 34
value_b = 16

# Basic Arithmetic
value_c = value_a + value_b
value_c = value_a - value_b
value_c = value_a * value_b
value_c = value_a / value_b

# Ceil Division
value_c = value_a // value_b

# Floor Division
value_c = -(-value_a//value_b)

# Modulo
value_c = 7%2

# Powers
value_c = 7**2

# Square Root
value_c = 7**0.5

# Absolute Value

abs_val = abs(-94)

# ========= STRINGS =========

# Indexing Strings
message = "Hello World"
string_pos = message[0]

# String Concatenate
first_name = 'Brian'
last_name = 'Jacobe'
full_name = first_name + last_name

# Slicing Strings - (Start, Stop, Skip)
# Note: When slicing, statement usually uses 
#       context of "up to but not including"
message_dup = message[:]
message_partial_dup = message[:3]

# Length
string_len = len(message)

# Reverse
string_rev = message[::-1]

# Some Built-In String Functions
message.upper()
message.lower()
message.isupper()
message.islower()
message.title()
message.split()
message.join(message_dup)

# String Formatting
# There are three ways to perform string formatting:
# 1. % modulo character 
#     • %s = string, %r = representation, %d = integers
# 	  • %_._f = minimum number of characters to contain and numbers past the decimal point
# 2. .format()
#	  • Has several advantages over % such as:
#	  • 1. Inserted objects can be called by index position
#	  • 2. Inserted objects can be assigned keywords
#	  • 3. Can be resued
# 3. f-strings

# % modulo formatting - single
print("I'm going to inject %s here." %'text')
# % modulo formatting - multiple
print("I'm going to inject several things such as: %s, %s, and %s here." %('numnbers','text', 'words'))

# format() 
print("Here are a list of my favorite Disney movies: {}, {}, {}.".format('Hercules', 'Goofy Movie', 'Princess & The Frog'))
print("Here are a list of numbers: {a},{b},{c}.".format(a=1,b=2,c=3))

# f-string
# Can display representation / float formatting within {}
age = 28
print(f"My name is {first_name} and I'm {age!r} years old.")

# ========= LISTS =========
# Mutable sequence of diferent object types.
my_list = [1,2,3,4,5,6,7,8,9,10]
my_list = ['28', 'Brian', 'Single']

print(len(my_list))

# Concatenate lists
my_list = my_list + ['Audi S4 2016']
print(my_list)

# Some Built-In List Functions
my_list.append('Ducati 821 Black')
my_list.append('test')

del my_list[-1]

my_list.insert(3, '2 Dogs')
my_list.insert(len(my_list),'test')

my_list.pop()

# Permanent reverse order
my_list.reverse()

# Sort only for str data type
my_list.sort()

print(my_list)

# List Comprehension
new_list = [i for i in range(0,11)]
print(new_list)

# Nesting Lists
list_1 = [1,2,3,4]
list_2 = [5,6,7,8]
list_3 =[list_1,list_2]
print(list_3)
print(list_3[1][0])

# ========= DICTIONARIES =========
# Mapping used in Python, called Hash Tables in other languages
# They are a collection of objects that are stored by a key.
# Differs from lists as they are not stored by their relative position
# Define a dictionary by { }

my_dict = {"user_name":["user_1","user_2","user_3"], "password":["pwd_123","pwd_456","pwd_789"]}

# Accessing values in dictionary
print(my_dict["user_name"][2])

# Adding new key-value pairs
my_dict["DOB"] = ["4/17/91", "5/19/91","5/11/91"]
print(my_dict)

# Few Methods that can be called on dictionaries
my_dict.keys()
my_dict.values()
my_dict.items()

# For-Loop interaction with dictionaries

for key, value in my_dict.items():
	print(key)
	print(value)
for key in my_dict.keys():
	print(key)
for value in my_dict.values():
	print(value)

# Sort and loop thru the dictionary
for key, value in sorted(my_dict.items()):
	print(key)
	print(value)

# ========= TUPLES =========
# Immutable sequence of objects. They cannot be changed.
# Only use when objects do not need to be changed.
# Use ( ) to define a tuple

t = (1,2,3,)
print(len(t))

# Basic tuple methods
t.index(1)
t.count(2)

# ========= SETS =========
# Unordered collection of unique elements
# use set( ) to define a set

my_set = set()
my_set.add(1)
print(my_set)

list_repeats = [1,1,1,1,3,3,3,2,2,2,5,5,5,6,6,6,4,4,4]
my_set = set(list_repeats)
print(my_set)



