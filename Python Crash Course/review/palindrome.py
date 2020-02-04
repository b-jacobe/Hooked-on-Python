"""
palindrome.py

Create a funciton that checks if the
string is a palindrome or not. Returns
True or False
"""

def check_palindrome(n):
  # converts string into list.
  user_list = list()
  for i in range(len(n)):
    user_list.append(n[i])
  # use slice and reverse for list to list comparison
  r_list = user_list[:]
  r_list.reverse()
  if r_list == user_list:
    return True
  else:
    return False

# Driver Code
print(check_palindrome('racecar'))
print(check_palindrome('banana'))
print(check_palindrome('kayak'))
print(check_palindrome('rotor'))
