"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check if the given tuple contains all valid values or not.
'''

def check_valid(test_tup):
  for ele in test_tup:
    if not ele:
      return False
  return True

'''
Standard answer: 
def check_valid(test_tup):
  res = not any(map(lambda ele: not ele, test_tup))
  return (res) 
'''
assert check_valid((True, True, True, True) ) == True
assert check_valid((True, False, True, True) ) == False
assert check_valid((True, True, True, True) ) == True
