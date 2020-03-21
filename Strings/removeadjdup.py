def remvdup(s):
    
    res = []
    
    for c in s:
        if res and res[-1] == c:
            res.pop()
        else:
            res.append(c)
            
    return "".join(x for x in res)

y = "geeksforgeek"

print(remvdup(y))