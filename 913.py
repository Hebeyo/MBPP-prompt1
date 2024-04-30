"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check for a number at the end of a string.
'''

def end_num(string):
    return string[-1].isdigit()

'''
Standard answer: 
import re
def end_num(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string):
        return True
    else:
        return False
'''
assert end_num('abcdef')==False
assert end_num('abcdef7')==True
assert end_num('abc')==False
