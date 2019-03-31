def set_zero(matrix):
    N = len(matrix)
    if N == 0:
        return

    M = len(matrix[0])
    if M == 0:
        return

    r_has_zero = False
    c_has_zero = False

    for i in range(N):
        if matrix[i][0] == 0:
            c_has_zero = True
            break
    
    for j in range(M):
        if matrix[0][j] == 0:
            r_has_zero = True
            break

    for i in range(1, N):
        for j in range(1, M):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    for i in range(1, N):
        if matrix[i][0] == 0:
            for j in range(0, M):
                matrix[i][j] = 0
    
    for j in range(1, M):
        if matrix[0][j] == 0:
            for i in range(0, N):
                matrix[i][j] = 0

    if c_has_zero:
        for i in range(0, N):
            matrix[i][0] = 0

    if r_has_zero:
        for j in range(0, M):
            matrix[0][j] = 0


if __name__ == '__main__':
    in_matrix = [[ 7, 10, 122, 15], 
                 [73, 8,   9,   1],
                 [ 8, 2,  77, 100],
                 [ 0, 9,   0,  11],
                 [ 0, 7,   6,   5]]

    out_matrix = [[ 0, 10, 0, 15], 
                  [ 0,  8, 0,  1],
                  [ 0,  2, 0,100],
                  [ 0,  0, 0,  0],
                  [ 0,  0, 0,  0]]

    set_zero(in_matrix)

    print('in_matrix == out_matrix:', in_matrix == out_matrix)