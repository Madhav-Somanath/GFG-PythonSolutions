def toString(a):
    
    return " ".join(a)

def permute(arr, l, r):
    
    if l==r: 
        print(toString(arr))
        
    else: 
        for i in range(l,r+1): 
            arr[l], arr[i] = arr[i], arr[l] 
            permute(arr, l+1, r) 
            arr[l], arr[i] = arr[i], arr[l]