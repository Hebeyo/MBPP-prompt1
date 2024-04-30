"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to extract values between quotation marks of a string.
'''

def extract_values(text):
    text = text.split(',')
    result = []
    for i in text:
        result.append(i.strip()[1:-1])
    return result

'''
Standard answer: 
import re
def extract_values(text):
 return (re.findall(r'"(.*?)"', text))
'''
assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']
assert extract_values('"python","program","language"')==['python','program','language']
assert extract_values('"red","blue","green","yellow"')==['red','blue','green','yellow']
