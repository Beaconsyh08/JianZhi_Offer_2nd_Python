import helper.linked_list as ll


class ListNode:
    def __init__(self, val: int):
        self.val = val
        self.next = None


def remove_node(head_node: ListNode, tb_removed_node: ListNode):
    if not head_node or not tb_removed_node:
        return

    # not the tail, copy the value and cover the one to be removed
    if tb_removed_node.next is not None:
        next_node = tb_removed_node.next
        tb_removed_node.val = next_node.val
        tb_removed_node.next = next_node.next

        del next_node
        next_node = None

    # there is only one node in the list, which is the head node, delete it
    elif head_node == tb_removed_node:
        del tb_removed_node
        tb_removed_node = None
        head_node = None

    # to be removed one is the tail one, then need to remove the last one
    else:
        temp_node = head_node
        while temp_node.next is not tb_removed_node:
            temp_node = temp_node.next
        temp_node.next = None
        del tb_removed_node
        tb_removed_node = None
        

