"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find palindromes in a given list of strings using lambda function.
'''

def palindrome_lambda(texts):
  result = []
  for text in texts:
    if text == "".join(reversed(text)):
      result.append(text)
  return result

'''
Standard answer: 
def palindrome_lambda(texts):
  result = list(filter(lambda x: (x == "".join(reversed(x))), texts))
  return result
'''
assert palindrome_lambda(["php", "res", "Python", "abcd", "Java", "aaa"])==['php', 'aaa']
assert palindrome_lambda(["abcd", "Python", "abba", "aba"])==['abba', 'aba']
assert palindrome_lambda(["abcd", "abbccbba", "abba", "aba"])==['abbccbba', 'abba', 'aba']
