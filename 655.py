"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the sum of fifth power of n natural numbers.
'''

def fifth_Power_Sum(n) : 
    sm = 0 
    for i in range(1,n+1) : 
        sm = sm + (i**5) 
    return sm

'''
Standard answer: 
def fifth_Power_Sum(n) : 
    sm = 0 
    for i in range(1,n+1) : 
        sm = sm + (i*i*i*i*i) 
    return sm 
'''
assert fifth_Power_Sum(2) == 33
assert fifth_Power_Sum(4) == 1300
assert fifth_Power_Sum(3) == 276
