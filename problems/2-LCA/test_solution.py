from solution import TreeNode, lowest_common_ancestor

"""
Example tree
        3 
     5        1
   6   2     0 8
      7 4
"""
def build_example_tree() -> TreeNode:
    n6 = TreeNode(6)
    n7 = TreeNode(7)
    n4 = TreeNode(4)
    n0 = TreeNode(0)
    n8 = TreeNode(8)

    n2 = TreeNode(2, n7, n4)
    n5 = TreeNode(5, n6, n2)
    n1 = TreeNode(1, n0, n8)

    root = TreeNode(3, n5, n1)
    return root, n5, n1, n4

"""
lowest_common_ancestor(root, 5, 1) -> 3
lowest_common_ancestor(root, 5, 4) -> 5
"""
def test():
    root, n5, n1, n4 = build_example_tree()
    test_1 = lowest_common_ancestor(root, n5, n1).val
    assert test_1 == 3, f"res:{test_1}, but should be 3"

    test_2 = lowest_common_ancestor(root, n5, n4).val
    assert test_2 == 5, f"res:{test_2}, but should be 5"

    print("Good job")

if __name__ == "__main__":
    test()