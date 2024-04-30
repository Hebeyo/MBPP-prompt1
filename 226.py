"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to remove the characters which have odd index values of a given string.
'''

def odd_values_string(str):
  return str[::2]

'''
Standard answer: 
def odd_values_string(str):
  result = "" 
  for i in range(len(str)):
    if i % 2 == 0:
      result = result + str[i]
  return result
'''
assert odd_values_string('abcdef') == 'ace'
assert odd_values_string('python') == 'pto'
assert odd_values_string('data') == 'dt'
