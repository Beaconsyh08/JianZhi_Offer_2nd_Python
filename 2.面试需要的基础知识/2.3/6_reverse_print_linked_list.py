import JianZhi.linked_list as ll


def reverse_print(lst: ll.LinkedList):
    stack = []
    print(lst)
    for node in lst:
        stack.append(node.data)

    while len(stack) > 0:
        print(stack.pop())


if __name__ == '__main__':
    reverse_print(ll.LinkedList(["a", "b", "c", "d"]))
