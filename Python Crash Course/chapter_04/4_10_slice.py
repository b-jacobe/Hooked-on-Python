"""
4_10_slice.py

Using one of the programs you wrote in this chapter, add several
lines to the end of the program that do the following:
• Print the message, The first three items in the list are:. Then use a slice to
print the first three items from that program’s list.
• Print the message, Three items from the middle of the list are:. Use a slice
to print three items from the middle of the list.
• Print the message, The last three items in the list are:. Use a slice to print
the last three items in the list.

Created: 1-15-19
Last Updated: 
@author: Brian Jacobe

"""

cube = [value**3 for value in range(1,11)]
print(cube)
print(cube[:3])
print("The three items from the midle of the list are: ")
print(cube[4:7])
print("The last three items from the list are: ")
print(cube[-3:])