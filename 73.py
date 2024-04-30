"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to split the given string with multiple delimiters by using regex.
'''

import re
def multiple_split(text):
  return (re.split('; |, |\*|\n',text))

'''
Standard answer: 
import re
def multiple_split(text):
  return (re.split('; |, |\*|\n',text))
'''
assert multiple_split('Forces of the \ndarkness*are coming into the play.') == ['Forces of the ', 'darkness', 'are coming into the play.']
assert multiple_split('Mi Box runs on the \n Latest android*which has google assistance and chromecast.') == ['Mi Box runs on the ', ' Latest android', 'which has google assistance and chromecast.']
assert multiple_split('Certain services\nare subjected to change*over the seperate subscriptions.') == ['Certain services', 'are subjected to change', 'over the seperate subscriptions.']
