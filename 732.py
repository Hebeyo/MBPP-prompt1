"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to replace all occurrences of spaces, commas, or dots with a colon.
'''

def replace_specialchar(text):
    return (text.replace(' ',',').replace(',',':').replace('.',':'))

'''
Standard answer: 
import re
def replace_specialchar(text):
 return (re.sub("[ ,.]", ":", text))
'''
assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')
assert replace_specialchar('a b c,d e f')==('a:b:c:d:e:f')
assert replace_specialchar('ram reshma,ram rahim')==('ram:reshma:ram:rahim')
