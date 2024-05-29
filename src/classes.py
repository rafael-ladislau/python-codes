class TreeNode:

    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

print(root.left.data)

