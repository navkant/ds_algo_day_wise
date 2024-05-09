# Problem Description
# Given an array of integers A, find and return whether the given array contains a non-empty subarray with a sum equal to 0.
#
# If the given array contains a sub-array with sum zero return 1, else return 0.
#
#
#
# Problem Constraints
# 1 <= |A| <= 100000
#
# -10^9 <= A[i] <= 10^9
#
#
#
# Input Format
# The only argument given is the integer array A.
#
#
#
# Output Format
# Return whether the given array contains a subarray with a sum equal to 0.
#
#
#
# Example Input
# Input 1:
#
#  A = [1, 2, 3, 4, 5]
# Input 2:
#
#  A = [4, -1, 1]
#
#
# Example Output
# Output 1:
#
#  0
# Output 2:
#
#  1
#
#
# Example Explanation
# Explanation 1:
#
#  No subarray has sum 0.
# Explanation 2:
#
#  The subarray [-1, 1] has sum 0.
from typing import List


def sub_array_with_zero_sum(A: List[int]) -> int:
    for i in range(1, len(A)):
        A[i] += A[i-1]

    sum_dict = {}

    for index, num in enumerate(A):
        if num != 0 and num not in sum_dict:
            sum_dict[num] = i
        else:
            return 1

    return 0


if __name__ == "__main__":
    A = [4, -1, 0, 1]
    print(sub_array_with_zero_sum(A))
