# Problem Description
# Given an integer A, generate a square matrix filled with elements from 1 to A2 in spiral order and return the generated square matrix.

# Problem Constraints
# 1 <= A <= 1000

# Input Format
# First and only argument is integer A

# Output Format
# Return a 2-D matrix which consists of the elements added in spiral order.

# Example Input
# Input 1:
# 1

# Input 2:
# 2

# Input 3:
# 5

# Example Output
# Output 1:
# [ [1] ]

# Output 2:
# [ [1, 2], 
#   [4, 3] ]

# Output 3:
# [ [1,   2,  3,  4, 5], 
#   [16, 17, 18, 19, 6], 
#   [15, 24, 25, 20, 7], 
#   [14, 23, 22, 21, 8], 
#   [13, 12, 11, 10, 9] ]
from typing import List


def spiral_matrix(A: int) -> List[List[int]]:
    matrix = [[0 for i in range(A)] for j in range(A)]

    left = 0
    right = A
    top = 0
    bottom = A
    count = 1

    while (left < right) and (top < bottom):
        for i in range(left, right):
            matrix[top][i] = count
            count += 1
        top += 1

        for i in range(top, bottom):
            matrix[i][right-1] = count
            count += 1
        right -= 1

        for i in range(right-1, left-1, -1):
            matrix[bottom-1][i] = count
            count += 1
        bottom -= 1

        for i in range(bottom-1, top-1, -1):
            matrix[i][left] = count
            count += 1
        left += 1

    return matrix


if __name__ == "__main__":
    A = 4
    for row in spiral_matrix(A):
        print(row)
