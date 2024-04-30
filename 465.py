"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to drop empty items from a given dictionary.
'''

def drop_empty(dict1):
  dict1 = {key:value for (key, value) in dict1.items() if value is not None}
  return dict1


'''
Standard answer: 
def drop_empty(dict1):
  dict1 = {key:value for (key, value) in dict1.items() if value is not None}
  return dict1
'''
assert drop_empty({'c1': 'Red', 'c2': 'Green', 'c3':None})=={'c1': 'Red', 'c2': 'Green'}
assert drop_empty({'c1': 'Red', 'c2': None, 'c3':None})=={'c1': 'Red'}
assert drop_empty({'c1': None, 'c2': 'Green', 'c3':None})=={ 'c2': 'Green'}
