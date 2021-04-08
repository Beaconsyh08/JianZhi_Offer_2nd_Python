def rotated_lst_min(lst):
    index_1 = 0
    index_2 = len(lst) - 1
    # if the 1st element is the smallest (smaller than the index_2)
    # then the function should simply return it
    index_mid = index_1

    while lst[index_1] >= lst[index_2]:

        if index_2 - index_1 == 1:
            index_mid = index_2
            break

        index_mid = (index_1 + index_2) // 2

        # e.g. [1, 0, 1, 1, 1], we couldn't decide which is the smallest unless linear search
        if lst[index_1] == lst[index_2] == lst[index_mid]:
            return min(lst[index_1 + 1:index_2 + 1])

        if lst[index_mid] >= lst[index_1]:
            index_1 = index_mid
        elif lst[index_mid] <= lst[index_2]:
            index_2 = index_mid

    return lst[index_mid]


if __name__ == '__main__':
    lst0 = [3, 4, 1, 2, 3]
    lst1 = [3, 4, 5, 1, 2]
    lst2 = [1, 0, 1, 1, 1]
    print(rotated_lst_min(lst0))
    print(rotated_lst_min(lst1))
    print(rotated_lst_min(lst2))
