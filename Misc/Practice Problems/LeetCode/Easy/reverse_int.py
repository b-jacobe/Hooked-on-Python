"""
reverse_integer

Given a 32-bit signed integer,
reverse digits of an integer
"""

def reverse(self, x: int) -> int:
    if x > 0:
    	result = int(str(x)[::-1]) 
    elif x <= 0:
        result = -1 * int(str(x*-1)[::-1])
    min_x = -2**31
    max_x = 2**31 - 1
    if result not in range(min_x, max_x):
        return 0
    else:
        return result