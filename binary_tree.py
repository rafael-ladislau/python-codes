class TreeNode:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def transverse(t: TreeNode):
    if t is None:
        return []
    elif t.left is None and t.right is None:
        return [t.data]
    else:
        return transverse(t.left)+[t.data]+transverse(t.right)
    
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.right= TreeNode(4)
# root.right.left = TreeNode(5)

root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(transverse(root))