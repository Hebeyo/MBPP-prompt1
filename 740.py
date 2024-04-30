"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to convert the given tuple to a key-value dictionary using adjacent elements.
'''

def tuple_to_dict(test_tup):
  res = {test_tup[idx]: test_tup[idx + 1] for idx in range(0, len(test_tup), 2)}
  return (res)

'''
Standard answer: 
def tuple_to_dict(test_tup):
  res = dict(test_tup[idx : idx + 2] for idx in range(0, len(test_tup), 2))
  return (res) 
'''
assert tuple_to_dict((1, 5, 7, 10, 13, 5)) == {1: 5, 7: 10, 13: 5}
assert tuple_to_dict((1, 2, 3, 4, 5, 6)) == {1: 2, 3: 4, 5: 6}
assert tuple_to_dict((7, 8, 9, 10, 11, 12)) == {7: 8, 9: 10, 11: 12}
