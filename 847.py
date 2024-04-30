"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to copy a list from a singleton tuple.
'''

def lcopy(xs):
  return list(xs)

'''
Standard answer: 
def lcopy(xs):
  return xs[:]

'''
assert lcopy([1, 2, 3]) == [1, 2, 3]
assert lcopy([4, 8, 2, 10, 15, 18]) == [4, 8, 2, 10, 15, 18]
assert lcopy([4, 5, 6]) == [4, 5, 6]

