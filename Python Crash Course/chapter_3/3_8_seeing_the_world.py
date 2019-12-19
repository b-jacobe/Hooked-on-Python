"""
3_8_seeing_the_world.py

Think of at least five places in the world you’d like to
visit.
• Store the locations in a list. Make sure the list is not in alphabetical order.
• Print your list in its original order. Don’t worry about printing the list neatly,
just print it as a raw Python list.
• Use sorted() to print your list in alphabetical order without modifying the
actual list.
• Show that your list is still in its original order by printing it.
• Use sorted() to print your list in reverse alphabetical order without changing
the order of the original list.
• Show that your list is still in its original order by printing it again.
• Use reverse() to change the order of your list. Print the list to show that its
order has changed.
• Use reverse() to change the order of your list again. Print the list to show
it’s back to its original order.
• Use sort() to change your list so it’s stored in alphabetical order. Print the
list to show that its order has been changed.
• Use sort() to change your list so it’s stored in reverse

Created: 1-12-19
Last Updated: 
@author: Brian Jacobe

"""

vacation_travels = ['Japan', 'Thailand', 'Vietnam', 'Europe', 'Australia/New Zealand']
print(vacation_travels)

print(sorted(vacation_travels))

print(vacation_travels)

vacation_travels.reverse()
print(vacation_travels)

vacation_travels.reverse()
print(vacation_travels)

vacation_travels.sort()
print(vacation_travels)

vacation_travels.sort(reverse=True)
print(vacation_travels)


