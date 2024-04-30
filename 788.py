"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to create a new tuple from the given string and list.
'''

def new_tuple(test_list, test_str):
  res = test_list
  res.append(test_str)
  return tuple(res)

'''
Standard answer: 
def new_tuple(test_list, test_str):
  res = tuple(test_list + [test_str])
  return (res) 
'''
assert new_tuple(["WEB", "is"], "best") == ('WEB', 'is', 'best')
assert new_tuple(["We", "are"], "Developers") == ('We', 'are', 'Developers')
assert new_tuple(["Part", "is"], "Wrong") == ('Part', 'is', 'Wrong')
