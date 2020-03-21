def rev(s):
    
    words = s.split(' ') 
    stng =[] 
    
    for word in words: 
        stng.insert(0, word) 
    
    print(" ".join(stng)) 
    
