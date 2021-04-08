import helper.linked_list as ll


def reverse_print_linked_list(lst: ll.LinkedList):
    stack = []  # use stack, first in last out

    for node in lst:
        stack.append(node.data)

    while len(stack) > 0:
        print(stack.pop())


if __name__ == '__main__':
    reverse_print_linked_list(ll.LinkedList(["a", "b", "c", "d"]))
