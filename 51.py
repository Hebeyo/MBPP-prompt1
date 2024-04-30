"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to print check if the triangle is equilateral or not.
'''

def check_equilateral(x,y,z):
    if x==y and x==z:
        return True
    else:
        return False

'''
Standard answer: 
def check_equilateral(x,y,z):
  if x == y == z:
	   return True
  else:
     return False
'''
assert check_equilateral(6,8,12)==False 
assert check_equilateral(6,6,12)==False
assert check_equilateral(6,6,6)==True
