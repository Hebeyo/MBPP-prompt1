"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find out, if the given number is abundant.
'''

def is_abundant(n):
    sum=0
    for i in range(1,n):
        if n%i==0:
            sum+=i
    return sum>n

'''
Standard answer: 
def is_abundant(n):
    fctrsum = sum([fctr for fctr in range(1, n) if n % fctr == 0])
    return fctrsum > n
'''
assert is_abundant(12)==True
assert is_abundant(13)==False
assert is_abundant(9)==False
