# Given an array A of size N. Rearrange the given array so that A[i] becomes A[A[i]] with O(1) extra space.
#
# Constraints:
#
# 1 <= N <= 5×104
#
# 0 <= A[i] <= N - 1
#
# The elements of A are distinct
#
# Input Format
#
# The argument A is an array of integers
#
# Example 1:
#
# Input : [1, 0]
# Return : [0, 1]
# Example 2:
#
# Input : [0, 2, 1, 3]
# Return : [0, 1, 2, 3]

from typing import List


def solve(A: List[int]):
    n = len(A)

    for i in range(n):
        A[i] = n * A[i]
    print(A)

    for i in range(n):
        element = A[A[i] // n] // n
        A[i] += element
    print(A)

    for i in range(n):
        rem = A[i] % n
        A[i] = rem

    return A


if __name__ == "__main__":
    a = [0, 2, 1, 3]
    print(a)
    print(solve(a))
