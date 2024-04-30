"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check if given tuple is distinct or not.
'''

def check_distinct(test_tup):
  temp = set()
  for ele in test_tup:
    if ele in temp:
      return False
    temp.add(ele)
  return True

'''
Standard answer: 
def check_distinct(test_tup):
  res = True
  temp = set()
  for ele in test_tup:
    if ele in temp:
      res = False
      break
    temp.add(ele)
  return (res) 
'''
assert check_distinct((1, 4, 5, 6, 1, 4)) == False
assert check_distinct((1, 4, 5, 6)) == True
assert check_distinct((2, 3, 4, 5, 6)) == True
