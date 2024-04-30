"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to check whether it follows the sequence given in the patterns array.
'''

def is_samepatterns(colors, patterns):
    if len(colors) != len(patterns):
        return False
    dict = {}
    for i in range(len(colors)):
        if patterns[i] not in dict:
            dict[patterns[i]] = colors[i]
        elif dict[patterns[i]] != colors[i]:
            return False
    return True

'''
Standard answer: 
def is_samepatterns(colors, patterns):    
    if len(colors) != len(patterns):
        return False    
    sdict = {}
    pset = set()
    sset = set()    
    for i in range(len(patterns)):
        pset.add(patterns[i])
        sset.add(colors[i])
        if patterns[i] not in sdict.keys():
            sdict[patterns[i]] = []

        keys = sdict[patterns[i]]
        keys.append(colors[i])
        sdict[patterns[i]] = keys

    if len(pset) != len(sset):
        return False   

    for values in sdict.values():

        for i in range(len(values) - 1):
            if values[i] != values[i+1]:
                return False

    return True
'''
assert is_samepatterns(["red","green","green"], ["a", "b", "b"])==True 
assert is_samepatterns(["red","green","greenn"], ["a","b","b"])==False 
assert is_samepatterns(["red","green","greenn"], ["a","b"])==False 
