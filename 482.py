"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find sequences of one upper case letter followed by lower case letters in the given string by using regex.
'''

import re
def match(text):
    pattern = '[A-Z]+[a-z]+$'
    if re.search(pattern, text):
        return('Yes')
    else:
        return('No')

'''
Standard answer: 
import re 
def match(text): 
		pattern = '[A-Z]+[a-z]+$'
		if re.search(pattern, text): 
				return('Yes') 
		else: 
				return('No') 
'''
assert match("Geeks") == 'Yes'
assert match("geeksforGeeks") == 'Yes'
assert match("geeks") == 'No'
