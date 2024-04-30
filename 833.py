"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to get dictionary keys as a list.
'''

def get_key(dict):
    return list(dict.keys())

'''
Standard answer: 
def get_key(dict): 
    list = [] 
    for key in dict.keys(): 
        list.append(key)           
    return list
'''
assert get_key({1:'python',2:'java'})==[1,2]
assert get_key({10:'red',20:'blue',30:'black'})==[10,20,30]
assert get_key({27:'language',39:'java',44:'little'})==[27,39,44]
