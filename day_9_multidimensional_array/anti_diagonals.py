from typing import List


def anti_diagonals(A: List[List[int]]) -> List[List[int]]:
    result_array = []

    i = 0
    while i < len(A):
        k = i
        j = 0
        row = []
        while k >= 0 and j <= len(A):
            row.append(A[k][j])
            j += 1
            k -=1
        i += 1
        result_array.append(row)

    return result_array


if __name__ == "__main__":
    A = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for row in anti_diagonals(A):
        print(row)
