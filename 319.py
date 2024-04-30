"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find all five characters long word in the given string by using regex.
'''

import re
def find_long_word(text):
  return (re.findall(r"\b\w{5}\b", text))

'''
Standard answer: 
import re
def find_long_word(text):
  return (re.findall(r"\b\w{5}\b", text))
'''
assert find_long_word('Please move back to strem') == ['strem']
assert find_long_word('4K Ultra HD streaming player') == ['Ultra']
assert find_long_word('Streaming Media Player') == ['Media']
