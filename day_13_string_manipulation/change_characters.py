# Problem Description
# You are given a string A of size N consisting of lowercase alphabets.
# You can change at most B characters in the given string to any other lowercase alphabet such that the number of
# distinct characters in the string is minimized.
# Find the minimum number of distinct characters in the resulting string.

# Problem Constraints
# 1 <= N <= 100000
# 0 <= B <= N

# Input Format
# The first argument is a string A.
# The second argument is an integer B.

# Output Format
# Return an integer denoting the minimum number of distinct characters in the string.

# Example Input
# A = "abcabbccd"
# B = 3

# Example Output
# 2

# Example Explanation
# We can change both 'a' and one 'd' into 'b'.So the new string becomes "bbcbbbccb".
# So the minimum number of distinct character will be 2.


def change_characters(A: str, B: int) -> int:
    if len(A) == 1:
        return 1

    arr = [0] * 26
    ans = 0
    for i in A:
        arr[ord(i) - 97] += 1
        if arr[ord(i) - 97] == 1:
            ans += 1

    arr.sort()

    for i in range(26):
        if B - arr[i] >= 0 and arr[i] != 0:
            ans -= 1
            B -= arr[i]
    return ans


if __name__ == "__main__":
    a = "abcabbccd"
    print(change_characters(a))