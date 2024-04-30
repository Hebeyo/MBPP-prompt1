"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find whether all the given tuples have equal length or not.
'''

def get_equal(Input, k):
  for tuple in Input:
    if len(tuple) != k:
      return 'All tuples do not have same length'
  return 'All tuples have same length'

'''
Standard answer: 
def find_equal_tuple(Input, k):
  flag = 1
  for tuple in Input:
    if len(tuple) != k:
      flag = 0
      break
  return flag
def get_equal(Input, k):
  if find_equal_tuple(Input, k) == 1:
    return ("All tuples have same length")
  else:
    return ("All tuples do not have same length")
'''
assert get_equal([(11, 22, 33), (44, 55, 66)], 3) == 'All tuples have same length'
assert get_equal([(1, 2, 3), (4, 5, 6, 7)], 3) == 'All tuples do not have same length'
assert get_equal([(1, 2), (3, 4)], 2) == 'All tuples have same length'
