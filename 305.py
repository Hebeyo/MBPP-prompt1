"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to match two words from a list of words starting with letter 'p'.
'''

def start_withp(words):
    for word in words:
        if word.startswith('p') or word.startswith('P'):
            p = word.split()
            return (p[0], p[1])

'''
Standard answer: 
import re
def start_withp(words):
 for w in words:
        m = re.match("(P\w+)\W(P\w+)", w)
        if m:
            return m.groups()
'''
assert start_withp(["Python PHP", "Java JavaScript", "c c++"])==('Python', 'PHP')
assert start_withp(["Python Programming","Java Programming"])==('Python','Programming')
assert start_withp(["Pqrst Pqr","qrstuv"])==('Pqrst','Pqr')
