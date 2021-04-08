def matrix_search(mat: [list], target: int) -> bool:
    rows = len(mat)
    cols = len(mat[0])
    row = 0
    while row <= rows and cols > 0:

        top_right = mat[row][cols - 1]

        if top_right == target:
            return True
        elif top_right > target:
            cols -= 1
        else:  # top_right < target
            row += 1

    return False


if __name__ == '__main__':
    print(matrix_search([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 7))
    print(matrix_search([[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]], 5))
