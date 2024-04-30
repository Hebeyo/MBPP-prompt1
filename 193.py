"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to remove the duplicates from the given tuple.
'''

def remove_tuple(test_tup):
  res = tuple(set(test_tup))
  return (res)

'''
Standard answer: 
def remove_tuple(test_tup):
  res = tuple(set(test_tup))
  return (res) 
'''
assert remove_tuple((1, 3, 5, 2, 3, 5, 1, 1, 3)) == (1, 2, 3, 5)
assert remove_tuple((2, 3, 4, 4, 5, 6, 6, 7, 8, 8)) == (2, 3, 4, 5, 6, 7, 8)
assert remove_tuple((11, 12, 13, 11, 11, 12, 14, 13)) == (11, 12, 13, 14)
