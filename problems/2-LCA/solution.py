class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def is_leaf(self) -> bool:
        return self.left == None and self.right == None


def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    if root is p or root is q: # base case
        return root

    if root.is_leaf(): # guard case
        return None

    left = lowest_common_ancestor(root.left, p, q)
    right = lowest_common_ancestor(root.right, p, q)
    
    if left is not None and right is None:
        return left

    if right is not None and left is None:
        return right

    if right is not None and left is not None:
        return root