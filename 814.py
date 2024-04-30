"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the area of a rombus.
'''

def rombus_area(p,q):
  area=p*q/2
  return area

'''
Standard answer: 
def rombus_area(p,q):
  area=(p*q)/2
  return area
'''
assert rombus_area(10,20)==100
assert rombus_area(10,5)==25
assert rombus_area(4,2)==4
