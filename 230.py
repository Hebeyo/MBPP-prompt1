"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to replace blank spaces with any character in a string.
'''

def replace_blank(str1,char):
    str2 = ""
    for i in str1:
        if i==" ":
            str2+=char
        else:
            str2+=i
    return str2

'''
Standard answer: 
def replace_blank(str1,char):
 str2 = str1.replace(' ', char)
 return str2
'''
assert replace_blank("hello people",'@')==("hello@people")
assert replace_blank("python program language",'$')==("python$program$language")
assert replace_blank("blank space","-")==("blank-space")
