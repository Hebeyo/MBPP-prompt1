"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find minimum sum of factors of a given number.
'''

def find_Min_Sum(num): 
    sum = 0
    i = 2
    while(i * i <= num): 
        while(num % i == 0): 
            sum += i 
            num /= i 
        i += 1
    sum += num 
    return sum

'''
Standard answer: 
def find_Min_Sum(num): 
    sum = 0
    i = 2
    while(i * i <= num): 
        while(num % i == 0): 
            sum += i 
            num /= i 
        i += 1
    sum += num 
    return sum
'''
assert find_Min_Sum(12) == 7
assert find_Min_Sum(105) == 15
assert find_Min_Sum(2) == 2
