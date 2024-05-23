# Problem Description
# Given a column title as appears in an Excel sheet, return its corresponding column number.

# Problem Constraints
# 1 <= length of the column title <= 5

# Input Format
# The only argument is a string that represents the column title in the excel sheet.

# Output Format
# Return a single integer that represents the corresponding column number.

# Example Input
# Input 1:
#  AB

# Input 2:
#  BB

# Example Output
# Output 1:
#  28

# Output 2:
#  54

# Example Explanation
# Explanation 1:
#  A -> 1
#  B -> 2
#  C -> 3
#  ...
#  Z -> 26
#  AA -> 27
#  AB -> 28
# Explanation 2:
#
#  A -> 1
#  B -> 2
#  C -> 3
#  ...
#  Z -> 26
#  AA -> 27
#  AB -> 28
#  ...
#  AZ -> 52
#  BA -> 53
#  BB -> 54


def solve(A: str) -> int:
    mapping_array = [i for i in range(1, 27)]

    ans = 0
    for i in range(len(A)-1, -1, -1):
        place_value = len(A) - 1 - i

        ans += mapping_array[ord(A[i]) - ord('A')] * (26 ** place_value)

    return ans


if __name__ == "__main__":
    string = "BA"
    print(solve(string))