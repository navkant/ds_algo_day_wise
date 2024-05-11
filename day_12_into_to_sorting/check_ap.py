from typing import List

def check_ap(A: List[int]) -> bool:
    A = sorted(A)
    cd = A[0] - A[1]

    for i in range(1, len(A)):
        if A[i] - A[i-1] != cd:
            return 0

    return 1


if __name__ == "__main__":
    A = []
    