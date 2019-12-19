"""
sum67.py

Return the sum of numbers in the array, except ignore sections
of numbers starting with a 6 and extending to the next 7

"""

def sum67(nums):
    flag_7th_value = 0
    if len(nums) == 0:
        return 0
    for i in range(len(nums)):
        if flag_7th_value == 0 and nums[i] == 6:
            flag_7th_value = 1
            nums[i] = 0
            continue
        elif flag_7th_value == 1 and nums[i] != 7:
            nums[i] = 0
            continue
        elif flag_7th_value == 1 and nums[i] == 7:
            flag_7th_value = 0
            nums[i] = 0
            continue
        else:
            continue
    return sum(nums)



# TEST CASE
print(sum67([1, 2, 2]))
print(sum67([1, 2, 2, 6, 99, 99, 7]))
print(sum67([1, 1, 6, 7, 2]))