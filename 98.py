"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to multiply all the numbers in a list and divide with the length of the list.
'''

def multiply_num(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total/len(numbers)

'''
Standard answer: 
def multiply_num(numbers):  
    total = 1
    for x in numbers:
        total *= x  
    return total/len(numbers) 
'''
assert multiply_num((8, 2, 3, -1, 7))==-67.2
assert multiply_num((-10,-20,-30))==-2000.0
assert multiply_num((19,15,18))==1710.0
