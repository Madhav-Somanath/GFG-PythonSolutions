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

def lcaiter(root, p, q):

        stack = [root]
        parent = {root: None}
        
        while p not in parent or q not in parent:

            node = stack.pop()
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)
                
        ancestors = set()

        while p:
            ancestors.add(p)
            p = parent[p]

        while q not in ancestors:
            q = parent[q]
            
        return q
