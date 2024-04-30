"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the lateral surface area of a cube.
'''

def lateralsurface_cube(l):
    return 4 * (l * l)

'''
Standard answer: 
def lateralsurface_cube(l):
  LSA = 4 * (l * l)
  return LSA
'''
assert lateralsurface_cube(5)==100
assert lateralsurface_cube(9)==324
assert lateralsurface_cube(10)==400
