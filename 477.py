"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to convert the given string to lower case.
'''

def is_lower(string):
  return (string.lower())

'''
Standard answer: 
def is_lower(string):
  return (string.lower())
'''
assert is_lower("InValid") == "invalid"
assert is_lower("TruE") == "true"
assert is_lower("SenTenCE") == "sentence"
