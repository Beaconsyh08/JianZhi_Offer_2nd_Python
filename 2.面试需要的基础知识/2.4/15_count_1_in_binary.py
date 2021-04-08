def count_1_in_binary(num):
    count = 0
    while num:
        count += 1
        num = (num - 1) & num

    return count


if __name__ == '__main__':
    print(count_1_in_binary(10))
