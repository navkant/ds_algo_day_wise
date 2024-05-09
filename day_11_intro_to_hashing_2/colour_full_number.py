# Problem Description
# Given a number A, find if it is COLORFUL number or not.
# If number A is a COLORFUL number return 1 else, return 0.
#
# What is a COLORFUL Number:
#
# A number can be broken into different consecutive sequence of digits.
# The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245.
# This number is a COLORFUL number, since the product of every consecutive sequence of digits is different
#
#
# Problem Constraints
# 1 <= A <= 2 * 109
#
#
#
# Input Format
# The first and only argument is an integer A.
#
#
#
# Output Format
# Return 1 if integer A is COLORFUL else return 0.
#
#
#
# Example Input
# Input 1:
#
#  A = 23
# Input 2:
#
#  A = 236
#
#
# Example Output
# Output 1:
#
#  1
# Output 2:
#
#  0
#
#
# Example Explanation
# Explanation 1:
#
#  Possible Sub-sequences: [2, 3, 23] where
#  2 -> 2
#  3 -> 3
#  23 -> 6  (product of digits)
#  This number is a COLORFUL number since product of every digit of a sub-sequence are different.
# Explanation 2:
#
#  Possible Sub-sequences: [2, 3, 6, 23, 36, 236] where
#  2 -> 2
#  3 -> 3
#  6 -> 6
#  23 -> 6  (product of digits)
#  36 -> 18  (product of digits)
#  236 -> 36  (product of digits)
#  This number is not a COLORFUL number since the product sequence 23  and sequence 6 is same.


def solve(A: int):
    number_sequence = []
    hash_map = {}
    num = A
    while num:
        rem = num % 10
        number_sequence.append(rem)
        if rem in hash_map:
            return 0
        else:
            hash_map[rem] = 1
        num = num // 10

    if len(number_sequence) == 1:
        return 1
    elif len(number_sequence) == 2:
        if 1 in number_sequence:
            return 0

    number_sequence.reverse()

    for i in range(len(number_sequence)-1):
        j = i + 1
        product = number_sequence[i]
        while j < len(number_sequence):
            product *= number_sequence[j]
            if product not in hash_map:
                hash_map[product] = 1
            else:
                return 0
            j += 1

    return 1


if __name__ == "__main__":
    A = 1
    print(solve(A))




