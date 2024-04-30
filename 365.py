"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count the number of digits of a given number.
'''

def count_Digit(n):
    return len(str(n))

'''
Standard answer: 
def count_Digit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count
'''
assert count_Digit(12345) == 5
assert count_Digit(11223305) == 8
assert count_Digit(4123459) == 7
