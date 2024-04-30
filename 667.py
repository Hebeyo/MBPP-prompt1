"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to count number of vowels in the string.
'''

def Check_Vow(string, vowels):
    count = 0
    for i in string:
        if i in vowels:
            count += 1
    return count

'''
Standard answer: 
def Check_Vow(string, vowels): 
    final = [each for each in string if each in vowels] 
    return(len(final)) 

'''
assert Check_Vow('corner','AaEeIiOoUu') == 2
assert Check_Vow('valid','AaEeIiOoUu') == 2
assert Check_Vow('true','AaEeIiOoUu') ==2
