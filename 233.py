"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the lateral surface area of a cylinder.
'''

def lateralsuface_cylinder(r,h):
  lateralsurface= 2*3.1415*r*h
  return lateralsurface

'''
Standard answer: 
def lateralsuface_cylinder(r,h):
  lateralsurface= 2*3.1415*r*h
  return lateralsurface
'''
assert lateralsuface_cylinder(10,5)==314.15000000000003
assert lateralsuface_cylinder(4,5)==125.66000000000001
assert lateralsuface_cylinder(4,10)==251.32000000000002
