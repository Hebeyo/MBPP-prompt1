"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to replace multiple occurence of character by single.
'''

def replace(string, char):
    new_string = ""
    for i in string:
        if i == char:
            if i != new_string[-1:]:
                new_string += i
        else:
            new_string += i
    return new_string

'''
Standard answer: 
import re 
def replace(string, char): 
    pattern = char + '{2,}'
    string = re.sub(pattern, char, string) 
    return string 
'''
assert replace('peep','e') == 'pep'
assert replace('Greek','e') == 'Grek'
assert replace('Moon','o') == 'Mon'
