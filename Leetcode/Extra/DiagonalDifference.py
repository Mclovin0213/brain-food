testArray = [[11, 2, 4],
             [4, 5, 6],
             [10, 8, -12]]


def diagonalDifference(arr):
    left_d = 0
    right_d = 0
    num_len = len(arr) - 1

    for i in range(len(arr)):
        for j in range(len(arr)):
            if i == j:
                left_d += arr[i][j]
            if j == num_len:
                right_d += arr[i][j]
                num_len -= 1

    return abs(left_d - right_d)

print(diagonalDifference(testArray))

