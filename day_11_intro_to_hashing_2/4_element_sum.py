# Given an array A of N integers, find the index of values that satisfy P + Q = R + S, where P, Q, R & S are integers values in the array
#
# Expected time complexity O(N2)
#
# NOTE:
#
# 1) Return the indices `A1 B1 C1 D1`, so that
#   A[A1] + A[B1] = A[C1] + A[D1]
#   A1 < B1, C1 < D1
#   A1 < C1, B1 != D1, B1 != C1
#
# 2) If there are more than one solutions,
#    then return the tuple of values which are lexicographical smallest.
#
# Assume we have two solutions
# S1 : A1 B1 C1 D1 ( these are values of indices in the array )
# S2 : A2 B2 C2 D2
#
# S1 is lexicographically smaller than S2 if:
#   A1 < A2 OR
#   A1 = A2 AND B1 < B2 OR
#   A1 = A2 AND B1 = B2 AND C1 < C2 OR
#   A1 = A2 AND B1 = B2 AND C1 = C2 AND D1 < D2
# If no solution is possible, return an empty list.
#
#
#
# Problem Constraints
# 1 <= N <= 1000
#
# 0 <= A[i] <= 1000
#
#
#
# Input Format
# First and only argument is an integer array A of length N.
#
#
#
# Output Format
# Return an array of size four which contains indices of values P, Q, R, and S.
#
#
#
# Example Input
# Input 1:
#  A = [3, 4, 7, 1, 2, 9, 8]

# Input 2:
#  A = [2, 5, 1, 6]

# Example Output
# Output 1:
#  [0, 2, 3, 5]

# Output 2:
#  [0, 1, 2, 3]

# Example Explanation
# Explanation 1:
#  A[0] + A[2] = A[3] + A[5]

#  Note: indexes returned should be 0-based.
# Explanation 2:
#  A[0] + A[1] = A[2] + A[3]
from typing import List


def four_element_sum(A: List[int]) -> List[int]:
    n = len(A)
    hash_map = dict()
    result = []

    for i in range(n):
        for j in range(i+1, n):
            temp = A[i] + A[j]
            if temp not in hash_map:
                hash_map[temp] = [i, j]
            else:
                if i not in hash_map[temp] and j not in hash_map[temp] and len(hash_map[temp]) <= 2:
                    hash_map[temp].extend([i, j])
                else:
                    pass

                if len(hash_map[temp]) == 4:
                    if not result:
                        result = hash_map[temp]
                    else:
                        temp_result = hash_map[temp]
                        for k in range(4):
                            if temp_result[k] < result[k]:
                                result = temp_result
                            elif temp_result[k] > result[k]:
                                break
                            else:
                                continue
                else:
                    continue

    return result



if __name__ == "__main__":
    A = [3, 4, 7, 1, 2, 9, 8]
    print(four_element_sum(A))
