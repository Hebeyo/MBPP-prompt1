"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to extract specified size of strings from a give list of string values.
'''

def extract_string(str, l):
    result = []
    for e in str:
        if len(e) == l:
            result.append(e)
    return result

'''
Standard answer: 
def extract_string(str, l):
    result = [e for e in str if len(e) == l] 
    return result
'''
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,6)==['Python']
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,9)==['exercises']
