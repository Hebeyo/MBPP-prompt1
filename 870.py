"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to calculate the sum of the positive numbers of a given list of numbers using lambda function.
'''

def sum_positivenum(nums):
  sum_positivenum = [num for num in nums if num>0]
  return sum(sum_positivenum)

'''
Standard answer: 
def sum_positivenum(nums):
  sum_positivenum = list(filter(lambda nums:nums>0,nums))
  return sum(sum_positivenum)
'''
assert sum_positivenum([2, 4, -6, -9, 11, -12, 14, -5, 17])==48
assert sum_positivenum([10,15,-14,13,-18,12,-20])==50
assert sum_positivenum([19, -65, 57, 39, 152,-639, 121, 44, 90, -190])==522
