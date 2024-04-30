"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to calculate the number of digits and letters in a string.
'''

def dig_let(s):
    l = sum(1 for c in s if c.isalpha())
    d = sum(1 for c in s if c.isdigit())
    return (l, d)

'''
Standard answer: 
def dig_let(s):
 d=l=0
 for c in s:
    if c.isdigit():
        d=d+1
    elif c.isalpha():
        l=l+1
    else:
        pass
 return (l,d)
'''
assert dig_let("python")==(6,0)
assert dig_let("program")==(7,0)
assert dig_let("python3.0")==(6,2)
