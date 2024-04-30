"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to convert radians to degrees.
'''

def degree_radian(radian):
 degree = radian*(180/3.141592653589793)
 return degree

'''
Standard answer: 
import math
def degree_radian(radian):
 degree = radian*(180/math.pi)
 return degree
'''
assert degree_radian(90)==5156.620156177409
assert degree_radian(60)==3437.746770784939
assert degree_radian(120)==6875.493541569878
