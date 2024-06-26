"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check the given decimal with a precision of 2 by using regex.
'''

import re
def is_decimal(num):
  num_fetch = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
  result = num_fetch.search(num)
  return bool(result)

'''
Standard answer: 
import re
def is_decimal(num):
  num_fetch = re.compile(r"""^[0-9]+(\.[0-9]{1,2})?$""")
  result = num_fetch.search(num)
  return bool(result)
'''
assert is_decimal('123.11') == True
assert is_decimal('0.21') == True
assert is_decimal('123.1214') == False
