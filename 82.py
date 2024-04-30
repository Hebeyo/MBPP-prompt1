"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the volume of a sphere.
'''

def volume_sphere(r):
  volume=(4/3)*3.141592653589793*r*r*r
  return volume

'''
Standard answer: 
import math
def volume_sphere(r):
  volume=(4/3)*math.pi*r*r*r
  return volume
'''
assert volume_sphere(10)==4188.790204786391
assert volume_sphere(25)==65449.84694978735
assert volume_sphere(20)==33510.32163829113
