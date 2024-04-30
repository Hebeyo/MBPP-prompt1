"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find nth centered hexagonal number.
'''

def centered_hexagonal_number(n):
    return 3*n*(n-1)+1

'''
Standard answer: 
def centered_hexagonal_number(n):
  return 3 * n * (n - 1) + 1
'''
assert centered_hexagonal_number(10) == 271
assert centered_hexagonal_number(2) == 7
assert centered_hexagonal_number(9) == 217
