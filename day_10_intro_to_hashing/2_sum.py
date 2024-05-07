from typing import Tuple, List


def two_sum(A: Tuple[int, ...], B: int) -> List[int]:
    map_dict = {}

    for index, number in enumerate(A):
        if B - number not in map_dict:
            if number not in map_dict:
                map_dict[number] = index
        else:
            return [map_dict[B - number] + 1, index + 1]

    return []


if __name__ == "__main__":
    arr = [1,2,3]
    point = 5
    print(two_sum(arr, point))