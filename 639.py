"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to sum the length of the names of a given list of names after removing the names that start with a lowercase letter.
'''

def sample_nam(sample_names):
  n=0
  for name in sample_names:
    if name[0].isupper() and name[1:].islower():
      n+=len(name)
  return n

'''
Standard answer: 
def sample_nam(sample_names):
  sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
  return len(''.join(sample_names))
'''
assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16
assert sample_nam(["php", "res", "Python", "abcd", "Java", "aaa"])==10
assert sample_nam(["abcd", "Python", "abba", "aba"])==6
