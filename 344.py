"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find number of elements with odd factors in a given range.
'''

def count_Odd_Squares(n,m): 
    count = 0
    for i in range(n, m+1):
        if (int(i**0.5)**2 == i):
            count += 1
    return count

'''
Standard answer: 
def count_Odd_Squares(n,m): 
    return int(m**0.5) - int((n-1)**0.5) 
'''
assert count_Odd_Squares(5,100) == 8
assert count_Odd_Squares(8,65) == 6
assert count_Odd_Squares(2,5) == 1
