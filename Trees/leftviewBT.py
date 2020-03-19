class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        

def leftView(root, level, maxlevel):
    
    if not root:
        return
    
    if maxlevel[0] < level:
        print(level, "level")
        print(maxlevel, "maxlevel")
        print(root.val)
        maxlevel[0] = level
        
    leftView(root.left, level+1, maxlevel)
    leftView(root.right, level+1, maxlevel)
    
    
def driver(root):
    maxlevel = [0]
    leftView(root, 1, maxlevel)


root = TreeNode(12) 
root.left = TreeNode(10) 
root.right = TreeNode(20) 
root.right.left = TreeNode(25) 
root.right.right = TreeNode(40) 

driver(root)