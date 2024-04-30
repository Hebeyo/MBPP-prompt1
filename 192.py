"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to check whether a string has atleast one letter and one number.
'''

def check_String(str): 
    flag_l = False
    flag_n = False
    for i in str: 
        if i.isalpha(): 
            flag_l = True  
        if i.isdigit(): 
            flag_n = True
    return flag_l and flag_n

'''
Standard answer: 
def check_String(str): 
    flag_l = False
    flag_n = False
    for i in str: 
        if i.isalpha(): 
            flag_l = True  
        if i.isdigit(): 
            flag_n = True
    return flag_l and flag_n 
'''
assert check_String('thishasboth29') == True
assert check_String('python') == False
assert check_String ('string') == False
