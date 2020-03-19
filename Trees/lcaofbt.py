class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def lcarecur(root, a, b):
    
    if root == a or root == b:
        return root
    
    left = right = None
    
    if root.left:
        left = lcarecur(root.left, a, b)
    if root.right:
        right = lcarecur(root.right, a, b)
    
    if left and right:
        return root
    
    else:
        return left or right

# confused about this recursive solution

def lcaiter(root, a, b):
    return 
