"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the next smallest palindrome of a specified number.
'''

def next_smallest_palindrome(num):
    num += 1
    while str(num) != str(num)[::-1]:
        num += 1
    return num

'''
Standard answer: 
import sys
def next_smallest_palindrome(num):
    numstr = str(num)
    for i in range(num+1,sys.maxsize):
        if str(i) == str(i)[::-1]:
            return i
'''
assert next_smallest_palindrome(99)==101
assert next_smallest_palindrome(1221)==1331
assert next_smallest_palindrome(120)==121
