"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to remove all whitespaces from the given string using regex.
'''

import re
def remove_whitespaces(text1):
  return (re.sub(r'\s+', '',text1))

'''
Standard answer: 
import re
def remove_whitespaces(text1):
  return (re.sub(r'\s+', '',text1))
'''
assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'
assert remove_whitespaces(' Google    Dart ') == 'GoogleDart'
assert remove_whitespaces(' iOS    Swift ') == 'iOSSwift'
