"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the previous palindrome of a specified number.
'''

def previous_palindrome(num):
    while True:
        num -= 1
        if str(num) == str(num)[::-1]:
            return num

'''
Standard answer: 
def previous_palindrome(num):
    for x in range(num-1,0,-1):
        if str(x) == str(x)[::-1]:
            return x
'''
assert previous_palindrome(99)==88
assert previous_palindrome(1221)==1111
assert previous_palindrome(120)==111
