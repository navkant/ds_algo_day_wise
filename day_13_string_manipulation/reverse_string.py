# Problem Description
# You are given a string A of size N.
#
# Return the string A after reversing the string word by word.
#
# NOTE:
#
# A sequence of non-space characters constitutes a word.
# Your reversed string should not contain leading or trailing spaces, even if it is present in the input string.
# If there are multiple spaces between words, reduce them to a single space in the reversed string.
#
#
# Problem Constraints
# 1 <= N <= 3 * 105
#
#
#
# Input Format
# The only argument given is string A.
#
#
#
# Output Format
# Return the string A after reversing the string word by word.
#
#
#
# Example Input
# Input 1:
# A = "the sky is blue"
# Input 2:
# A = "this is ib"
#
#
# Example Output
# Output 1:
# "blue is sky the"
# Output 2:
# "ib is this"
#
#
# Example Explanation
# Explanation 1:
# We reverse the string word by word so the string becomes "blue is sky the".
# Explanation 2:
# We reverse the string word by word so the string becomes "ib is this".

def reverse_string(A: str) -> str:
    inter_list = A.split(" ")[::-1]
    inter_list = [string.strip() for string in inter_list]
    return " ".join(inter_list)


if __name__ == "__main__":
    A = 'e jrkeymu coklj si vohl slje sxtpf xvak p kicqxoqaof uqwftidoi xixfvqbjey n tpkh ylqllzln ljo gvozwv'
    print(reverse_string(A))