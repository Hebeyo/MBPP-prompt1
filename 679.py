"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to access dictionary key’s element by index.
'''

def access_key(dictionary, index):
    return list(dictionary.keys())[index]

'''
Standard answer: 
def access_key(ditionary,key):
  return list(ditionary)[key]
'''
assert access_key({'physics': 80, 'math': 90, 'chemistry': 86},0)== 'physics'
assert access_key({'python':10, 'java': 20, 'C++':30},2)== 'C++'
assert access_key({'program':15,'computer':45},1)== 'computer'
