"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to remove all digits from a list of strings.
'''

def remove(list): 
    for i in range(len(list)): 
        list[i] = ''.join([j for j in list[i] if not j.isdigit()]) 
    return list

'''
Standard answer: 
import re  
def remove(list): 
    pattern = '[0-9]'
    list = [re.sub(pattern, '', i) for i in list] 
    return list
'''
assert remove(['4words', '3letters', '4digits']) == ['words', 'letters', 'digits']
assert remove(['28Jan','12Jan','11Jan']) == ['Jan','Jan','Jan']
assert remove(['wonder1','wonder2','wonder3']) == ['wonder','wonder','wonder']
