"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to caluclate the area of a tetrahedron.
'''

def area_tetrahedron(side):
  area = 1.7320508075688772*(side*side)
  return area

'''
Standard answer: 
import math
def area_tetrahedron(side):
  area = math.sqrt(3)*(side*side)
  return area
'''
assert area_tetrahedron(3)==15.588457268119894
assert area_tetrahedron(20)==692.8203230275509
assert area_tetrahedron(10)==173.20508075688772
