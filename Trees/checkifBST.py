class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        

def checkBST(root):
    
    def dfs(root, lower, upper):
        
        if not root:
            return True
        
        if root.val >= upper or root.val <= lower:
            return False
        
        return dfs(root.left, lower, root.val) and dfs(root.right, root.val, upper)
    
    return dfs(root, float('-inf'), float('inf'))

root = TreeNode(2) 
root.left = TreeNode(1) 
root.right = TreeNode(3) 
root.right.left = TreeNode(4) 
root.right.right = TreeNode(5)

print(checkBST(root)) 