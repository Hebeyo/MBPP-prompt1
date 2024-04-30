"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to determine whether all the numbers are different from each other are not.
'''

def test_distinct(data):
  for i in range(len(data)):
    for j in range(i+1,len(data)):
      if data[i] == data[j]:
        return False
  return True

'''
Standard answer: 
def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;
'''
assert test_distinct([1,5,7,9]) == True
assert test_distinct([2,4,5,5,7,9]) == False
assert test_distinct([1,2,3]) == True
