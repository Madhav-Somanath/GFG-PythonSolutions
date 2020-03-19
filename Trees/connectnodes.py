class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        self.next = None
        

def connect(root):
    
    if not root:
        return
    
    if root.left:
        root.left.next = root.right
        
    if root.right and root.next:
        if root.next.left:
            root.right.next = root.next.left
        elif root.next.right:
            root.right.next = root.next.right
            
    connect(root.left)
    connect(root.right)
