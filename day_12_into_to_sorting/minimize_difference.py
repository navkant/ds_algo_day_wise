# Problem Description
# Given an array of integers A of size, N. Minimize the absolute difference between the maximum and minimum element
# of the array.
# You can perform two types of operations at most B times in total to change the values in the array.
# Multiple operations can be performed on the same element.
# Increment : A[i] -> A[i] + 1.
# Decrement : A[i] -> A[i] - 1.
# Return the minimum difference possible.

# Problem Constraints
# 1 <= N <= 105
# 1 <= A[i] <= 106
# 1 <= B <= 109

# Input Format
# First argument is an integer array A.
# Second argument is an integer B which represents the maximum number of operations that can be performed.

# Output Format
# Return an integer denoting the minimum difference.

# Example Input
# Input 1:
#  A = [2, 6, 3, 9, 8]
#  B = 3

# Input 2:
#  A = [4, 6, 3, 1, 4]
#  B = 5

# Example Output
# Output 1:
#  5

# Output 2:
#  1

# Example Explanation
# Explanation 1:
#  We can apply the atmost 3 operations in the following sequence.
#  Initial array => [2, 6, 3, 9, 8].
#    Decrement 9 => [2, 6, 3, 8, 8].
#    Increment 2 => [3, 6, 3, 8, 8].
#    Increment 3 => [3, 6, 4, 8, 8].
#  Max = 8. Min = 3.
#  Therefore, abs|Max - Min| = |8 - 3| = 5.

# Explanation 2:
#  We can apply the atmost 5 operations in the following sequence.
#  Initial array => [4, 6, 3, 1, 4].
#    Increment 1 => [4, 6, 3, 2, 4].
#    Decrement 6 => [4, 5, 3, 2, 4].
#    Increment 2 => [4, 5, 3, 3, 4].
#    Decrement 5 => [4, 4, 3, 3, 4].
#    Increment 3 => [4, 4, 4, 3, 4].
#  Max = 4. Min = 3.
#  Therefore, abs|Max - Min| = |4 - 3| = 1.
from typing import List


def minimum_difference(A: List[int], B: int) -> int:
    maxx = 0
    k = B
    for i in A:
        maxx = max(i, maxx)
    freq_arr = [0] * (maxx+1)
    for i in A:
        freq_arr[i] += 1
    i = 0
    j = maxx
    while i < j:
        if freq_arr[i] > freq_arr[j]:
            if freq_arr[j] <= k:
                freq_arr[j-1] = freq_arr[j-1] + freq_arr[j]
                k = k - freq_arr[j]
                j = j - 1
            else:
                break
        else:
            if freq_arr[i] <= k:
                freq_arr[i+1] = freq_arr[i+1] + freq_arr[i]
                k = k - freq_arr[i]
                i = i + 1
            else:
                break
    return j - i


if __name__ == "__main__":
    A = [2, 6, 3, 9, 8]
    B = 3
    print(minimum_difference(A, B))
