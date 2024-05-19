# Problem Description
# Given a collection of integers denoted by array A of size N that might contain duplicates, return all
# possible subsets.

# NOTE:
# Elements in a subset must be in non-descending order.
# The solution set must not contain duplicate subsets.
# The subsets must be sorted lexicographically.

# Problem Constraints
# 0 <= N <= 16

# Input Format
# Only argument is an integer array A of size N.

# Output Format
# Return a 2-D vector denoting all the possible subsets.

# Example Input
# Input 1:
#  A = [1, 2, 2]

# Input 2:
#  A = [1, 1]

# Example Output
# Output 1:
#  [
#     [],
#     [1],
#     [1, 2],
#     [1, 2, 2],
#     [2],
#     [2, 2]
#  ]

# Output 2:
#  [
#     [],
#     [1],
#     [1, 1]
#  ]

# Example Explanation
# Explanation 1:
# All the subsets of the array [1, 2, 2] in lexicographically sorted order.

from typing import List

class ArraySubsets:

    def get_subsets(self, array: List[int], start: int, output: List[int], ans: List[int]) -> None:
        if output not in ans:
            ans.append(output)

        if start == len(array):
            return

        output_2 = output.copy()
        output_2.append(array[start])

        self.get_subsets(array, start+1, output, ans)
        self.get_subsets(array, start+1, output_2, ans)

    def solve(self, A: List[int]):
        start = 0
        output = []
        ans = []

        A.sort()
        self.get_subsets(A, start, output, ans)

        return ans


if __name__ == "__main__":
    a = [2,3,10,7,6,5,4,8,9,7,1,3,4,7,10,8]
    solution = ArraySubsets()
    print(solution.solve(a))
