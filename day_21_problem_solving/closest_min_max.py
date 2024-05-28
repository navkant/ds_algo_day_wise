# Problem Description
# Given an array A, find the size of the smallest subarray such that it contains at least one occurrence of the maximum value of the array
#
# and at least one occurrence of the minimum value of the array.
#
#
#
# Problem Constraints
# 1 <= |A| <= 2000
#
#
#
# Input Format
# First and only argument is vector A
#
#
#
# Output Format
# Return the length of the smallest subarray which has at least one occurrence of minimum and maximum element of the array
#
#
#
# Example Input
# Input 1:
#
# A = [1, 3, 2]
# Input 2:
#
# A = [2, 6, 1, 6, 9]
#
#
# Example Output
# Output 1:
#
#  2
# Output 2:
#
#  3
#
#
# Example Explanation
# Explanation 1:
#
#  Take the 1st and 2nd elements as they are the minimum and maximum elements respectievly.
# Explanation 2:
#
#  Take the last 3 elements of the array.

from typing import List


def solve(A: List[int]) -> int:
    minn = min(A)
    maxx = max(A)
    inf = 10000000000
    last_min = -inf
    last_max = inf
    result = inf
    c = 0

    for i in A:
        if i == minn:
            last_min = c

        if i == maxx:
            last_max = c

        p = abs(last_max - last_min) + 1

        if result > p:
            result = p

        c += 1

    return result


if __name__ == "__main__":
    a = [2, 6, 1, 6, 9]
    print(solve(a))
