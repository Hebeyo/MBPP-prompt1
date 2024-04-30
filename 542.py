"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to replace all occurrences of spaces, commas, or dots with a colon in the given string by using regex.
'''

import re
def fill_spaces(text):
  return (re.sub("[ ,.]", ":", text))

'''
Standard answer: 
import re
def fill_spaces(text):
  return (re.sub("[ ,.]", ":", text))
'''
assert fill_spaces('Boult Curve Wireless Neckband') == 'Boult:Curve:Wireless:Neckband'
assert fill_spaces('Stereo Sound Sweatproof') == 'Stereo:Sound:Sweatproof'
assert fill_spaces('Probass Curve Audio') == 'Probass:Curve:Audio'
