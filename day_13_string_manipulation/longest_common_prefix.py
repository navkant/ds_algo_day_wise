# Problem Description
# Given the array of strings A, you need to find the longest string S, which is the prefix of ALL the strings in
# the array.
# The longest common prefix for a pair of strings S1 and S2 is the longest string S which is the prefix of both S1
# and S2.

# Example: the longest common prefix of "abcdefgh" and "abcefgh" is "abc".

# Problem Constraints
# 0 <= sum of length of all strings <= 1000000

# Input Format
# The only argument given is an array of strings A.

# Output Format
# Return the longest common prefix of all strings in A.

# Example Input
# Input 1:
# A = ["abcdefgh", "aefghijk", "abcefgh"]

# Input 2:
# A = ["abab", "ab", "abcd"];

# Example Output
# Output 1:
# "a"

# Output 2:
# "ab"

# Example Explanation
# Explanation 1:
# Longest common prefix of all the strings is "a".

# Explanation 2:
# Longest common prefix of all the strings is "ab".
from typing import List


def longest_common_prefix(A: List[str]) -> str:
    if len(A) == 1:
        return A[0]

    first = A[0]
    common_substring = ''

    for i in range(1, len(A)):
        substring = ''
        for j in range(min(len(first), len(A[i]))):
            if first[j] == A[i][j]:
                substring += A[i][j]
            else:
                break

        if len(substring) < len(common_substring):
            common_substring = substring
        elif not common_substring and substring:
            common_substring = substring
        else:
            pass

    return common_substring




if __name__ == "__main__":
    a = ["abab", "ab", "abcd"]
    print(longest_common_prefix(a))

