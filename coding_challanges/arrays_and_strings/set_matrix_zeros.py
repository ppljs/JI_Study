def setZeroes(matrix):
    if not matrix or not isinstance(matrix[0], list) or not matrix[0]:
        return

    zero_on_first_line = zero_on_first_column = False
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                project_zero_on_sides(i, j, matrix)
                zero_on_first_line |= i == 0
                zero_on_first_column |= j == 0

    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[0])):
            if should_put_zero(i, j, matrix):
                matrix[i][j] = 0

    if zero_on_first_line:
        for j in range(len(matrix[0])):
            matrix[0][j] = 0

    if zero_on_first_column:
        for i in range(len(matrix)):
            matrix[i][0] = 0


def should_put_zero(i, j, matrix):
    return matrix[i][0] == 0 or matrix[0][j] == 0

def project_zero_on_sides(i, j, matrix):
    matrix[i][0] = 0
    matrix[0][j] = 0
