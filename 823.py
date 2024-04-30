"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check if the given string starts with a substring using regex.
'''

import re
def check_substring(string, sample) : 
  if (sample in string): 
      y = "\A" + sample 
      x = re.search(y, string) 
      if x : 
          return ("string starts with the given substring") 
      else : 
          return ("string doesnt start with the given substring") 
  else : 
      return ("entered string isnt a substring")

'''
Standard answer: 
import re 
def check_substring(string, sample) : 
  if (sample in string): 
      y = "\A" + sample 
      x = re.search(y, string) 
      if x : 
          return ("string starts with the given substring") 
      else : 
          return ("string doesnt start with the given substring") 
  else : 
      return ("entered string isnt a substring")
'''
assert check_substring("dreams for dreams makes life fun", "makes") == 'string doesnt start with the given substring'
assert check_substring("Hi there how are you Hi alex", "Hi") == 'string starts with the given substring'
assert check_substring("Its been a long day", "been") == 'string doesnt start with the given substring'
