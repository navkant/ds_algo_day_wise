# Problem Description
# Find the Bth smallest element in given array A .
# NOTE: Users should try to solve it in less than equal to B swaps.

# Problem Constraints
# 1 <= |A| <= 100000
# 1 <= B <= min(|A|, 500)
# 1 <= A[i] <= 109

# Input Format
# The first argument is an integer array A.
# The second argument is integer B.

# Output Format
# Return the Bth smallest element in given array.

# Example Input
# Input 1:
# A = [2, 1, 4, 3, 2]
# B = 3

# Input 2:
# A = [1, 2]
# B = 2

# Example Output
# Output 1:
#  2
# Output 2:
#  2

# Example Explanation
# Explanation 1:
#  3rd element after sorting is 2.

# Explanation 2:
#  2nd element after sorting is 2.

from typing import List

def kth_smallest_element(A: List[int], B: int) -> int:
    for i in range(B):
        min_idx = i
        for j in range(i+1, len(A)):
            if A[j] < A[min_idx]:
                min_idx = j
            else:
                continue
        A[i], A[min_idx] = A[min_idx], A[i]
        print(A)

    # print(A)
    return A[B-1]


if __name__ == "__main__":
    A = [7, 6, 3, 4, 5, 1]
    B = 3
    print(kth_smallest_element(A, B))
