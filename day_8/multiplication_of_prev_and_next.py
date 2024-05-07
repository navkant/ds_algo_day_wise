# Given an array of integers A, update every element with multiplication of previous and next elements with 
# following exceptions. a) First element is replaced by multiplication of first and second. b) Last element 
# is replaced by multiplication of last and second last.


# Input Format

# The only argument given is the integer array A.
# Output Format

# Return the updated array.
# Constraints

# 1 <= length of the array <= 100000
# -10^4 <= A[i] <= 10^4 
# For Example

# Input 1:
#     A = [1, 2, 3, 4, 5]
# Output 1:
#     [2, 3, 8, 15, 20]

# Input 2:
#     A = [5, 17, 100, 11]
# Output 2:
#     [85, 500, 187, 1100]
# Expected Output
# Provide sample input and click run to see the correct output for the provided input. Use this to improve your problem understanding and test edge cases
from typing import List


def multiplication(A: List[int]) -> List[int]:

    for i in range(len(A)):
        if i == 0:
            A[i] = A[i] * A[i+1]
        elif i == len(A)-1:
            A[i] = A[i-1] * A[i]
        else:
            A[i] = A[i-1] * A[i+1]
    
    return A
