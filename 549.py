"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the sum of fifth power of first n odd natural numbers.
'''

def odd_Num_Sum(n) : 
    sm = 0
    for i in range(1,n+1) : 
        sm = sm + (2*i-1)*(2*i-1)*(2*i-1)*(2*i-1)*(2*i-1)     
    return sm

'''
Standard answer: 
def odd_Num_Sum(n) : 
    j = 0
    sm = 0
    for i in range(1,n+1) : 
        j = (2*i-1) 
        sm = sm + (j*j*j*j*j)     
    return sm 
'''
assert odd_Num_Sum(1) == 1
assert odd_Num_Sum(2) == 244
assert odd_Num_Sum(3) == 3369
