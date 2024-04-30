"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''[link text](https:// [link text](https:// [link text](https://)))write a function to convert a string to a list.
'''

def string_to_list(string): 
    return string.split(" ")


'''
Standard answer: 
def string_to_list(string): 
    lst = list(string.split(" ")) 
    return lst
'''
assert string_to_list("python programming")==['python','programming']
assert string_to_list("lists tuples strings")==['lists','tuples','strings']
assert string_to_list("write a program")==['write','a','program']
