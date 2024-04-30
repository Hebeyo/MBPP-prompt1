"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to toggle characters case in a string.
'''

def toggle_string(string):
    new_string = ""
    for i in string:
        if i.isupper():
            new_string += i.lower()
        else:
            new_string += i.upper()
    return new_string

'''
Standard answer: 
def toggle_string(string):
 string1 = string.swapcase()
 return string1
'''
assert toggle_string("Python")==("pYTHON")
assert toggle_string("Pangram")==("pANGRAM")
assert toggle_string("LIttLE")==("liTTle")
