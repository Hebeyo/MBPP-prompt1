"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to calculate the harmonic sum of n-1.
'''

def harmonic_sum(n):
  if n < 2:
    return 1
  else:
    return 1 / n + (harmonic_sum(n - 1))

'''
Standard answer: 
def harmonic_sum(n):
  if n < 2:
    return 1
  else:
    return 1 / n + (harmonic_sum(n - 1)) 
'''
assert harmonic_sum(7) == 2.5928571428571425
assert harmonic_sum(4) == 2.083333333333333
assert harmonic_sum(19) == 3.547739657143682
