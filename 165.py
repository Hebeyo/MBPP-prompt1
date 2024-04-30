"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count characters at same position in a given string (lower and uppercase characters) as in english alphabet.
'''

def count_char_position(str1):
    count_chars = 0
    for i in range(len(str1)):
        if i == ord(str1[i].upper()) - ord('A'):
            count_chars += 1
    return count_chars


'''
Standard answer: 
def count_char_position(str1): 
    count_chars = 0
    for i in range(len(str1)):
        if ((i == ord(str1[i]) - ord('A')) or 
            (i == ord(str1[i]) - ord('a'))): 
            count_chars += 1
    return count_chars 
'''
assert count_char_position("xbcefg") == 2
assert count_char_position("ABcED") == 3
assert count_char_position("AbgdeF") == 5
