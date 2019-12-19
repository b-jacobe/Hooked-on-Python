"""
sum13.py

Return the sum of numbers in the array, returning 0
for an empty array. Except the number 13 is unlucky,
so it does not count and numberst that come immediately after
a 13 also does not count.

"""

def sum13(nums):
    if len(nums) == 0:
        return 0
    for i in range(0, len(nums)):
        if nums[i] == 13:
            nums[i] = 0
        if i+1 < len(nums): 
            nums[i+1] = 0
    return sum(nums)


# TEST CASE
print(sum13([1,2,2,1]))
print(sum13([1,2,2,1,13]))
print(sum13([13,1,2,13,2,1,13]))