"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to find the maximum length of sublist.
'''

def Find_Max_Length(lst):  
    maxLength = 0
    for x in lst:
        if len(x) > maxLength:
            maxLength = len(x)
    return maxLength

'''
Standard answer: 
def Find_Max_Length(lst):  
    maxLength = max(len(x) for x in lst )
    return maxLength 
'''
assert Find_Max_Length([[1],[1,4],[5,6,7,8]]) == 4
assert Find_Max_Length([[0,1],[2,2,],[3,2,1]]) == 3
assert Find_Max_Length([[7],[22,23],[13,14,15],[10,20,30,40,50]]) == 5
