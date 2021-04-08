from collections import defaultdict


def sel_sort(lst):
    for i in range(len(lst)):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst


def ins_sort(lst):
    for i in range(1, len(lst)):
        the_val = lst[i]
        j = i - 1
        while j >= 0 and the_val < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = the_val
    return lst


def bubble_sort(lst):
    for i in range(len(lst) - 1):
        for j in range(len(lst) - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst


def merge_sort(lst):
    if len(lst) > 1:

        # Finding the mid of the lstay
        mid = len(lst) // 2

        # Dividing the lstay elements
        left_lst = lst[:mid]

        # into 2 halves
        right_lst = lst[mid:]

        # Sorting the first half
        merge_sort(left_lst)

        # Sorting the second half
        merge_sort(right_lst)

        i = j = k = 0

        # Copy data to temp lst left_lst[] and right_lst[]
        while i < len(left_lst) and j < len(right_lst):
            if left_lst[i] < right_lst[j]:
                lst[k] = left_lst[i]
                i += 1
            else:
                lst[k] = right_lst[j]
                j += 1
            k += 1

        # Checking if any element was left, the lst is not clear
        while i < len(left_lst):
            lst[k] = left_lst[i]
            i += 1
            k += 1

        while j < len(right_lst):
            lst[k] = right_lst[j]
            j += 1
            k += 1

    return lst


def count_sort(lst):
    dic = dict()
    for i in range(len(lst)):
        if lst[i] not in dic.keys():
            dic[lst[i]] = 1
        else:
            dic[lst[i]] += 1

    res = []
    for k, v in dic.items():
        res.extend([int(k)] * v)

    return res


def quick_sort(lst, low, high):
    if len(lst) == 1:
        return lst

    if low < high:
        s = partition(lst, low, high)
        quick_sort(lst, low, s - 1)
        quick_sort(lst, s + 1, high)

    return lst


def partition(lst, low, high):
    i = (low - 1)  # smaller index
    pivot = lst[high]

    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            if j != i:
                lst[i], lst[j] = lst[j], lst[i]
        print(lst)

    i += 1
    lst[i], lst[high] = lst[high], lst[i]
    print(lst)
    return i


if __name__ == '__main__':
    # lst_1 = [3, 6, 9, 3, 7, 4, 1, 0, 3, 3, 6, 10, 5]
    lst_2 = [3, 8, 4, 2, 7, 6]
    # print(sel_sort(lst_1))
    # print(ins_sort(lst_1))
    # print(bubble_sort(lst_1))
    # print(merge_sort(lst_1))
    # print(count_sort(lst_1))
    # print(quick_sort(lst_1, 0, len(lst_1) - 1))
    print(quick_sort(lst_2, 0, len(lst_2) - 1))
