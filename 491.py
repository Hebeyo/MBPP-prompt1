"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the sum of geometric progression series.
'''

def sum_gp(a,n,r):
    total = 0
    for i in range(n):
        total += a
        a *= r
    return total

'''
Standard answer: 
import math
def sum_gp(a,n,r):
 total = (a * (1 - math.pow(r, n ))) / (1- r)
 return total
'''
assert sum_gp(1,5,2)==31
assert sum_gp(1,5,4)==341
assert sum_gp(2,6,3)==728
