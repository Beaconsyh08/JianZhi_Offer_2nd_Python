def fib(n):
    fib_res = [0, 1]
    print(type(fib_res))
    while len(fib_res) <= n:
        fib_res.append(fib_res[-2] + fib_res[-1])
    return fib_res[n]


if __name__ == '__main__':
    print(fib(2))
