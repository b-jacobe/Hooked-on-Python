"""
xyz_there.py

Return True if the given string contains
'xyz' where the 'xyz' is not directly
proceeded by a period(.)
"""

def xyz_there(w):
  result_str = w.split('.xyz')
  result_str = "".join(result_str)
  return result_str.count('.xyz') == 0 and result_str.count('xyz') > 0

# Driver Code
print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('abcxy'))
print(xyz_there('xyz'))
