"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the sum of all even natural numbers within the range l and r.
'''

def sum_Even(l,r): 
    sum = 0
    for i in range(l,r+1): 
        if (i % 2 == 0) : 
            sum += i 
    return sum

'''
Standard answer: 
def sum_Natural(n): 
    sum = (n * (n + 1)) 
    return int(sum) 
def sum_Even(l,r): 
    return (sum_Natural(int(r / 2)) - sum_Natural(int((l - 1) / 2))) 
'''
assert sum_Even(2,5) == 6
assert sum_Even(3,8) == 18
assert sum_Even(4,6) == 10
