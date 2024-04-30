"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to replace maximum n occurrences of spaces, commas, or dots with a colon.
'''

def replace_max_specialchar(text,n):
    text = list(text)
    count = 0
    for i in range(len(text)):
        if text[i] == ' ' or text[i] == ',' or text[i] == '.':
            text[i] = ':'
            count += 1
            if count == n:
                break
    return ''.join(text)


'''
Standard answer: 
import re
def replace_max_specialchar(text,n):
 return (re.sub("[ ,.]", ":", text, n))
'''
assert replace_max_specialchar('Python language, Programming language.',2)==('Python:language: Programming language.')
assert replace_max_specialchar('a b c,d e f',3)==('a:b:c:d e f')
assert replace_max_specialchar('ram reshma,ram rahim',1)==('ram:reshma,ram rahim')
