"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to sort the given string.
'''

def sort_String(str) : 
    return ''.join(sorted(str))

'''
Standard answer: 
def sort_String(str) : 
    str = ''.join(sorted(str)) 
    return (str) 
'''
assert sort_String("cba") == "abc"
assert sort_String("data") == "aadt"
assert sort_String("zxy") == "xyz"
