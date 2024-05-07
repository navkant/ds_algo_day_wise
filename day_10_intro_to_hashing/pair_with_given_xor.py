# Problem Description
# Given an integer array A containing N distinct integers.
# Find the number of unique pairs of integers in the array whose XOR is equal to B.
#
# NOTE:
# Pair (a, b) and (b, a) is considered to be the same and should be counted once.
#
# Problem Constraints
# 1 <= N <= 105
# 1 <= A[i], B <= 107
#
# Input Format
# The first argument is an integer array A.
# The second argument is an integer B.
#
# Output Format
# Return a single integer denoting the number of unique pairs of integers in the array A whose XOR is equal to B.
#
# Example Input

# Input 1:
#  A = [5, 4, 10, 15, 7, 6]
#  B = 5

# Input 2:
#  A = [3, 6, 8, 10, 15, 50]
#  B = 5

from typing import List


def pair_with_given_xor(A: List[int], B: int):
    map_dict = {}
    count = 0

    for i in A:
        if B ^ i not in map_dict:
            map_dict[i] = 1
        else:
            count += 1

    return count


if __name__ == "__main__":
    A = [3, 6, 8, 10, 15, 50]
    B = 5

    print(pair_with_given_xor(A, B))