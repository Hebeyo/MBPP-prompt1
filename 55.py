"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find t-nth term of geometric series.
'''

def tn_gp(a,n,r):
  tn = a
  for i in range(1,n):
    tn = tn * r
  return tn

'''
Standard answer: 
import math
def tn_gp(a,n,r):
  tn = a * (math.pow(r, n - 1))
  return tn
'''
assert tn_gp(1,5,2)==16
assert tn_gp(1,5,4)==256
assert tn_gp(2,6,3)==486
