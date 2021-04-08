def moving_count(threshold, rows, cols):
    if threshold < 0 or rows <= 0 or cols <= 0:
        return 0

    visited = [0] * (rows * cols)

    count = moving_count_core(threshold, rows, cols, 0, 0, visited)
    return count


def moving_count_core(threshold, rows, cols, row, col, visited):
    count = 0

    if check(threshold, rows, cols, row, col, visited):
        visited[row * cols + col] = 1

        count = 1 + moving_count_core(threshold, rows, cols, row - 1, col, visited) \
                  + moving_count_core(threshold, rows, cols, row + 1, col, visited) \
                  + moving_count_core(threshold, rows, cols, row, col - 1, visited) \
                  + moving_count_core(threshold, rows, cols, row, col + 1, visited)

    return count


def check(threshold, rows, cols, row, col, visited):
    row_col = get_digit_sum(row) + get_digit_sum(col)

    return 0 <= row < rows and 0 <= col < cols and row_col <= threshold and not visited[row * cols + col]


def get_digit_sum(num):
    res = 0
    while num > 0:
        res += num % 10
        num //= 10
    return res


if __name__ == '__main__':
    print(moving_count(9, 15, 15))
