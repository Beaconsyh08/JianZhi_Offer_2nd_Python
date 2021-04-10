def power_1(base: float, exponent: int) -> float:
    return base ** exponent


def power_2(base: float, exponent: int) -> float:
    invalid_input = False
    if base == 0 and exponent < 0:
        invalid_input = True
        return 0.0

    abs_exponent = abs(exponent)

    # res = power_of_unsigned_1(base, abs_exponent)
    res = power_of_unsigned_2(base, abs_exponent)

    if exponent < 0:
        res = 1.0 / res

    return res


def power_of_unsigned_1(base: float, abs_exponent: int) -> float:
    res = 1.0
    for i in range(1, abs_exponent + 1):
        res *= base
    return res


def power_of_unsigned_2(base: float, abs_exponent: int) -> float:
    if abs_exponent == 0:
        return 1
    elif abs_exponent == 1:
        return base
    else:
        res = power_of_unsigned_2(base, abs_exponent >> 1)
        res *= res

        if abs_exponent & 1 == 1:  # check if exponent is odd
            res *= base
    return res


if __name__ == '__main__':
    print(power_2(2, -3))
    # print(power_3(3, -3))
