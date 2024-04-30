"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether the elements in a list are same or not.
'''

def chkList(lst):
    if len(set(lst)) == 1:
        return True
    return False

'''
Standard answer: 
def chkList(lst): 
    return len(set(lst)) == 1
'''
assert chkList(['one','one','one']) == True
assert chkList(['one','Two','Three']) == False
assert chkList(['bigdata','python','Django']) == False
