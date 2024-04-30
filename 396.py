"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check whether the given string starts and ends with the same character or not using regex.
'''

import re
def check_char(string):
    if re.search(r'^[a-z]$|^([a-z]).*\1$', string):
        return "Valid"
    else:
        return "Invalid"

'''
Standard answer: 
import re  
regex = r'^[a-z]$|^([a-z]).*\1$'
def check_char(string): 
	if(re.search(regex, string)): 
		return "Valid" 
	else: 
		return "Invalid" 
'''
assert check_char("abba") == "Valid"
assert check_char("a") == "Valid"
assert check_char("abcd") == "Invalid"
