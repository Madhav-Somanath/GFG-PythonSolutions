class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        

def identicalTree(t1, t2):
    
    if t1 is None and t2 is None:
        return True
    
    if t1 and t2:
        return t1.val == t2.val and identicalTree(t1.left, t2.right) and identicalTree(t1.right, t2.left)
    
    return False

def issymmetric(root):
    
    identicalTree(root,  root)
