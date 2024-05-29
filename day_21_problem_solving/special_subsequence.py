# Problem Description
# You have given a string A having Uppercase English letters.
#
# You have to find how many times subsequence "AG" is there in the given string.
#
# NOTE: Return the answer modulo 109 + 7 as the answer can be very large.
#
#
#
# Problem Constraints
# 1 <= length(A) <= 105
#
#
#
# Input Format
# First and only argument is a string A.
#
#
#
# Output Format
# Return an integer denoting the answer.
#
#
#
# Example Input
# Input 1:
#
#  A = "ABCGAG"
# Input 2:
#
#  A = "GAB"
#
#
# Example Output
# Output 1:
#
#  3
# Output 2:
#
#  0
#
#
# Example Explanation
# Explanation 1:
#
#  Subsequence "AG" is 3 times in given string
# Explanation 2:
#
#  There is no subsequence "AG" in the given string.



def solve(A: str) -> int:
    n = len(A)
    mod = 1e9 + 7
    count_of_a = 0
    final_count = 0

    for i in range(n):
        if A[i] == 'A':
            count_of_a += 1
        elif A[i] == 'G':
            final_count += count_of_a
        else:
            pass

    return int(final_count % mod)


if __name__ == "__main__":
    a = "ABCGAG"
    print(solve(a))
