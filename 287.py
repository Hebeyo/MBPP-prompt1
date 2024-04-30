"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the sum of squares of first n even natural numbers.
'''

def square_Sum(n):
    sum = 0
    for i in range(1, n + 1):
        sum += (2 * i) ** 2
    return sum


'''
Standard answer: 
def square_Sum(n):  
    return int(2*n*(n+1)*(2*n+1)/3)
'''
assert square_Sum(2) == 20
assert square_Sum(3) == 56
assert square_Sum(4) == 120
