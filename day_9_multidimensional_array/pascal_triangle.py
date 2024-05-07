from typing import List

def pascal_triangle(A: int) -> List[List[int]]:
    array = [[0 for i in range(A)] for j in range(A)]
    array[0][0] = 1

    for i in range(1, A):
        for j in range(A):
            if j == 0:
                array[i][j] = 1
            else:
                array[i][j] = array[i-1][j] + array[i-1][j-1]
    return array


if __name__ == "__main__":
    A = 4
    for row in pascal_triangle(A):
        print(row)
