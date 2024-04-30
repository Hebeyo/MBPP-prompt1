"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find sum of all prime divisors of a given number.
'''

def Sum(N): 
    SumOfPrimeDivisors = [0]*(N + 1)   
    for i in range(2,N + 1) : 
        if (SumOfPrimeDivisors[i] == 0) : 
            for j in range(i,N + 1,i) : 
                SumOfPrimeDivisors[j] += i           
    return SumOfPrimeDivisors[N]

'''
Standard answer: 
def Sum(N): 
    SumOfPrimeDivisors = [0]*(N + 1)   
    for i in range(2,N + 1) : 
        if (SumOfPrimeDivisors[i] == 0) : 
            for j in range(i,N + 1,i) : 
                SumOfPrimeDivisors[j] += i           
    return SumOfPrimeDivisors[N] 
'''
assert Sum(60) == 10
assert Sum(39) == 16
assert Sum(40) == 7
