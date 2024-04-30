"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find binomial co-efficient.
'''

def binomial_Coeff(n,k):
    if k > n:
        return 0
    if k==0 or k ==n:
        return 1
    return binomial_Coeff(n-1,k-1) + binomial_Coeff(n-1,k)

'''
Standard answer: 
def binomial_Coeff(n,k): 
    if k > n : 
       return 0
    if k==0 or k ==n : 
        return 1 
    return binomial_Coeff(n-1,k-1) + binomial_Coeff(n-1,k) 
'''
assert binomial_Coeff(5,2) == 10
assert binomial_Coeff(4,3) == 4
assert binomial_Coeff(3,2) == 3
assert binomial_Coeff(14,6) == 3003
