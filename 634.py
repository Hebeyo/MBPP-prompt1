"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the sum of fourth power of first n even natural numbers.
'''

def even_Power_Sum(n):
    sum = 0
    for i in range(1,n + 1):
        j = 2*i
        sum = sum + (j*j*j*j)
    return sum

'''
Standard answer: 
def even_Power_Sum(n): 
    sum = 0; 
    for i in range(1,n + 1): 
        j = 2*i; 
        sum = sum + (j*j*j*j); 
    return sum; 
'''
assert even_Power_Sum(2) == 272
assert even_Power_Sum(3) == 1568
assert even_Power_Sum(4) == 5664
