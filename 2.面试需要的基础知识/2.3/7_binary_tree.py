class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def reconstruct_binary_tree(preorder: [int], inorder: [int]):
    if not preorder or not inorder:
        return None

    root = TreeNode(preorder[0])  # the root is the first node of the preorder traversal
    root_index_in = inorder.index(root.val)
    # the nodes before the root at inorder are the left subtree,
    # the node after the nodes are the right subtree

    root.left = reconstruct_binary_tree(preorder[1:root_index_in + 1], inorder[:root_index_in])
    root.right = reconstruct_binary_tree(preorder[root_index_in + 1:], inorder[root_index_in + 1:])

    return root


if __name__ == '__main__':
    pre_order = [1, 2, 4, 7, 3, 5, 6, 8]
    in_order = [4, 7, 2, 1, 5, 3, 8, 6]
    print(reconstruct_binary_tree(pre_order, in_order).left.val)
    print(reconstruct_binary_tree(pre_order, in_order).right.val)
