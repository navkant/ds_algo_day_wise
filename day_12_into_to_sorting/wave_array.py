# Problem Description
# Given an array of integers A, sort the array into a wave-like array and return it.
# In other words, arrange the elements into a sequence such that
# a1 >= a2 <= a3 >= a4 <= a5.....
# NOTE: If multiple answers are possible, return the lexicographically smallest one.

# Problem Constraints
# 1 <= len(A) <= 106
# 0 <= A[i] <= 106

# Input Format
# The first argument is an integer array A.

# Output Format
# Return an array arranged in the sequence as described.

# Example Input
# Input 1:
# A = [1, 2, 3, 4]

# Input 2:
# A = [1, 2]

# Example Output
# Output 1:
# [2, 1, 4, 3]

# Output 2:
# [2, 1]

# Example Explanation
# Explanation 1:
# One possible answer : [2, 1, 4, 3]
# Another possible answer : [4, 1, 3, 2]
# First answer is lexicographically smallest. So, return [2, 1, 4, 3].

# Explanation 1:
# Only possible answer is [2, 1].
from typing import List


def wave_array(A: List[int]) -> List[int]:
    if len(A) == 1:
        return A

    A = sorted(A)
    result = []
    i = 1

    while i < len(A):
        result.extend([A[i], A[i-1]])

        if len(A) % 2 != 0 and i == len(A)-2:
            result.append(A[i+1])

        i += 2

    return result

if __name__ == "__main__":
    A = [6, 17, 15, 13]
    print(wave_array(A))
