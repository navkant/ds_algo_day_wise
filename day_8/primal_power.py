# Problem Description

# "Primal Power" of an array is defined as the count of prime numbers present in it.

# Given an array of integers A of length N, you have to calculate its Primal Power.



# Problem Constraints

# 1 <= N <= 103

# -106 <= A[i] <= 106



# Input Format

# First and only argument is an integer array A.



# Output Format

# Return the Primal Power of array A.



# Example Input

# Input 1:

#  A = [-6, 10, 12]
# Input 2:

#  A = [-11, 7, 8, 9, 10, 11]

from typing import List
import math

def is_prime(number: int) -> bool:
    sq_root = int(math.sqrt(number))

    for i in range(2, sq_root+1):
        if number % i == 0:
            return False
    
    return True



def primal_power(A: List[int]) -> int:
    count = 0

    for num in A:
        if num < 0:
            continue
        if is_prime(num):
            count += 1
        else:
            pass
    
    return count


if __name__ == "__main__":
    A = [-11, 7, 8, 9, 2, 10, 11]
    print(primal_power(A))