"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to remove lowercase substrings from a given string.
'''

def remove_lowercase(str1):
    str2 = ''
    for i in str1:
        if i.isupper():
            str2+=i
    return str2

'''
Standard answer: 
import re
def remove_lowercase(str1):
 remove_lower = lambda text: re.sub('[a-z]', '', text)
 result =  remove_lower(str1)
 return result
'''
assert remove_lowercase("PYTHon")==('PYTH')
assert remove_lowercase("FInD")==('FID')
assert remove_lowercase("STRinG")==('STRG')
