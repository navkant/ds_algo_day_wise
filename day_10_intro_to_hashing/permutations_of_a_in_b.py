from typing import List

def same_hash(hash_1: List[int], hash_2: List[int]):
    for i in range(len(hash_1)):
        if hash_1[i] != hash_2[i]:
            return 0
    return 1


def permutations_of_a_in_b(A: str, B: str):
    n = len(A)
    m = len(B)
    count = 0

    hash_a = [0] * 26
    hash_b = [0] * 26

    for i in range(n):
        hash_a[ord(A[i]) - ord('a')] += 1

    for i in range(n):
        hash_b[ord(B[i]) - ord('a')] += 1

    count += same_hash(hash_a, hash_b)

    j = 0
    for i in range(n, m):
        hash_b[ord(B[j]) - ord("a")] -= 1
        hash_b[ord(B[i]) - ord("a")] += 1
        count += same_hash(hash_a, hash_b)
        j += 1

    return count


if __name__ == "__main__":
    A = "abc"
    B = "abcbacabc"
    print(permutations_of_a_in_b(A, B))
