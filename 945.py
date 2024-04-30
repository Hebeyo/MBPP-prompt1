"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to convert the given tuples into set.
'''

def tuple_to_set(t):
  s = set()
  for i in t:
    s.add(i)
  return (s)

'''
Standard answer: 
def tuple_to_set(t):
  s = set(t)
  return (s) 
'''
assert tuple_to_set(('x', 'y', 'z') ) == {'y', 'x', 'z'}
assert tuple_to_set(('a', 'b', 'c') ) == {'c', 'a', 'b'}
assert tuple_to_set(('z', 'd', 'e') ) == {'d', 'e', 'z'}
