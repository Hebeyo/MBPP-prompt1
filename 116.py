"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to convert a given tuple of positive integers into an integer.
'''

def tuple_to_int(nums):
    result = 0
    for i in range(len(nums)):
        result = result*10 + nums[i]
    return result

'''
Standard answer: 
def tuple_to_int(nums):
    result = int(''.join(map(str,nums)))
    return result
'''
assert tuple_to_int((1,2,3))==123
assert tuple_to_int((4,5,6))==456
assert tuple_to_int((5,6,7))==567
