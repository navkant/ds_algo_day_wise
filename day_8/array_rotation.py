# Problem Description
# Given an integer array A of size N and an integer B, you have to print the same array after rotating it B times towards the right.


# Problem Constraints
# 1 <= N <= 106
# 1 <= A[i] <=108
# 1 <= B <= 109


# Input Format
# There are 2 lines in the input

# Line 1: The first number is the size N of the array A. Then N numbers follow which indicate the elements in the array A.

# Line 2: A single integer B.


# Output Format
# Print array A after rotating it B times towards the right.


# Example Input
# Input 1 :
# 4 1 2 3 4
# 2


# Example Output
# Output 1 :
# 3 4 1 2

from typing import List


def reverse_array(arr: List[int], start: int, end: int) -> None:
    mid = int(start + (end-start) / 2)
    print(f"start: {start}, mid: {mid}, end: {end}")

    if (end-start) % 2 != 0:
        for i in range(start, mid+1):
            arr[i], arr[end - (i - start)] = arr[end - (i - start)], arr[i]
    else:
        for i in range(start, mid+1):
            arr[i], arr[end - (i - start)] = arr[end - (i - start)], arr[i]


def rotate_array(A: List[int], B: int) -> None:
    n = len(A)

    reverse_array(A, 0, n-1)
    print(A)
    reverse_array(A, 0, B-1)
    print(A)
    reverse_array(A, B, n-1)
    print(A)


if __name__ == "__main__":
    A = [1, 2, 3, 4, 5, 6, 7]
    B = 7
    print(A)
    rotate_array(A, B)
