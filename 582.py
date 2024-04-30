"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check if a dictionary is empty or not.
'''

def my_dict(dict1):
  if len(dict1)==0:
    return True
  else:
    return False

'''
Standard answer: 
def my_dict(dict1):
  if bool(dict1):
     return False
  else:
     return True
'''
assert my_dict({10})==False
assert my_dict({11})==False
assert my_dict({})==True
