"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function that matches a string that has an a followed by two to three 'b'.
'''

import re
def text_match_two_three(text):
    if re.search('ab{2,3}',  text):
        return 'Found a match!'
    else:
        return('Not matched!')

'''
Standard answer: 
import re
def text_match_two_three(text):
        patterns = 'ab{2,3}'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
'''
assert text_match_two_three("ac")==('Not matched!')
assert text_match_two_three("dc")==('Not matched!')
assert text_match_two_three("abbbba")==('Found a match!')
