"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to calculate the perimeter of a regular polygon.
'''

def perimeter_polygon(s,l):
  perimeter = s*l
  return perimeter

'''
Standard answer: 
from math import tan, pi
def perimeter_polygon(s,l):
  perimeter = s*l
  return perimeter
'''
assert perimeter_polygon(4,20)==80
assert perimeter_polygon(10,15)==150
assert perimeter_polygon(9,7)==63
