"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to calculate the difference between the squared sum of first n natural numbers and the sum of squared first n natural numbers.
'''

def sum_difference(n):
    sumofsquares = 0
    squareofsum = 0
    for num in range(1, n+1):
        sumofsquares += num * num
        squareofsum += num
    squareofsum = squareofsum ** 2
    return squareofsum - sumofsquares

'''
Standard answer: 
def sum_difference(n):
    sumofsquares = 0
    squareofsum = 0
    for num in range(1, n+1):
        sumofsquares += num * num
        squareofsum += num
    squareofsum = squareofsum ** 2
    return squareofsum - sumofsquares
'''
assert sum_difference(12)==5434
assert sum_difference(20)==41230
assert sum_difference(54)==2151270
