"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count the number of equal numbers from three given integers.
'''

def test_three_equal(x,y,z):
  result= set([x,y,z])
  if len(result)==3:
    return 0
  else:
    return (4-len(result))

'''
Standard answer: 
def test_three_equal(x,y,z):
  result= set([x,y,z])
  if len(result)==3:
    return 0
  else:
    return (4-len(result))
'''
assert test_three_equal(1,1,1) == 3
assert test_three_equal(-1,-2,-3) == 0
assert test_three_equal(1,2,2) == 2
