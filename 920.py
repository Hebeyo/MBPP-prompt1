"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to remove all tuples with all none values in the given tuple list.
'''

def remove_tuple(test_list):
  res = [sub for sub in test_list if not all(ele == None for ele in sub)]
  return (str(res))

'''
Standard answer: 
def remove_tuple(test_list):
  res = [sub for sub in test_list if not all(ele == None for ele in sub)]
  return (str(res)) 
'''
assert remove_tuple([(None, 2), (None, None), (3, 4), (12, 3), (None, )] ) == '[(None, 2), (3, 4), (12, 3)]'
assert remove_tuple([(None, None), (None, None), (3, 6), (17, 3), (None,1 )] ) == '[(3, 6), (17, 3), (None, 1)]'
assert remove_tuple([(1, 2), (2, None), (3, None), (24, 3), (None, None )] ) == '[(1, 2), (2, None), (3, None), (24, 3)]'
