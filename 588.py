"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the difference between largest and smallest value in a given array.
'''

def big_diff(nums):
     nums.sort()
     diff= nums[-1]-nums[0]
     return diff

'''
Standard answer: 
def big_diff(nums):
     diff= max(nums)-min(nums)
     return diff
'''
assert big_diff([1,2,3,4]) == 3
assert big_diff([4,5,12]) == 8
assert big_diff([9,2,3]) == 7
