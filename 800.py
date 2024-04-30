"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to remove all whitespaces from a string.
'''

def remove_all_spaces(text):
 return text.replace(' ','')

'''
Standard answer: 
import re
def remove_all_spaces(text):
 return (re.sub(r'\s+', '',text))
'''
assert remove_all_spaces('python  program')==('pythonprogram')
assert remove_all_spaces('python   programming    language')==('pythonprogramminglanguage')
assert remove_all_spaces('python                     program')==('pythonprogram')
