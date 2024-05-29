import unittest
from src.binary_tree import TreeNode, transverse

class TestTreeNode(unittest.TestCase):

    def test_transverse_empty_tree(self):
        self.assertEqual(transverse(None), [])

    def test_transverse_single_node(self):
        root = TreeNode(1)
        self.assertEqual(transverse(root), [1])

    def test_transverse_left_heavy_tree(self):
        root = TreeNode(3)
        root.left = TreeNode(2)
        root.left.left = TreeNode(1)
        self.assertEqual(transverse(root), [1, 2, 3])

    def test_transverse_right_heavy_tree(self):
        root = TreeNode(1)
        root.right = TreeNode(2)
        root.right.right = TreeNode(3)
        self.assertEqual(transverse(root), [1, 2, 3])

    def test_transverse_full_tree(self):
        root = TreeNode(4)
        root.left = TreeNode(2)
        root.right = TreeNode(5)
        root.left.left = TreeNode(1)
        root.left.right = TreeNode(3)
        self.assertEqual(transverse(root), [1, 2, 3, 4, 5])

    def test_transverse_balanced_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.left.left = TreeNode(4)
        root.left.right = TreeNode(5)
        root.right.left = TreeNode(6)
        root.right.right = TreeNode(7)
        self.assertEqual(transverse(root), [4, 2, 5, 1, 6, 3, 7])

if __name__ == '__main__':
    unittest.main()