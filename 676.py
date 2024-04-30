"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to remove everything except alphanumeric characters from the given string by using regex.
'''

import re
def remove_extra_char(text1):
  return re.sub(r'\W+', '', text1)

'''
Standard answer: 
import re
def remove_extra_char(text1):
  pattern = re.compile('[\W_]+')
  return (pattern.sub('', text1))
'''
assert remove_extra_char('**//Google Android// - 12. ') == 'GoogleAndroid12'
assert remove_extra_char('****//Google Flutter//*** - 36. ') == 'GoogleFlutter36'
assert remove_extra_char('**//Google Firebase// - 478. ') == 'GoogleFirebase478'
