# Given an array of integers A consisting of only 0 and 1.
#
# Find the maximum length of a contiguous subarray with equal number of 0 and 1.
#
#
#
# Input Format
#
# The only argument given is the integer array A.
# Output Format
#
# Return the maximum length of a contiguous subarray with equal number of 0 and 1.
# Constraints
#
# 1 <= length of the array <= 100000
# 0 <= A[i] <= 1
# For Example
#
# Input 1:
#     A = [1, 0, 1, 0, 1]
# Output 1:
#     4
#     Explanation 1:
#         Subarray from index 0 to index 3 : [1, 0, 1, 0]
#         Subarray from index 1 to index 4 : [0, 1, 0, 1]
#         Both the subarrays have equal number of ones and equal number of zeroes.
#
# Input 2:
#     A = [1, 1, 1, 0]
# Output 2:
#     2
from typing import List


def contiguous_array(A: List[int]) -> int:
    for index, num in enumerate(A):
        if A[index] == 0:
            A[index] = -1

    for i in range(1, len(A)):
        curr_sum = A[i] + A[i - 1]
        A[i] = curr_sum

    ans = 0
    hash_map = dict()

    for index, num in enumerate(A):
        if num == 0:
            ans = max(ans, index + 1)
        if num not in hash_map:
            hash_map[num] = index
        else:
            prev_index = hash_map[num]
            ans = max(ans, index - prev_index)

    return ans

if __name__ == "__main__":
    A = [0,0,0,1,1,1,0,0,1,0,1,1,0,1,1,0,1,1,1,0,0,1,1,0,0,0,0,1,1,1,1,1,0,0,1,0,0,0,0,1,0,0,1,0,0,1,0,1,1,0,0,1,0,1,1,
         1,0,0,0,0,1,0,0,1,1,1]

    print(contiguous_array(A))