"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to convert a given string to a tuple.
'''

def string_to_tuple(str1):
    result = tuple(x for x in str1 if not x.isspace()) 
    return result

'''
Standard answer: 
def string_to_tuple(str1):
    result = tuple(x for x in str1 if not x.isspace()) 
    return result
'''
assert string_to_tuple("python 3.0")==('p', 'y', 't', 'h', 'o', 'n', '3', '.', '0')
assert string_to_tuple("item1")==('i', 't', 'e', 'm', '1')
assert string_to_tuple("15.10")==('1', '5', '.', '1', '0')
