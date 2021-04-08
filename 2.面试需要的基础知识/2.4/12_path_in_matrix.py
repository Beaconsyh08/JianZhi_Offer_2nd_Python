def has_path(matrix, rows, cols, path):
    if not matrix and rows <= 0 and cols <= 0 and path is None:
        return False
    # 模拟的字符矩阵
    visited = [0] * (rows * cols)
    print(visited)
    path_len = 0
    # 从第一个开始递归，当然第一二个字符可能并不位于字符串之上，所以有这样一个双层循环找起点用的，一旦找到第一个符合的字符串，就开始进入递归，
    # 返回的第一个return Ture就直接跳出循环了。
    for row in range(rows):
        for col in range(cols):
            if has_path_core(matrix, rows, cols, row, col, path, path_len, visited):
                return True
    return False


def has_path_core(matrix, rows, cols, row, col, path, path_len, visited):
    # 说明已经找到该路径，可以返回True
    if len(path) == path_len:
        return True

    has_path_tf = False
    if 0 <= row < rows and 0 <= col < cols and matrix[row * cols + col] == path[path_len] and not \
            visited[row * cols + col]:

        path_len += 1
        visited[row * cols + col] = True
        # 进行该值上下左右的递归
        has_path_tf = has_path_core(matrix, rows, cols, row - 1, col, path, path_len, visited) \
                      or has_path_core(matrix, rows, cols, row, col - 1, path, path_len, visited) \
                      or has_path_core(matrix, rows, cols, row + 1, col, path, path_len, visited) \
                      or has_path_core(matrix, rows, cols, row, col + 1, path, path_len, visited)

        # 对标记矩阵进行布尔值标记
        if not has_path_tf:
            path_len -= 1
            visited[row * cols + col] = False

    return has_path_tf


if __name__ == '__main__':
    mat = ["a", "b", "t", "g", "c", "f", "c", "s", "j", "d", "e", "h"]
    mat_2 = ["a", "c", "j", "b", "f", "d", "t", "c", "e", "g", "s", "h"]
    c = 4
    r = 3
    p = "bfce"

    print(has_path(mat_2, c, r, p))
