"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the perimeter of a pentagon.
'''

def perimeter_pentagon(a):
  perimeter=0
  for i in range(0,5):
    perimeter+=a
  return perimeter

'''
Standard answer: 
import math
def perimeter_pentagon(a):
  perimeter=(5*a)
  return perimeter
'''
assert perimeter_pentagon(5)==25
assert perimeter_pentagon(10)==50
assert perimeter_pentagon(15)==75
