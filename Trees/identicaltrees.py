class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        

def identicalTree(t1, t2):
    
    if t1 is None and t2 is None:
        return True
    
    if t1 and t2:
        return t1.val == t2.val and identicalTree(t1.left, t2.left) and identicalTree(t1.right, t2.right)
    
    return False


root1 = TreeNode(1) 
root2 = TreeNode(1)

root1.left = TreeNode(2) 
root1.right = TreeNode(3) 
root1.left.left = TreeNode(4) 
root1.left.right = TreeNode(5) 
  
root2.left = TreeNode(2) 
root2.right = TreeNode(3) 
root2.left.left = TreeNode(4) 
root2.left.right = TreeNode(5) 

print(identicalTree(root1, root2))