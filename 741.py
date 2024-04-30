"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether all the characters are same or not.
'''

def all_Characters_Same(s) :
    return all(i == s[0] for i in s)

'''
Standard answer: 
def all_Characters_Same(s) :
    n = len(s)
    for i in range(1,n) :
        if s[i] != s[0] :
            return False
    return True
'''
assert all_Characters_Same("python") == False
assert all_Characters_Same("aaa") == True
assert all_Characters_Same("data") == False
