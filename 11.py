"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a python function to remove first and last occurrence of a given character from the string.
'''

def remove_Occ(s,ch):
    s = s.replace(ch,"",1)
    s = s[::-1].replace(ch,"",1)[::-1]
    return s

'''
Standard answer: 
def remove_Occ(s,ch): 
    for i in range(len(s)): 
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    for i in range(len(s) - 1,-1,-1):  
        if (s[i] == ch): 
            s = s[0 : i] + s[i + 1:] 
            break
    return s 
'''
assert remove_Occ("hello","l") == "heo"
assert remove_Occ("abcda","a") == "bcd"
assert remove_Occ("PHP","P") == "H"
assert remove_Occ("hellolloll","l") == "helollol"
assert remove_Occ("","l") == ""
