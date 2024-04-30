"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether the sum of divisors are same or not.
'''

def areEquivalent(num1,num2):
    sum1 = 1
    sum2 = 1
    for i in range(2, num1):
        if num1 % i == 0:
            sum1 += i
    for i in range(2, num2):
        if num2 % i == 0:
            sum2 += i
    return sum1 == sum2

'''
Standard answer: 
import math 
def divSum(n): 
    sum = 1; 
    i = 2; 
    while(i * i <= n): 
        if (n % i == 0): 
            sum = (sum + i +math.floor(n / i)); 
        i += 1; 
    return sum; 
def areEquivalent(num1,num2): 
    return divSum(num1) == divSum(num2); 
'''
assert areEquivalent(36,57) == False
assert areEquivalent(2,4) == False
assert areEquivalent(23,47) == True
