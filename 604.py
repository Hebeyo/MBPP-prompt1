"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to reverse words in a given string.
'''

def reverse_words(s):
        return ' '.join(reversed(s.split()))

'''
Standard answer: 
def reverse_words(s):
        return ' '.join(reversed(s.split()))
'''
assert reverse_words("python program")==("program python")
assert reverse_words("java language")==("language java")
assert reverse_words("indian man")==("man indian")
