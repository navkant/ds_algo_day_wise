from typing import List


def common_elements(A: List[int], B: List[int]) -> List[int]:
    hash_map = {}

    for num in A:
        if num not in hash_map:
            hash_map[num] = 1
        else:
            hash_map[num] += 1

    common_nums = []

    for num in B:
        if num in hash_map and hash_map[num] > 0:
            common_nums.append(num)
            hash_map[num] -= 1
        else:
            pass

    return common_nums


if __name__ == "__main__":
    A = [1, 2, 2, 1]
    B = [2, 3, 1, 2]

    print(common_elements(A, B))
