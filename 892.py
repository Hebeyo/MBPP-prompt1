"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to remove multiple spaces in a string.
'''

def remove_spaces(text):
    return ' '.join(text.split())

'''
Standard answer: 
import re
def remove_spaces(text):
 return (re.sub(' +',' ',text))
'''
assert remove_spaces('python  program')==('python program')
assert remove_spaces('python   programming    language')==('python programming language')
assert remove_spaces('python                     program')==('python program')
