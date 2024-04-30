"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to split the given string at uppercase letters by using regex.
'''

import re
def split_list(text):
  return (re.findall('[A-Z][^A-Z]*', text))

'''
Standard answer: 
import re
def split_list(text):
  return (re.findall('[A-Z][^A-Z]*', text))
'''
assert split_list("LearnToBuildAnythingWithGoogle") == ['Learn', 'To', 'Build', 'Anything', 'With', 'Google']
assert split_list("ApmlifyingTheBlack+DeveloperCommunity") == ['Apmlifying', 'The', 'Black+', 'Developer', 'Community']
assert split_list("UpdateInTheGoEcoSystem") == ['Update', 'In', 'The', 'Go', 'Eco', 'System']
