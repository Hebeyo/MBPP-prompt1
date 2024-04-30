"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to remove spaces from a given string.
'''

def remove_spaces(str1):
  str1 = str1.replace(' ','')
  return str1

'''
Standard answer: 
def remove_spaces(str1):
  str1 = str1.replace(' ','')
  return str1
'''
assert remove_spaces("a b c") == "abc"
assert remove_spaces("1 2 3") == "123"
assert remove_spaces(" b c") == "bc"
