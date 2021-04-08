def cut_dp(length):
    prod = [0, 1, 2, 3] + [0] * (length - 3)

    if length < 2:
        return 0
    elif length == 2 or length == 3:
        return prod[length - 1]

    for i in range(4, length + 1):
        res = 0

        # no need to calculate the duplicated situation, use total to minus
        for j in range(1, length // 2):

            pro = prod[j] * prod[i - j]

            if res < pro:
                res = pro
            prod[i] = res

    res = prod[length]

    return res


def cut_greedy(length):
    if length < 2:
        return 0
    elif length == 2:
        return 1
    elif length == 3:
        return 2

    # cut 3 as many as possible
    times_of_3 = length // 3

    # when 4 left, 2 * 2 > 3 * 1
    if length - 3 * times_of_3 == 1:
        times_of_3 -= 1

    times_of_2 = (length - 3 * times_of_3) // 2

    return (3 ** times_of_3) * (2 ** times_of_2)


if __name__ == '__main__':
    print(cut_dp(150))
    print(cut_greedy(150))
