"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to remove two duplicate numbers from a given number of lists.
'''

def two_unique_nums(nums):
  res = []
  for i in nums:
    if nums.count(i) == 1:
      res.append(i)
  return res

'''
Standard answer: 
def two_unique_nums(nums):
  return [i for i in nums if nums.count(i)==1]
'''
assert two_unique_nums([1,2,3,2,3,4,5]) == [1, 4, 5]
assert two_unique_nums([1,2,3,2,4,5]) == [1, 3, 4, 5]
assert two_unique_nums([1,2,3,4,5]) == [1, 2, 3, 4, 5]
