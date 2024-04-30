"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the average of even numbers till a given even number.
'''

def average_Even(n):
    sum = 0
    count = 0
    while n >= 2:
        count = count + 1
        sum = sum + n
        n = n - 2
    return sum // count

'''
Standard answer: 
def average_Even(n) : 
    if (n% 2!= 0) : 
        return ("Invalid Input") 
        return -1  
    sm = 0
    count = 0
    while (n>= 2) : 
        count = count+1
        sm = sm+n 
        n = n-2
    return sm // count 
'''
assert average_Even(2) == 2
assert average_Even(4) == 3
assert average_Even(100) == 51
