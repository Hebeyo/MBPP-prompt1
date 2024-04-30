"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check if each element of the second tuple is greater than its corresponding index in the first tuple.
'''

def check_greater(test_tup1, test_tup2):
  for i in range(len(test_tup1)):
    if test_tup1[i] >= test_tup2[i]:
      return False
  return True

'''
Standard answer: 
def check_greater(test_tup1, test_tup2):
  res = all(x < y for x, y in zip(test_tup1, test_tup2))
  return (res) 
'''
assert check_greater((10, 4, 5), (13, 5, 18)) == True
assert check_greater((1, 2, 3), (2, 1, 4)) == False
assert check_greater((4, 5, 6), (5, 6, 7)) == True
