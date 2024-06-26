"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function that matches a string that has an 'a' followed by anything, ending in 'b'.
'''

def text_starta_endb(text):
    import re
    patterns = 'a.*b$'
    if re.search(patterns,  text):
        return 'Found a match!'
    else:
        return('Not matched!')

'''
Standard answer: 
import re
def text_starta_endb(text):
        patterns = 'a.*?b$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
'''
assert text_starta_endb("aabbbb")==('Found a match!')
assert text_starta_endb("aabAbbbc")==('Not matched!')
assert text_starta_endb("accddbbjjj")==('Not matched!')
