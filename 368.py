"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to repeat the given tuple n times.
'''

def repeat_tuples(test_tup, N):
  res = []
  for i in range(N):
    res.append(test_tup)
  return tuple(res)


'''
Standard answer: 
def repeat_tuples(test_tup, N):
  res = ((test_tup, ) * N)
  return (res) 
'''
assert repeat_tuples((1, 3), 4) == ((1, 3), (1, 3), (1, 3), (1, 3))
assert repeat_tuples((1, 2), 3) == ((1, 2), (1, 2), (1, 2))
assert repeat_tuples((3, 4), 5) == ((3, 4), (3, 4), (3, 4), (3, 4), (3, 4))
