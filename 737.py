"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check whether the given string is starting with a vowel or not using regex.
'''

def check_str(string):
    import re
    regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
    return "Valid" if re.search(regex, string) else "Invalid"

'''
Standard answer: 
import re 
regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
def check_str(string): 
	if(re.search(regex, string)): 
		return ("Valid") 
	else: 
		return ("Invalid") 
'''
assert check_str("annie") == 'Valid'
assert check_str("dawood") == 'Invalid'
assert check_str("Else") == 'Valid'
