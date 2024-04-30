"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to add all the numbers in a list and divide it with the length of the list.
'''

def sum_num(numbers):
    return sum(numbers)/len(numbers)

'''
Standard answer: 
def sum_num(numbers):
    total = 0
    for x in numbers:
        total += x
    return total/len(numbers) 
'''
assert sum_num((8, 2, 3, 0, 7))==4.0
assert sum_num((-10,-20,-30))==-20.0
assert sum_num((19,15,18))==17.333333333333332
