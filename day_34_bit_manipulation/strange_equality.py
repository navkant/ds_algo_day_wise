# Problem Description
# Given an integer A.
# Two numbers, X and Y, are defined as follows:
#
# X is the greatest number smaller than A such that the XOR sum of X and A is the same as the sum of X and A.
# Y is the smallest number greater than A, such that the XOR sum of Y and A is the same as the sum of Y and A.
# Find and return the XOR of X and Y.
#
# NOTE 1: XOR of X and Y is defined as X ^ Y where '^' is the BITWISE XOR operator.
#
# NOTE 2: Your code will be run against a maximum of 100000 Test Cases.
#
#
#
# Problem Constraints
# 1 <= A <= 109
#
#
#
# Input Format
# First and only argument is an integer A.
#
#
#
# Output Format
# Return an integer denoting the XOR of X and Y.
#
#
#
# Example Input
# A = 5
#
#
# Example Output
# 10
#
#
# Example Explanation
# The value of X will be 2 and the value of Y will be 8. The XOR of 2 and 8 is 10.


def solve(A: int):

        for i in range(32):
            if 1 << i <= A:
                continue
            else:
                y = 1 << i
                break

        x = 0

        for i in range(len(bin(A)[2:])):
            if not A >> i & 1:
                x = x | 1 << i
            else:
                continue

        print(x, y)
        return x ^ y


if __name__ == "__main__":
    a = 5
    print(solve(a))
