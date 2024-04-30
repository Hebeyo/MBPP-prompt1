"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the surface area of a sphere.
'''

def surfacearea_sphere(r):
  surfacearea=4*3.141592653589793*r*r
  return surfacearea

'''
Standard answer: 
import math
def surfacearea_sphere(r):
  surfacearea=4*math.pi*r*r
  return surfacearea
'''
assert surfacearea_sphere(10)==1256.6370614359173
assert surfacearea_sphere(15)==2827.4333882308138
assert surfacearea_sphere(20)==5026.548245743669
