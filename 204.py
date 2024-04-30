"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count the occurrence of a given character in a string.
'''

def count(s,c) : 
    res = 0 
    for i in s: 
        if (i == c): 
            res = res + 1
    return res

'''
Standard answer: 
def count(s,c) : 
    res = 0 
    for i in range(len(s)) : 
        if (s[i] == c): 
            res = res + 1
    return res 
'''
assert count("abcc","c") == 2
assert count("ababca","a") == 3
assert count("mnmm0pm","m") == 4
