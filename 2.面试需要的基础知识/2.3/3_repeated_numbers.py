def repeated_number_1(lst: list) -> int:
    lst.sort()
    for i in range(len(lst)):
        # if adjacent numbers are equal after sorting, then repeated number appears
        if lst[i] == lst[i + 1]:
            return lst[i]


def repeated_number_2(lst: list) -> int:
    all_number = set()
    for i in range(len(lst)):
        if lst[i] in all_number:  # the set already has the number
            return lst[i]
        else:
            all_number.add(lst[i])


def repeated_number_3(lst: list) -> int:
    # length == n and range in [0, n - 1], which means must repeated, then if every element sit in
    # the same index as their index, if there is a conflict, then repeated
    for i in range(len(lst)):
        cur_num = lst[i]
        if cur_num != i:
            if cur_num == lst[cur_num]:
                return cur_num
            else:
                lst[i], lst[cur_num] = lst[cur_num], cur_num


def repeated_number_4(lst: list) -> int:
    # same as method 3, but use some assistant from extra space, not modify the original one
    lst_new = [-1] * len(lst)
    for i in range(len(lst)):
        if lst_new[lst[i]] == lst[i]:
            return lst[i]
        else:
            lst_new[lst[i]] = lst[i]


if __name__ == '__main__':
    # print(repeated_number_1([2, 3, 1, 0, 2, 5, 3]))
    # print(repeated_number_2([2, 3, 1, 0, 2, 5, 3]))
    # print(repeated_number_3([2, 3, 1, 0, 2, 5, 3]))
    print(repeated_number_4([2, 3, 1, 0, 2, 5, 3]))
