"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to convert degrees to radians.
'''

def radian_degree(degree):
    return degree*(3.141592653589793/180)

'''
Standard answer: 
import math
def radian_degree(degree):
 radian = degree*(math.pi/180)
 return radian
'''
assert radian_degree(90)==1.5707963267948966
assert radian_degree(60)==1.0471975511965976
assert radian_degree(120)==2.0943951023931953
