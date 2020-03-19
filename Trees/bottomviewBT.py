class TreeNode:
    
    def __init__(self, val):
        self.val = val
        self.hd = 0
        self.left = self.right = None


def bottomView(root):
    
    if root is None:
        return
    
    q = []
    hdist = {}
    
    q.append(root)
    
    while any(q):
        
        curr = q.pop(0)
        hd = curr.hd
        hdist[hd] = curr.val
        
        if curr.left is not None:
            curr.left.hd = hd - 1
            q.append(curr.left)
            
        if curr.right is not None:
            curr.right.hd = hd + 1
            q.append(curr.right)
            
    print(list(hdist.values()))
        
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.right = TreeNode(6)
root.left.left.right = TreeNode(7)
root.right.right.left = TreeNode(8)
root.left.left.right.left = TreeNode(9)
root.left.left.right.left.left = TreeNode(10)
root.right.right.left.right = TreeNode(11)

bottomView(root) 