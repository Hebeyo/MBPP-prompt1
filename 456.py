"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to reverse strings in a given list of string values.
'''

def reverse_string_list(stringlist):
    result = []
    for x in stringlist:
        result.append(x[::-1])
    return result

'''
Standard answer: 
def reverse_string_list(stringlist):
    result = [x[::-1] for x in stringlist]
    return result
'''
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
assert reverse_string_list(['john','amal','joel','george'])==['nhoj','lama','leoj','egroeg']
assert reverse_string_list(['jack','john','mary'])==['kcaj','nhoj','yram']
