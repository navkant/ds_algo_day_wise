# Problem Description
# Given an array of positive integers A, two integers appear only once, and all the other integers appear twice.
# Find the two integers that appear only once.
#
# Note: Return the two numbers in ascending order.
#
#
# Problem Constraints
# 2 <= |A| <= 100000
# 1 <= A[i] <= 109
#
#
#
# Input Format
# The first argument is an array of integers of size N.
#
#
#
# Output Format
# Return an array of two integers that appear only once.
#
#
#
# Example Input
# Input 1:
# A = [1, 2, 3, 1, 2, 4]
# Input 2:
#
# A = [1, 2]
#
#
# Example Output
# Output 1:
# [3, 4]
# Output 2:
#
# [1, 2]
#
#
# Example Explanation
# Explanation 1:
# 3 and 4 appear only once.
# Explanation 2:
#
# 1 and 2 appear only once.
from typing import List


def solve(A: List[int]) -> List[int]:
        xor_value = 0
        n = len(A)

        for i in range(n):
            xor_value = xor_value ^ A[i]

        for j in range(32):
            if xor_value >> j & 1:
                break

        a1 = []
        b1 = []

        for i in range(n):
            if A[i] >> j & 1:
                a1.append(A[i])
            else:
                b1.append(A[i])

        values1 = 0
        for i in range(len(a1)):
            values1 = values1 ^ a1[i]

        values2 = 0
        for i in range(len(b1)):
            values2 = values2 ^ b1[i]

        return sorted([values2, values1])


if __name__ == "__main__":
    a = [1, 2, 3, 1, 2, 4]
    print(solve(a))
