"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to convert a string to a list.
'''

def Convert(string): 
    li = list(string.split(" ")) 
    return li

'''
Standard answer: 
def Convert(string): 
    li = list(string.split(" ")) 
    return li 
'''
assert Convert('python program') == ['python','program']
assert Convert('Data Analysis') ==['Data','Analysis']
assert Convert('Hadoop Training') == ['Hadoop','Training']
