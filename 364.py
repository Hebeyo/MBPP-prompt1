"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to find the number of flips required to make the given binary string a sequence of alternate characters.
'''

def min_flip_to_make_string_alternate(str): 
	count1 = 0
	count2 = 0
	for i in range(len(str)): 
		if i % 2 == 0: 
			# count1 is for 01010101... 
			if str[i] == '1': 
				count1 += 1
			# count2 is for 10101010... 
			else: 
				count2 += 1
		else: 
			# count1 is for 10101010... 
			if str[i] == '0': 
				count1 += 1
			# count2 is for 01010101... 
			else: 
				count2 += 1
	return min(count1, count2)

'''
Standard answer: 
def make_flip(ch): 
	return '1' if (ch == '0') else '0'
def get_flip_with_starting_charcter(str, expected): 
	flip_count = 0
	for i in range(len( str)): 
		if (str[i] != expected): 
			flip_count += 1
		expected = make_flip(expected) 
	return flip_count 
def min_flip_to_make_string_alternate(str): 
	return min(get_flip_with_starting_charcter(str, '0'),get_flip_with_starting_charcter(str, '1')) 
'''
assert min_flip_to_make_string_alternate("0001010111") == 2
assert min_flip_to_make_string_alternate("001") == 1
assert min_flip_to_make_string_alternate("010111011") == 2 
