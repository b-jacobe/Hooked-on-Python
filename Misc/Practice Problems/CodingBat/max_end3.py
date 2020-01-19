"""
max_end3

given an array of ints length 3, figure out which
is larger, the first or the last element of the array
and set all the other elements to be that value. Return
the changed array.
"""

def max_end3(nums):
  result_list = list()
  max_num = None
  if nums[0] < nums[-1]:
    max_num = nums[-1]
  else:
    max_num = nums[0]
  for i in range(len(nums)):
    result_list.append(max_num)
  return result_list

#driver code
print(max_end3([2,3,1]))
print(max_end3([2,3,3]))
print(max_end3([99,123,443,2342,33]))
