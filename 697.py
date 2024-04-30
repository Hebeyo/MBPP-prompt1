"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find number of even elements in the given list using lambda function.
'''

def count_even(array_nums):
   count_even = len(list(filter(lambda x: (x%2 == 0) , array_nums)))
   return count_even

'''
Standard answer: 
def count_even(array_nums):
   count_even = len(list(filter(lambda x: (x%2 == 0) , array_nums)))
   return count_even
'''
assert count_even([1, 2, 3, 5, 7, 8, 9, 10])==3
assert count_even([10,15,14,13,-18,12,-20])==5
assert count_even([1, 2, 4, 8, 9])==3
