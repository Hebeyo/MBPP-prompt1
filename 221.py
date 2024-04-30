"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the first even number in a given list of numbers.
'''

def first_even(nums):
    for i in nums:
        if i % 2 == 0:
            return i
    return -1

'''
Standard answer: 
def first_even(nums):
    first_even = next((el for el in nums if el%2==0),-1)
    return first_even
'''
assert first_even ([1, 3, 5, 7, 4, 1, 6, 8]) == 4
assert first_even([2, 3, 4]) == 2
assert first_even([5, 6, 7]) == 6
