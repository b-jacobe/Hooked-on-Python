"""
4_11_my_pizza_your_pizza.py

Start with your program from Exercise 4-1
(page 60). Make a copy of the list of pizzas, and call it friend_pizzas.
Then, do the following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message, My favorite
pizzas are:, and then use a for loop to print the first list. Print the message,
My friend’s favorite pizzas are:, and then use a for loop to print the second
list. Make sure each new pizza is stored in the appropriate list.

Created: 1-15-19
Last Updated: 
@author: Brian Jacobe

"""

favorite_pizzas = ['mushroom & sausage', 'pepperoni', 'chicken']

for i in favorite_pizzas:
	print("I like " + i + " pizza.")

print('These are my three favorite flavors and my main reason why I love pizza is because of the taste!')

friend_pizzas = favorite_pizzas[:]
favorite_pizzas.append('cheese')
friend_pizzas.append('anchovie')

print("My favorite pizzas are: ")
for i in favorite_pizzas:
	print(i)

print("My friend's favorite pizzas are: " )
for j in friend_pizzas:
	print(j)
