# Problem Description
# You are given an integer array A of size N.
#
# You have to perform B operations. In one operation, you can remove either the leftmost or the rightmost element of the array A.
#
# Find and return the maximum possible sum of the B elements that were removed after the B operations.
#
# NOTE: Suppose B = 3, and array A contains 10 elements, then you can:
#
# Remove 3 elements from front and 0 elements from the back, OR
# Remove 2 elements from front and 1 element from the back, OR
# Remove 1 element from front and 2 elements from the back, OR
# Remove 0 elements from front and 3 elements from the back.
#
#
# Problem Constraints
# 1 <= N <= 105
#
# 1 <= B <= N
#
# -103 <= A[i] <= 103
#
#
#
# Input Format
# First argument is an integer array A.
#
# Second argument is an integer B.
#
#
#
# Output Format
# Return an integer denoting the maximum possible sum of elements you removed.
#
#
#
# Example Input
# Input 1:
#
#  A = [5, -2, 3 , 1, 2]
#  B = 3
# Input 2:
#
#  A = [ 2, 3, -1, 4, 2, 1 ]
#  B = 4
#
#
# Example Output
# Output 1:
#
#  8
# Output 2:
#
#  9
#
#
# Example Explanation
# Explanation 1:
#
#  Remove element 5 from front and element (1, 2) from back so we get 5 + 1 + 2 = 8
# Explanation 2:
#
#  Remove the first element and the last 3 elements. So we get 2 + 4 + 2 + 1 = 9

from typing import List


def main(A: List[int], B: int) -> int:
    n = len(A)
    suff = [0] * (n + 1)
    suff[n - 1] = A[n - 1]
    for i in range(n - 2, -1, -1):
        suff[i] = A[i] + suff[i + 1]
    print(suff)
    prefSum = 0
    ans = suff[n - B]
    print(ans)
    for i in range(B):
        prefSum = prefSum + A[i]
        suffSum = suff[n - B + i + 1]
        print(f"presum: {prefSum}, suffSum: {suffSum}")
        ans = max(ans, prefSum + suffSum)
    return ans


if __name__ == "__main__":
    a = [2, 3, -1, 4, 2, 1]
    print(a)
    b = 4
    print(main(a, b))
