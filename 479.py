"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the first digit of a given number.
'''

def first_Digit(n) :  
    while n >= 10:  
        n = n // 10; 
    return n

'''
Standard answer: 
def first_Digit(n) :  
    while n >= 10:  
        n = n / 10; 
    return int(n) 
'''
assert first_Digit(123) == 1
assert first_Digit(456) == 4
assert first_Digit(12) == 1
