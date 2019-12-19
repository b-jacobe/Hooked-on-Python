"""
has22.py

Given an array of ints, return True
if the array contains a 2 next to a 2
somewhere
"""

def has22(nums):
    flag_2 = 0
    for i in range(len(nums)):
        if i < len(nums) and nums[i] == 2 and nums[i+1] == 2:
            flag_2 += 1
    if flag_2 >= 1:
        return True
    else:
        return False