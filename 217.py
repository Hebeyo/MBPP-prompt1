"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the first repeated character in a given string.
'''

def first_Repeated_Char(str): 
    h = {}
    for ch in str:
        if ch in h: 
            return ch;
        else: 
            h[ch] = 0
    return '\0'


'''
Standard answer: 
def first_Repeated_Char(str): 
    h = {}
    for ch in str:
        if ch in h: 
            return ch;
        else: 
            h[ch] = 0
    return '\0'
'''
assert first_Repeated_Char("Google") == "o"
assert first_Repeated_Char("data") == "a"
assert first_Repeated_Char("python") == '\0'
