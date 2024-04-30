"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the union of elements of the given tuples.
'''

def union_elements(test_tup1, test_tup2):
  res = test_tup1 + test_tup2
  res = tuple(set(res))
  return (res)

'''
Standard answer: 
def union_elements(test_tup1, test_tup2):
  res = tuple(set(test_tup1 + test_tup2))
  return (res) 
'''
assert union_elements((3, 4, 5, 6),(5, 7, 4, 10) ) == (3, 4, 5, 6, 7, 10)
assert union_elements((1, 2, 3, 4),(3, 4, 5, 6) ) == (1, 2, 3, 4, 5, 6)
assert union_elements((11, 12, 13, 14),(13, 15, 16, 17) ) == (11, 12, 13, 14, 15, 16, 17)
