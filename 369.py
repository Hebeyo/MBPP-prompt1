"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the lateral surface area of cuboid
'''

def lateralsurface_cuboid(l,w,h):
  return 2*h*(l+w)


'''
Standard answer: 
def lateralsurface_cuboid(l,w,h):
  LSA = 2*h*(l+w)
  return LSA
'''
assert lateralsurface_cuboid(8,5,6)==156
assert lateralsurface_cuboid(7,9,10)==320
assert lateralsurface_cuboid(10,20,30)==1800
