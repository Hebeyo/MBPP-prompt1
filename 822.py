"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to return true if the password is valid.
'''

def pass_validity(p):
    import re
    if (len(p)<6 or len(p)>12):
        return False
    if not re.search("[a-z]",p):
        return False
    if not re.search("[0-9]",p):
        return False
    if not re.search("[A-Z]",p):
        return False
    if not re.search("[$#@]",p):
        return False
    if re.search("\s",p):
        return False
    return True

'''
Standard answer: 
import re
def pass_validity(p):
 x = True
 while x:  
    if (len(p)<6 or len(p)>12):
        break
    elif not re.search("[a-z]",p):
        break
    elif not re.search("[0-9]",p):
        break
    elif not re.search("[A-Z]",p):
        break
    elif not re.search("[$#@]",p):
        break
    elif re.search("\s",p):
        break
    else:
        return True
        x=False
        break

 if x:
    return False
'''
assert pass_validity("password")==False
assert pass_validity("Password@10")==True
assert pass_validity("password@10")==False
