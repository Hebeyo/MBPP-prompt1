"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to convert a list of multiple integers into a single integer.
'''

def convert(list): 
    res = int("".join(map(str, list)))  
    return (res)

'''
Standard answer: 
def convert(list): 
    s = [str(i) for i in list] 
    res = int("".join(s))  
    return (res) 
'''
assert convert([1,2,3]) == 123
assert convert([4,5,6]) == 456
assert convert([7,8,9]) == 789
