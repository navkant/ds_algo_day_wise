# Problem Description
# Surprisingly, in an alien language, they also use English lowercase letters, but possibly in a different order.
# The order of the alphabet is some permutation of lowercase letters.
# Given an array of words A of size N written in the alien language, and the order of the alphabet denoted by string
# B of size 26, return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.

# Problem Constraints
# 1 <= N, length of each word <= 105
# Sum of the length of all words <= 2 * 106

# Input Format
# The first argument is a string array A of size N.
# The second argument is a string B of size 26, denoting the order.

# Output Format
# Return 1 if and only if the given words are sorted lexicographically in this alien language else, return 0.

# Example Input
# Input 1:
#  A = ["hello", "scaler", "interviewbit"]
#  B = "adhbcfegskjlponmirqtxwuvzy"

# Input 2:
#  A = ["fine", "none", "bush"]
#  B = "qwertyuiopasdfghjklzxcvbnm"

# Example Output
# Output 1:
#  1

# Output 2:
#  0

# Example Explanation
# Explanation 1:
#  The order shown in string B is: h < s < i (adhbcfegskjlponmirqtxwuvzy) for the given words.
#  So, Return 1.

# Explanation 2:
#  "none" should be present after "bush", Since b < n (qwertyuiopasdfghjklzxcvbnm).
#  So, Return 0.
from typing import List


def is_dictionary(A: List[str], B: str):
    for i in range(len(A) - 1):
        first_word = A[i]
        second_word = A[i + 1]
        j = 0

        while j < min(len(first_word), len(second_word)):
            if first_word[j] != second_word[j]:
                if B.index(first_word[j]) > B.index(second_word[j]):
                    return 0
                break
            j += 1

        if len(first_word) > len(second_word):
            return 0
    return 1


if __name__ == "__main__":
    A = ["hello", "scaler", "interviewbit"]
    B = "adhbcfegskjlponmirqtxwuvzy"

    print(is_dictionary(A, B))
