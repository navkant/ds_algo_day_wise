# Problem Description
# You are given a n x n 2D matrix A representing an image.
#
# Rotate the image by 90 degrees (clockwise).
#
# You need to do this in place.
#
# Note: If you end up using an additional array, you will only receive partial score.
#
#
#
# Problem Constraints
# 1 <= n <= 1000
#
#
#
# Input Format
# First argument is a 2D matrix A of integers
#
#
#
# Output Format
# Return the 2D rotated matrix.
#
#
#
# Example Input
# Input 1:
#
#  [
#     [1, 2],
#     [3, 4]
#  ]
# Input 2:
#
#  [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
#  ]

# Example Output
# Output 1:
#
#  [
#     [3, 1],
#     [4, 2]
#  ]
# Output 2:
#
#  [
#     [7, 4, 1],
#     [8, 5, 2],
#     [9, 6, 3]
#  ]
#
#
# Example Explanation
# Explanation 1:
#
#  After rotating the matrix by 90 degree:
#  1 goes to 2, 2 goes to 4
#  4 goes to 3, 3 goes to 1
# Explanation 2:
#
#  After rotating the matrix by 90 degree:
#  1 goes to 3, 3 goes to 9
#  2 goes to 6, 6 goes to 8
#  9 goes to 7, 7 goes to 1
#  8 goes to 4, 4 goes to 2
#
#
#
# Expected Output
# Enter your input as per the following guideline:
# There are 1 lines in the input
#
# Line 1 ( Corresponds to arg 1 ) : 2 D array. First 2 integers R, C are the number of rows and columns. Then R * C integers follow corresponding to the rowwise numbers in the 2D array

from typing import  List


def reverse_array(arr: List[int]):
    mid = len(arr)//2

    for i in range(mid):
        last_index = len(arr) - i - 1
        arr[i], arr[last_index] = arr[last_index], arr[i]
    return arr

def rotate_matrix(A: List[List[int]]):
    for i in range(len(A)):
        for j in range(i, len(A)):
            if i == j:
                continue
            else:
                A[i][j], A[j][i] = A[j][i], A[i][j]

    for i in range(len(A)):
        A[i] = reverse_array(A[i])

    return A


if __name__ == "__main__":
    A = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print("before rotation")
    for row in A:
        print(row)
    print()
    for row in rotate_matrix(A):
        print(row)