"""
foo_bar.py

Print numbers from 1 to user input value,
assuming its an integer. For every multiple
of 5, print 'Foo', every multiple of 7, print
'Bar', and print 'FooBar' if its a multiple
of both. Otherwise print the number.
"""

def foo_bar():
  user_value = int(input("Enter a numeric value.\n"))
  for n in range(1, user_value+1):
    if n % 3 == 0:
      print("Foo")
    elif n % 5 == 0:
      print("Bar")
    elif n % 3 == 0 and n % 5 == 0:
      print("FooBar")
    else:
      print(n)

# Driver Code
if __name__ == "__main__":
  foo_bar()
