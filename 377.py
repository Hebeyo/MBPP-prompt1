"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to remove all occurrences of a character in a given string.
'''

def remove_Char(s,c) :  
    s = s.replace(c, '') 
    return (s)

'''
Standard answer: 
def remove_Char(s,c) :  
    counts = s.count(c) 
    s = list(s) 
    while counts :  
        s.remove(c) 
        counts -= 1 
    s = '' . join(s)   
    return (s) 
'''
assert remove_Char("aba",'a') == "b"
assert remove_Char("toggle",'g') == "tole"
assert remove_Char("aabbc",'b') == "aac"
