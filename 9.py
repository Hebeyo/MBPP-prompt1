"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the minimum number of rotations required to get the same string.
'''

def find_Rotations(s):
    n = len(s)
    for i in range(1,n+1):
        if s == s[i:] + s[:i]:
            return i
    return n

'''
Standard answer: 
def find_Rotations(str): 
    tmp = str + str
    n = len(str) 
    for i in range(1,n + 1): 
        substring = tmp[i: i+n] 
        if (str == substring): 
            return i 
    return n 
'''
assert find_Rotations("aaaa") == 1
assert find_Rotations("ab") == 2
assert find_Rotations("abc") == 3
