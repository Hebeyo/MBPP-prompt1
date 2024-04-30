"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the next perfect square greater than a given number.
'''

def next_Perfect_Square(N): 
    nextN = N
    while True:
        nextN += 1
        if int(nextN ** 0.5) == nextN ** 0.5:
            return nextN

'''
Standard answer: 
import math  
def next_Perfect_Square(N): 
    nextN = math.floor(math.sqrt(N)) + 1
    return nextN * nextN 
'''
assert next_Perfect_Square(35) == 36
assert next_Perfect_Square(6) == 9
assert next_Perfect_Square(9) == 16
