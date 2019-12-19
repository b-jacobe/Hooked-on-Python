"""
3_10_every_function.py

Think of something you could store in a list. For example,
you could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items
and then uses each function introduced in this chapter at least once.

Created: 1-12-19
Last Updated: 
@author: Brian Jacobe

"""

mylist = ['dog', 'cat', 'monkey']

mylist.remove('monkey')
mylist.append('pig')
mylist.pop()
del mylist[0]
mylist.insert(0,'dog')

print(sorted(mylist))
print(mylist)
mylist.sort()
print(mylist)
mylist.sort(reverse=True)
print(mylist)
print(str(len(mylist)))