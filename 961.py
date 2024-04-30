"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to convert a roman numeral to an integer.
'''

def roman_to_int(s):
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    int_val = 0
    for i in range(len(s)):
        if i > 0 and roman_dict[s[i]] > roman_dict[s[i-1]]:
            int_val += roman_dict[s[i]] - 2 * roman_dict[s[i-1]]
        else:
            int_val += roman_dict[s[i]]
    return int_val

'''
Standard answer: 
def roman_to_int(s):
        rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        int_val = 0
        for i in range(len(s)):
            if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
                int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
            else:
                int_val += rom_val[s[i]]
        return int_val
'''
assert roman_to_int('MMMCMLXXXVI')==3986
assert roman_to_int('MMMM')==4000
assert roman_to_int('C')==100
