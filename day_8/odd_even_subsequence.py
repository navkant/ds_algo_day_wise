# Given an array of integers A of size, N. Find the longest subsequence of A, which is odd-even.

# A subsequence is said to be odd-even in the following cases:

#   1. The first element of the subsequence is odd; the second element is even, the third element is odd, and so on. For example: [5, 10, 5, 2, 1, 4], [1, 2, 3, 4, 5]

#   2. The first element of the subsequence is even, the second element is odd, the third element is even, and so on. For example: [10, 5, 2, 1, 4, 7], [10, 1, 2, 3, 4]

# Return the maximum possible length of odd-even subsequence.

# Note: An array B is a subsequence of an array A if B can be obtained from A by deleting several (possibly, zero, or all) elements.


# Input Format

# The only argument given is the integer array A.
# Output Format

# Return the maximum possible length of odd-even subsequence.
# Constraints

# 1 <= N <= 100000
# 1 <= A[i] <= 10^9 
# For Example

# Input 1:
#     A = [1, 2, 2, 5, 6]
# Output 1:
#     4
#     Explanation 1:
#         Maximum length odd even subsequence is [1, 2, 5, 6]

# Input 2:
#     A = [2, 2, 2, 2, 2, 2]
# Output 2:
#     1
#     Explanation 2:
#         Maximum length odd even subsequence is [2]
from typing import List

def odd_even_subsequence(A: List[int]) -> int:
    state = -1
    count = 0

    for i,v in enumerate(A):
        if v % 2 != state:
            count += 1
            state = v % 2
        else:
            pass

    return count


if __name__ == "__main__":
    a = [1, 2, 2, 5, 6]
    print(odd_even_subsequence(a))
