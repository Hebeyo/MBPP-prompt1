"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to count the most common character in a given string.
'''

def max_char(str1):
    temp = {}
    for i in str1:
        if i in temp:
            temp[i] += 1
        else:
            temp[i] = 1
    max_char = max(temp, key = temp.get)
    return max_char

'''
Standard answer: 
from collections import Counter 
def max_char(str1):
    temp = Counter(str1) 
    max_char = max(temp, key = temp.get)
    return max_char
'''
assert max_char("hello world")==('l')
assert max_char("hello ")==('l')
assert max_char("python pr")==('p')
