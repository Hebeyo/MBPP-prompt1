"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the first non-repeated character in a given string.
'''

def first_non_repeating_character(str1):
  for i in range(len(str1)):
    if str1.count(str1[i]) == 1:
      return str1[i]
  return None

'''
Standard answer: 
def first_non_repeating_character(str1):
  char_order = []
  ctr = {}
  for c in str1:
    if c in ctr:
      ctr[c] += 1
    else:
      ctr[c] = 1 
      char_order.append(c)
  for c in char_order:
    if ctr[c] == 1:
      return c
  return None
'''
assert first_non_repeating_character("abcabc") == None
assert first_non_repeating_character("abc") == "a"
assert first_non_repeating_character("ababc") == "c"
