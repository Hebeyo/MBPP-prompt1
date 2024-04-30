"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to get the length of a complex number.
'''

def len_complex(a,b):
  return (a**2 + b**2)**0.5

'''
Standard answer: 
import cmath
def len_complex(a,b):
  cn=complex(a,b)
  length=abs(cn)
  return length
'''
assert len_complex(3,4)==5.0
assert len_complex(9,10)==13.45362404707371
assert len_complex(7,9)==11.40175425099138
