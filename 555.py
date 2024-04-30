"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the difference between sum of cubes of first n natural numbers and the sum of first n natural numbers.
'''

def difference(n) :  
    sum1 = 0
    sum2 = 0
    for i in range(1,n+1) : 
        sum1 += i * i*i
        sum2 += i
    return sum1 - sum2

'''
Standard answer: 
def difference(n) :  
    S = (n*(n + 1))//2;  
    res = S*(S-1);  
    return res;  
'''
assert difference(3) == 30
assert difference(5) == 210
assert difference(2) == 6
