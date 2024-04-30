"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to remove particular data type elements from the given tuple.
'''

def remove_datatype(test_tuple, data_type):
  return [ele for ele in test_tuple if not isinstance(ele, data_type)]

'''
Standard answer: 
def remove_datatype(test_tuple, data_type):
  res = []
  for ele in test_tuple:
    if not isinstance(ele, data_type):
      res.append(ele)
  return (res) 
'''
assert remove_datatype((4, 5, 4, 7.7, 1.2), int) == [7.7, 1.2]
assert remove_datatype((7, 8, 9, "SR"), str) == [7, 8, 9]
assert remove_datatype((7, 1.1, 2, 2.2), float) == [7, 2]
