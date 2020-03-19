class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.left = self.right = None
        

def levelorder(root):
    
    q = [root]
    res = []
    
    while any(q):
        temp = []
        for _ in range(len(q)):
            node = q.pop(0)
            temp.append(node.val)
            
            if node.left:
                q.append(node.left)
                
            if node.right:
                q.append(node.right)
        res.append(temp)
        
    for e in res:
        print(e)

root = TreeNode(2) 
root.left = TreeNode(1) 
root.right = TreeNode(3) 
root.right.left = TreeNode(4) 
root.right.right = TreeNode(5)

levelorder(root)