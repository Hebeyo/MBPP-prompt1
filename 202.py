"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to remove even characters in a string.
'''

def remove_even(str1):
    return str1[::2]

'''
Standard answer: 
def remove_even(str1):
 str2 = ''
 for i in range(1, len(str1) + 1):
    if(i % 2 != 0):
        str2 = str2 + str1[i - 1]
 return str2
'''
assert remove_even("python")==("pto")
assert remove_even("program")==("porm")
assert remove_even("language")==("lnug")
