"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to split a string into characters.
'''

def split(word): 
    return [char for char in word]


'''
Standard answer: 
def split(word): 
    return [char for char in word] 
'''
assert split('python') == ['p','y','t','h','o','n']
assert split('Name') == ['N','a','m','e']
assert split('program') == ['p','r','o','g','r','a','m']
