"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the median of a trapezium.
'''

def median_trapezium(base1,base2,height):
    median = 0.5 * (base1+ base2)
    return median

'''
Standard answer: 
def median_trapezium(base1,base2,height):
 median = 0.5 * (base1+ base2)
 return median
'''
assert median_trapezium(15,25,35)==20
assert median_trapezium(10,20,30)==15
assert median_trapezium(6,9,4)==7.5
