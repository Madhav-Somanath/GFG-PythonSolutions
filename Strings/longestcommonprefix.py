def longprefix(strs):
    
    prefix=[]
    
    for x in zip(*strs):
            
        if len(set(x)) == 1:
            prefix.append(x[0])
            
        else:
            break
        
    return "".join(prefix)
    
y = ["flower","flow","flight"]
print(longprefix(y))