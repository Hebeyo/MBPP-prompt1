"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to left rotate the string.
'''

def left_rotate(s,d):
    return s[d : ] + s[0 : d]

'''
Standard answer: 
def left_rotate(s,d):
    tmp = s[d : ] + s[0 : d]
    return tmp  
'''
assert left_rotate("python",2) == "thonpy"   
assert left_rotate("bigdata",3 ) == "databig" 
assert left_rotate("hadoop",1 ) == "adooph" 
