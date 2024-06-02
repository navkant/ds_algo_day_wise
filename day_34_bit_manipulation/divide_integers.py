# Problem Description
# Divide two integers without using multiplication, division and mod operator.
#
# Return the floor of the result of the division.
#
# Also, consider if there can be overflow cases i.e output is greater than INT_MAX, return INT_MAX.
#
# NOTE: INT_MAX = 2^31 - 1
#
#
#
# Problem Constraints
# -231 <= A, B <= 231-1
#
# B != 0
#
#
#
# Input Format
# The first argument is an integer A denoting the dividend.
# The second argument is an integer B denoting the divisor.
#
#
#
# Output Format
# Return an integer denoting the floor value of the division.
#
#
#
# Example Input
# Input 1:
#
#  A = 5
#  B = 2
# Input 2:
#
#  A = 7
#  B = 1
#
#
# Example Output
# Output 1:
#
#  2
# Output 2:
#
#  7
#
#
# Example Explanation
# Explanation 1:
#
#  floor(5/2) = 2


def solve(A: int, B: int) -> int:
        ans = 0
        m = abs(A)
        n = abs(B)
        sign = 0

        if A < 0:
            sign = -sign
        if B < 0:
            sign = -sign

        for i in range(31, -1, -1):
            if (n << i) <= m:
                m -= n << i
                ans += 1 << i

        if sign < 0:
            ans = -ans

        return ans


if __name__ == "__main__":
    a = 5
    b = 2
    print(solve(a, b))
