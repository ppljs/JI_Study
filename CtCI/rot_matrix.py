def new_pos(i, j, N):
    return N - 1 - j, i


def rot_matrix(matrix):
    N = len(matrix)

    print((N//2) - 1)
    for j in range(N // 2):
        for i in range(j, N - j - 1, 1):
            i_1, j_1 = new_pos(i, j, N)
            i_2, j_2 = new_pos(i_1, j_1, N)
            i_3, j_3 = new_pos(i_2, j_2, N)

            temp1 = matrix[i_1][j_1]
            matrix[i_1][j_1] = matrix[i][j]

            temp2 = matrix[i_2][j_2]
            matrix[i_2][j_2] = temp1

            temp1 = temp2
            temp2 = matrix[i_3][j_3]
            matrix[i_3][j_3] = temp1

            matrix[i][j] = temp2


if __name__ == '__main__':
    matrix = [[1,2,3], [4,5,6], [7,8,9]]
    rot_matrix(matrix)
    for row in matrix:
        print(row)

