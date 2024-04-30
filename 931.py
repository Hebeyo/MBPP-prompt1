"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to calculate the sum of series 1³+2³+3³+….+n³.
'''

def sum_series(number):
    total = 0
    for i in range(1,number+1):
        total += i**3
    return total

'''
Standard answer: 
import math 
def sum_series(number):
 total = 0
 total = math.pow((number * (number + 1)) /2, 2)
 return total
'''
assert sum_series(7)==784
assert sum_series(5)==225
assert sum_series(15)==14400
