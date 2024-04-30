"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to print check if the triangle is scalene or not.
'''

def check_isosceles(x,y,z):
  if x!=y and y!=z and z!=x:
	   return True
  else:
     return False

'''
Standard answer: 
def check_isosceles(x,y,z):
  if x!=y & y!=z & z!=x:
	   return True
  else:
     return False
'''
assert check_isosceles(6,8,12)==True
assert check_isosceles(6,6,12)==False
assert check_isosceles(6,15,20)==True
