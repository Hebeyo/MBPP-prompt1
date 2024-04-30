"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to put spaces between words starting with capital letters in a given string by using regex.
'''

def capital_words_spaces(str1):
  new_str = ""
  for i in str1:
    if i.isupper() and new_str:
      new_str += " " + i
    else:
      new_str += i
  return new_str

'''
Standard answer: 
import re
def capital_words_spaces(str1):
  return re.sub(r"(\w)([A-Z])", r"\1 \2", str1)
'''
assert capital_words_spaces("Python") == 'Python'
assert capital_words_spaces("PythonProgrammingExamples") == 'Python Programming Examples'
assert capital_words_spaces("GetReadyToBeCodingFreak") == 'Get Ready To Be Coding Freak'
