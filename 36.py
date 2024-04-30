"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the nth digit in the proper fraction of two given numbers.
'''

def find_Nth_Digit(p,q,N) :  
    while (N > 0) : 
        N -= 1;  
        p *= 10;  
        res = p // q;  
        p %= q;  
    return res;

'''
Standard answer: 
def find_Nth_Digit(p,q,N) :  
    while (N > 0) : 
        N -= 1;  
        p *= 10;  
        res = p // q;  
        p %= q;  
    return res;  
'''
assert find_Nth_Digit(1,2,1) == 5
assert find_Nth_Digit(3,5,1) == 6
assert find_Nth_Digit(5,6,5) == 3
