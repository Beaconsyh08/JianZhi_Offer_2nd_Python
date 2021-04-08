class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left = None
        self.right = None


def next_node_inorder(parent_node):
    if not parent_node:
        return
    # 该节点有右子节点，那么该节点的下一个节点就是有自己节点的最左节点
    if parent_node.right is not None:
        parent_node = parent_node.right

        while parent_node.left is not None:
            parent_node = parent_node.left

        return parent_node

    # 该节点没有右子节点 该节点为父节点的左子节点
    elif parent_node.next is not None and parent_node.next.left == parent_node:
        return parent_node.next

    # 该节点为父节点的右子节点，它的下一个节点就是其父节点作为父节点的左子节点的下一个节点
    elif parent_node.next is not None and parent_node.next.right == parent_node:
        while parent_node.next is not None and parent_node.next.left != parent_node:
            parent_node = parent_node.next

        return parent_node.next

    else:
        # 节点无父节点，即节点为根节点
        return parent_node.next
