"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find quotient of two numbers.
'''

def find(n,m):
    q = 0
    while n >= m:
        n -= m
        q += 1
    return q

'''
Standard answer: 
def find(n,m):  
    q = n//m 
    return (q)
'''
assert find(10,3) == 3
assert find(4,2) == 2
assert find(20,5) == 4
