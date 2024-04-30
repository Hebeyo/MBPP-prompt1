"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to remove multiple spaces in a string by using regex.
'''

import re
def remove_multiple_spaces(text1):
  return (re.sub(' +',' ',text1))

'''
Standard answer: 
import re
def remove_multiple_spaces(text1):
  return (re.sub(' +',' ',text1))
'''
assert remove_multiple_spaces('Google      Assistant') == 'Google Assistant'
assert remove_multiple_spaces('Quad      Core') == 'Quad Core'
assert remove_multiple_spaces('ChromeCast      Built-in') == 'ChromeCast Built-in'
