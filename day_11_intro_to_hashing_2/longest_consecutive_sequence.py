# Problem Description
# Given an unsorted integer array A of size N.
# Find the length of the longest set of consecutive elements from array A.

# Problem Constraints
# 1 <= N <= 106
# -106 <= A[i] <= 106

# Input Format
# First argument is an integer array A of size N.

# Output Format
# Return an integer denoting the length of the longest set of consecutive elements from the array A.

# Example Input
# Input 1:
# A = [100, 4, 200, 1, 3, 2]

# Input 2:
# A = [2, 1]

# Example Output
# Output 1:
#  4

# Output 2:
#  2

# Example Explanation
# Explanation 1:
#  The set of consecutive elements will be [1, 2, 3, 4].

# Explanation 2:
#  The set of consecutive elements will be [1, 2].
from typing import List


def longest_consecutive_sequence(A: List[int]) -> int:
    hash_map = dict()

    for i in A:
        if i not in hash_map:
            hash_map[i] = 1
    ans = 0

    for index, num in enumerate(A):
        if num - 1 in hash_map:
            # this helps in reducing time complexity 
            # as we will start inner loop from smallest element only
            continue
        else:
            count = 1
            j = num
            while True:
                if j+1 in hash_map:
                    count += 1
                    j += 1
                else:
                    break

            ans = max(ans, count)

    return ans


if __name__ == "__main__":
    A = [2, 1]
    print(longest_consecutive_sequence(A))


