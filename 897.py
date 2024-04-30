"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether the word is present in a given sentence or not.
'''

def is_Word_Present(sentence,word):
    return word in sentence.split(" ")

'''
Standard answer: 
def is_Word_Present(sentence,word): 
    s = sentence.split(" ") 
    for i in s:  
        if (i == word): 
            return True
    return False
'''
assert is_Word_Present("machine learning","machine") == True
assert is_Word_Present("easy","fun") == False
assert is_Word_Present("python language","code") == False
