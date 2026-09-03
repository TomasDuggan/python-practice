# Lowest Common Ancestor (Binary Tree, no parent pointers)

Given the root of a binary tree and two nodes p and q that both exist
in the tree, find their lowest common ancestor (LCA). A node can be a
descendant of itself.

## Definition
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

## Signature
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

## Constraints
- Number of nodes: [2, 10^5]
- All node values are unique
- p != q, both guaranteed to exist in the tree

## Example
      3
     / \
    5   1
   / \ / \
  6  2 0  8
    / \
   7   4

lowest_common_ancestor(root, 5, 1) -> 3
lowest_common_ancestor(root, 5, 4) -> 5