"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to get the sum of a non-negative integer.
'''

def sum_digits(n):
  sum = 0
  while n>0:
    sum += n % 10
    n = n//10
  return sum

'''
Standard answer: 
def sum_digits(n):
  if n == 0:
    return 0
  else:
    return n % 10 + sum_digits(int(n / 10))
'''
assert sum_digits(345)==12
assert sum_digits(12)==3
assert sum_digits(97)==16
