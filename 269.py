"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the ascii value of a character.
'''

def ascii_value(k):
    return ord(k)

'''
Standard answer: 
def ascii_value(k):
  ch=k
  return ord(ch)
'''
assert ascii_value('A')==65
assert ascii_value('R')==82
assert ascii_value('S')==83
