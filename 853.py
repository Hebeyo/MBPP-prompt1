"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find sum of odd factors of a number.
'''

def sum_of_odd_Factors(n): 
    res = 1
    while n % 2 == 0: 
        n = n // 2 
    for i in range(3,n + 1): 
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0: 
            count+=1 
            n = n // i 
            curr_term *= i 
            curr_sum += curr_term    
        res *= curr_sum  
    if n >= 2: 
        res *= (1 + n) 
    return res

'''
Standard answer: 
import math
def sum_of_odd_Factors(n): 
    res = 1
    while n % 2 == 0: 
        n = n // 2 
    for i in range(3,int(math.sqrt(n) + 1)): 
        count = 0
        curr_sum = 1
        curr_term = 1
        while n % i == 0: 
            count+=1 
            n = n // i 
            curr_term *= i 
            curr_sum += curr_term    
        res *= curr_sum  
    if n >= 2: 
        res *= (1 + n) 
    return res 
'''
assert sum_of_odd_Factors(30) == 24
assert sum_of_odd_Factors(18) == 13
assert sum_of_odd_Factors(2) == 1
