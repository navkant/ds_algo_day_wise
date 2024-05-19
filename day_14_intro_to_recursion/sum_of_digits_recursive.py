# Given a number A, we need to find the sum of its digits using recursion.


def solve(A: int) -> int:
    if A == 0:
        return 0

    last_digit = A % 10
    A = A // 10

    return last_digit + solve(A)


if __name__ == "__main__":
    a = 64637
    print(solve(a))
