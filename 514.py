"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the summation of tuple elements in the given tuple list.
'''

def sum_elements(test_tup):
  res = 0
  for ele in test_tup:
    res += ele
  return (res)

'''
Standard answer: 
def sum_elements(test_tup):
  res = sum(list(test_tup))
  return (res) 
'''
assert sum_elements((7, 8, 9, 1, 10, 7)) == 42
assert sum_elements((1, 2, 3, 4, 5, 6)) == 21
assert sum_elements((11, 12 ,13 ,45, 14)) == 95
