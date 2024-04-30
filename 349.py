"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether the given string is a binary string or not.
'''

def check(string) :
    for i in string :
        if i == "0" or i == "1" :
            pass
        else :
            return "No"
    return "Yes"

'''
Standard answer: 
def check(string) :
    p = set(string) 
    s = {'0', '1'} 
    if s == p or p == {'0'} or p == {'1'}: 
        return ("Yes") 
    else : 
        return ("No") 
'''
assert check("01010101010") == "Yes"
assert check("name0") == "No"
assert check("101") == "Yes"
