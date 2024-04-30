"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the sum of the largest and smallest value in a given array.
'''

def big_sum(nums):
    sum = 0
    for i in range(len(nums)):
        if i == 0:
            max = nums[i]
            min = nums[i]
        else:
            if nums[i] > max:
                max = nums[i]
            if nums[i] < min:
                min = nums[i]
    sum = max + min
    return sum

'''
Standard answer: 
def big_sum(nums):
      sum= max(nums)+min(nums)
      return sum
'''
assert big_sum([1,2,3]) == 4
assert big_sum([-1,2,3,4]) == 3
assert big_sum([2,3,6]) == 8
