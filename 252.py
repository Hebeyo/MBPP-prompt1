"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to convert complex numbers to polar coordinates.
'''

import math
def convert(numbers):
    return (math.sqrt(numbers.real**2 + numbers.imag**2), math.atan2(numbers.imag, numbers.real))

'''
Standard answer: 
import cmath  
def convert(numbers):    
  num = cmath.polar(numbers)  
  return (num) 
'''
assert convert(1) == (1.0, 0.0)
assert convert(4) == (4.0,0.0)
assert convert(5) == (5.0,0.0)
