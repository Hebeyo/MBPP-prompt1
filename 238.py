"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count number of non-empty substrings of a given string.
'''

def number_of_substrings(str): 
    str_len = len(str)
    count = 0
    for i in range(str_len):
        for j in range(i, str_len):
            count += 1
    return count

'''
Standard answer: 
def number_of_substrings(str): 
	str_len = len(str); 
	return int(str_len * (str_len + 1) / 2); 
'''
assert number_of_substrings("abc") == 6
assert number_of_substrings("abcd") == 10
assert number_of_substrings("abcde") == 15
