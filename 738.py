"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to calculate the geometric sum of n-1.
'''

def geometric_sum(n):
  if n == 0:
    return 1
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 1)

'''
Standard answer: 
def geometric_sum(n):
  if n < 0:
    return 0
  else:
    return 1 / (pow(2, n)) + geometric_sum(n - 1)
'''
assert geometric_sum(7) == 1.9921875
assert geometric_sum(4) == 1.9375
assert geometric_sum(8) == 1.99609375
