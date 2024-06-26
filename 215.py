"""Complete the function with better-performing Python code. Use efficient function calls and looping structures, use efficient algorithms, avoid unnecessary complexity and waste of resources, ensure that the code is concise, and make full use of language features."""
'''Write a function to decode a run-length encoded given list.
'''

def decode_list(alist):
    result = []
    for i in range(len(alist)):
        if isinstance(alist[i], list):
            result += [alist[i][1]] * alist[i][0]
        else:
            result.append(alist[i])
    return result

'''
Standard answer: 
def decode_list(alist):
    def aux(g):
        if isinstance(g, list):
            return [(g[1], range(g[0]))]
        else:
            return [(g, [0])]
    return [x for g in alist for x, R in aux(g) for i in R]
'''
assert decode_list([[2, 1], 2, 3, [2, 4], 5,1])==[1,1,2,3,4,4,5,1]
assert decode_list(['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', [2, 'l'], 'y'])==['a', 'u', 't', 'o', 'm', 'a', 't', 'i', 'c', 'a', 'l', 'l', 'y']
assert decode_list(['p', 'y', 't', 'h', 'o', 'n'])==['p', 'y', 't', 'h', 'o', 'n']
